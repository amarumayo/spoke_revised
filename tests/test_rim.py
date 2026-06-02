import pytest
from src.rim import Rim

def test_rim_does_not_accept_negative_erd():
    with pytest.raises(ValueError):
        rim = Rim(erd=-1, num_spokes=0, num_crosses=3)

def test_rim_does_not_accept_zero_spokes():
    with pytest.raises(ValueError):
        rim = Rim(erd=1, num_spokes=0, num_crosses=3)

def test_rim_does_not_accept_negative_crosses():
    with pytest.raises(ValueError):
        rim = Rim(erd=1, num_spokes=10, num_crosses=-1)