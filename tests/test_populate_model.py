import pytest
from spoke.ui import App

class FakeField:
    def __init__(self, target, key, value):
        self.target = target   
        self.key = key         
        self._value = value    

    def get(self):
        return self._value

def test_populate_model_updates_hub():
    app = App()

    field = FakeField(target="hub", key="lfo", value="42.5")
    app._poplate_model(field)

    assert app.hub.lfo == 42.5


def test_populate_model_updates_rim():
    app = App()

    field = FakeField(target="rim", key="erd", value="600")
    app._poplate_model(field)

    assert app.rim.erd == 600.0
