#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, error="Unknown garden error"):
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error="Unknown plant error"):
        super().__init__(error)


class WaterError(GardenError):
    def __init__(self, error="Unknown water error"):
        super().__init__(error)


def test_error_types():
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors..")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    test_error_types()
