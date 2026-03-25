# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("c < ABSOLUTE_ZERO_C")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    if k < 0:
        raise ValueError("k < 0")
    return k - 273.15


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between any supported units.

    Units: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    Raises: ValueError for unknown units or invalid temperatures.
    """

    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return float(value)

    supported_units = ["C", "F", "K"]
    if from_unit not in supported_units or to_unit not in supported_units:
        raise ValueError("unknown units or invalid temperatures.")

    if from_unit == "C" and to_unit == "F":
        return celsius_to_fahrenheit(value)

    if from_unit == "C" and to_unit == "K":
        return celsius_to_kelvin(value)

    if from_unit == "F" and to_unit == "C":
        return fahrenheit_to_celsius(value)

    if from_unit == "F" and to_unit == "K":
        return celsius_to_kelvin(fahrenheit_to_celsius(value))

    if from_unit == "K" and to_unit == "C":
        return kelvin_to_celsius(value)

    if from_unit == "K" and to_unit == "F":
        return celsius_to_fahrenheit(kelvin_to_celsius(value))

    raise ValueError("invalid conversion")
