"""
Tests for the measure module.
"""

# imports
import molecool
import pytest
import numpy as np

def test_calculate_distance():
    
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculated_distance

# Test for the calculate_angle function

def test_calculate_angle():
    
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    expected_value = 90

    calculated_value = molecool.calculate_angle(r1,r2,r3,True)

    assert pytest.approx(expected_value) == calculated_value

@pytest.mark.parametrize("p1,p2,p3, expected_angle",[
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0 ]),np.array([0,0,0]),np.array([1,0,0]),45),
    (np.array([0,0,-1]),np.array([0,1,0]),np.array([1,0,0]),60),
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_value = molecool.calculate_angle(p1,p2,p3,True)

    assert pytest.approx(expected_angle) == calculated_value
