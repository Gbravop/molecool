"""
Test for the molecule module
"""

# Import package, test suite, and other packages as needed
import pytest
import molecool

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)
    
    actual_mass = 16.04
    
    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass