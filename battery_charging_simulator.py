import time


def battery_charging_simulator():

    print("=" * 65)
    print("           BATTERY CHARGING ALGORITHM SIMULATOR")
    print("=" * 65)

    # Battery inputs
    capacity = float(input("Enter battery capacity (Ah): "))
    initial_soc = float(input("Enter initial SOC (%): "))
    battery_voltage = float(input("Enter nominal battery voltage (V): "))
    charge_current = float(input("Enter charging current (A): "))
    max_voltage = float(input("Enter maximum charging voltage (V): "))

    # Validation
    if capacity <= 0:
        print("Battery capacity must be greater than zero.")
        return

    if not 0 <= initial_soc <= 100:
        print("SOC must be between 0 and 100%.")
        return

    if battery_voltage <= 0:
        print("Battery voltage must be greater than zero.")
        return

    if charge_current <= 0:
        print("Charging current must be greater than zero.")
        return

    if max_voltage <= battery_voltage:
        print("Maximum charging voltage must be greater than nominal voltage.")
        return

    if initial_soc >= 100:
        print("Battery is already fully charged.")
        return

    # --------------------------------------------------
    # CONSTANT CURRENT STAGE
    # --------------------------------------------------

    print("\n" + "-" * 65)
    print("STAGE 1: CONSTANT CURRENT (CC)")
    print("-" * 65)

    soc = initial_soc
    voltage = battery_voltage

    cc_target = 80.0

    # Simplified voltage rise model
    voltage_range = max_voltage - battery_voltage

    while soc < cc_target:

        # Increase SOC based on charging current
        soc += (charge_current / capacity) * 10

        if soc > cc_target:
            soc = cc_target

        # Approximate battery voltage rise
        voltage = battery_voltage + (
            voltage_range * (soc / 100)
        )

        print(
            f"SOC: {soc:6.2f}% | "
            f"Voltage: {voltage:5.2f} V | "
            f"Current: {charge_current:5.2f} A"
        )

        time.sleep(0.2)

    print("\nCC stage completed.")
    print("Transitioning to Constant Voltage...")

    # --------------------------------------------------
    # CONSTANT VOLTAGE STAGE
    # --------------------------------------------------

    print("\n" + "-" * 65)
    print("STAGE 2: CONSTANT VOLTAGE (CV)")
    print("-" * 65)

    voltage = max_voltage
    current = charge_current

    while soc < 100:

        # Current gradually decreases
        current *= 0.82

        # Minimum charging current
        if current < 0.1:
            current = 0.1

        # SOC increases more slowly
        soc += (current / capacity) * 5

        if soc > 100:
            soc = 100

        print(
            f"SOC: {soc:6.2f}% | "
            f"Voltage: {voltage:5.2f} V | "
            f"Current: {current:5.2f} A"
        )

        if current <= 0.1:
            break

        time.sleep(0.2)

    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    print("\n" + "=" * 65)
    print("                  CHARGING RESULT")
    print("=" * 65)

    print(f"Initial SOC          : {initial_soc:.2f}%")
    print(f"Final SOC            : {soc:.2f}%")
    print(f"Battery Capacity     : {capacity:.2f} Ah")
    print(f"Nominal Voltage      : {battery_voltage:.2f} V")
    print(f"Maximum Voltage      : {max_voltage:.2f} V")

    if soc >= 100:
        print("Battery Status       : FULLY CHARGED")
    else:
        print("Battery Status       : CHARGING")

    print("=" * 65)


if __name__ == "__main__":
    battery_charging_simulator()
