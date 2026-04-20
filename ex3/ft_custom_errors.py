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
    print("Testing PlantError...")
    try:
        raise PlantError("Tomato was dry")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Engine broke down")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing GardenError...")
    try:
        raise WaterError("Engine broke down")
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
