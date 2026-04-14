#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:

    value = int(temp_str)
    if value < 0:
        raise Exception(f"{value}°C is too cold for plants (min 0°C)")

    elif value > 40:
        raise Exception(f"{value}°C is too hot\
 for plants (max 40°C)")

    return value


def show(temp_str):
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")


def test_temperature():
    print("=== Garden Temperature ===\n")
    temp_str = "25"
    show(temp_str)

    temp_str = "abc"
    show(temp_str)

    temp_str = "100"
    show(temp_str)

    temp_str = "-50"
    show(temp_str)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
