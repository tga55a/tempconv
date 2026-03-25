import pytest
from src.converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    convert,
)


def test_freezing_c_to_f(freezing_point):
    assert celsius_to_fahrenheit(freezing_point["C"]) == freezing_point["F"]


def test_boiling_c_to_f(boiling_point):
    assert celsius_to_fahrenheit(boiling_point["C"]) == boiling_point["F"]


@pytest.mark.parametrize(
    "c, expected_f",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
    ],
)
def test_c_to_f_cases(c, expected_f):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected_f, rel=1e-3)


@pytest.mark.edge
def test_absolute_zero_kelvin():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)


@pytest.mark.edge
def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)