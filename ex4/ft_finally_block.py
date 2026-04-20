#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, name):
        super().__init__(name)


def water_plant(plant_name):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")


def test_watering_system():
    print("Testing valid plants...")
    print("Opening watering system")

    vegetable = ["Tomato", "Lettuce", "Carrots"]
    for i in range(3):
        try:
            water_plant(vegetable[i])
        except PlantError as e:
            print(f"Caught GardenError: {e}")

    print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant(vegetable[0])
    except PlantError as e:
        print(f"Caught GardenError: {e}")

    try:
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
