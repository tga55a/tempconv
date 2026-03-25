ABSOLUTE_ZERO_C = -273.15


# Absolute zero in Celsius
ABSOLUTE_ZERO_C = -273.15

def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:

    return (f - 32) * 5/9

def celsius_to_kelvin(c: float) -> float:
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("c < ABSOLUTE_ZERO_C")
    return c + 273.15

def kelvin_to_celsius(k: float) -> float:
    # TODO: implement (remember: Kelvin cannot be negative)
    if k < 0:
        raise ValueError("k < 0")
    
    return k - 273.15

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature between any supported units.

    Units: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    Raises: ValueError for unknown units or invalid temperatures.

    Examples:
        convert(100, 'C', 'F')  →  212.0
        convert(32,  'F', 'C')  →  0.0
        convert(0,   'C', 'K')  →  273.15
    """

    # Normalize to uppercase so 'c' and 'C' both work
    from_unit = from_unit.upper()
    to_unit   = to_unit.upper()

    # If same unit, return as-is
    if from_unit == to_unit:
        return float(value)

    # TODO: implement the conversion routing.
    # Hint: convert via Celsius as the intermediate unit.
    # C → F, C → K, F → C, F → K (via C), K → C, K → F (via C)
    # Raise ValueError for unknown units.
    supported_units = ["C","F","K"]
    if (not from_unit in supported_units) or (not to_unit in supported_units):
        raise ValueError("unknown units or invalid temperatures.")
    
    if from_unit == "C" and to_unit == "F":
        return celsius_to_fahrenheit(value)
    elif from_unit == "C" and to_unit == "K":
        return celsius_to_kelvin(value)
    elif from_unit == "F" and to_unit == "C":
        return fahrenheit_to_celsius(value)
    elif from_unit == "F" and to_unit == "K":
        value_in_celsius = fahrenheit_to_celsius(value)
        return celsius_to_kelvin(value_in_celsius)
    elif from_unit == "K" and to_unit == "C":
        return kelvin_to_celsius(value)
    elif from_unit == "K" and to_unit == "F":
        value_in_celsius = kelvin_to_celsius(value)
        return celsius_to_fahrenheit(value)
    else:
        raise ValueError
    
    
    