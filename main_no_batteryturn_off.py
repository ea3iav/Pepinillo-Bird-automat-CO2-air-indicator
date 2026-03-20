import time
import machine
import sys
from machine import Pin, I2C, deepsleep, RTC
from sg90 import SG90

# ---------- DEBUG MODE ----------
DEBUG = sys.stdin is not None
print("DEBUG MODE:", DEBUG)

# ---------- APAGAR RADIOS ----------
try:
    import network
    network.WLAN(network.STA_IF).active(False)
    network.WLAN(network.AP_IF).active(False)
except:
    pass

try:
    import bluetooth
    bluetooth.BLE().active(False)
except:
    pass

# ---------- Hardware ----------
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
addr = 0x62

time.sleep(2)  # estabilizar tras boot

servo = SG90(4)
rtc = RTC()

# ---------- Config ----------
LIVE_ANGLE = 180
DEAD_ANGLE = 0

CO2_THRESHOLD = 1200

# ---------- Estado RTC ----------
try:
    mem = rtc.memory().decode().split(",")
    last_state = mem[0]
    cycle_count = int(mem[1])
except:
    last_state = None
    cycle_count = 0

current_angle = LIVE_ANGLE

# ---------- FUNCIONES ----------
def start_sensor():
    print("Starting SCD41...")

    for _ in range(5):
        try:
            i2c.writeto(addr, b'\x21\xb1')
            time.sleep(5)
            print("Sensor started")
            return True
        except OSError:
            print("Retrying sensor init...")
            time.sleep(1)

    return False


def read_co2():
    try:
        i2c.writeto(addr, b'\xec\x05')
        time.sleep_ms(10)
        data = i2c.readfrom(addr, 9)
        return data[0] << 8 | data[1]
    except OSError:
        return None


def move_smooth(start, end):
    global current_angle

    if start == end:
        return

    step = 1 if start < end else -1

    for angle in range(start, end, step):
        servo.set_angle(angle)
        time.sleep(0.02)

    servo.set_angle(end)
    current_angle = end


# =========================================================
# ===================== DEBUG MODE =========================
# =========================================================
if DEBUG:

    print("DEBUG MODE → continuous reading")

    servo.set_angle(LIVE_ANGLE)
    current_angle = LIVE_ANGLE
    time.sleep(1)

    start_sensor()

    last_state = None

    while True:
        co2 = read_co2()

        if co2 is not None:
            print("CO2:", co2)

            current_state = "BAD" if co2 > CO2_THRESHOLD else "OK"
            print("State:", current_state)

            if current_state != last_state:
                print("State changed → moving bird")

                target = DEAD_ANGLE if current_state == "BAD" else LIVE_ANGLE

                if current_angle != target:
                    move_smooth(current_angle, target)

                last_state = current_state

        else:
            print("Sensor not ready")

        time.sleep(5)


# =========================================================
# =================== LOW POWER MODE =======================
# =========================================================
else:

    print("Wake up...")
    print("Last state:", last_state)
    print("Cycle:", cycle_count)

    servo.set_angle(LIVE_ANGLE)
    current_angle = LIVE_ANGLE
    time.sleep(1)

    if start_sensor():

        co2 = read_co2()

        if co2 is not None:

            print("CO2:", co2)

            current_state = "BAD" if co2 > CO2_THRESHOLD else "OK"
            print("Current state:", current_state)

            if current_state != last_state:
                print("State changed → moving bird")

                target = DEAD_ANGLE if current_state == "BAD" else LIVE_ANGLE

                if current_angle != target:
                    move_smooth(current_angle, target)

                last_state = current_state

            else:
                print("No change → no movement")

        else:
            print("Sensor read failed")

    else:
        print("Sensor start failed")

    # ---------- ACTUALIZAR CICLO ----------
    cycle_count += 1
    rtc.memory(f"{last_state},{cycle_count}")

    # ---------- MODO INTELIGENTE ----------
    if cycle_count < 120:
        sleep_time = 30000  # 30s
        print("FAST MODE (30s)")
    else:
        sleep_time = 120000  # 120s
        print("ECO MODE (120s)")

    print("Sleeping...")
    deepsleep(sleep_time)
