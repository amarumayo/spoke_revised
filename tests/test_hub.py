import pytest
from src.hub import Hub

def test_Hub_does_not_accept_negative_lfo():
    with pytest.raises(ValueError):
        hub = Hub(lfo=-5)

def test_Hub_does_not_accept_negative_rfo():
    with pytest.raises(ValueError):
        hub = Hub(rfo=-5)

def test_Hub_does_not_accept_negative_old():
    with pytest.raises(ValueError):
        hub = Hub(old=-5)

def test_Hub_does_not_accept_negative_dl():
    with pytest.raises(ValueError):
        hub = Hub(dl=-5)

def test_Hub_does_not_accept_negative_dr():
    with pytest.raises(ValueError):
        hub = Hub(dr=-5)

def test_Hub_does_not_accept_negative_shd():
    with pytest.raises(ValueError):
        hub = Hub(shd=-5)

def test_Hub_does_not_accept_negative_osb():
    with pytest.raises(ValueError):
        hub = Hub(osb=-5)

