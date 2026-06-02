import math
import pytest
from src.hub import Hub
from src.rim import Rim
from src.wheel import Wheel

def test_make_calc_does_correct_calc():
    hub = Hub(lfo=35, rfo=20, old=100, dl=58, dr=58, shd=2.5, osb=0)
    rim = Rim(erd=600, num_spokes=32, num_crosses=3)
    wheel = Wheel(hub=hub, rim=rim)
    right, left = wheel.make_calc()

    assert math.isclose(right, 289.6, abs_tol=0.1)
    assert math.isclose(left, 291.0, abs_tol=0.1)


