from pyUtils.src.calc_adapter import calcAdapter
from pyUtils.src.pure_calc import pure_calc
import pytest

class FakeBus:
    def __init__(self):
        self.published = []

    def publish(self, msg):
        print(f"Published: {msg}") 
        

@pytest.fixture
def fake_bus():
    return FakeBus()

def test_add(fake_bus):
    """
    Test the addition operation via the calcAdapter using a fake message bus.

    This test sends an 'add' command with arguments 5 and 3 to the calcAdapter,
    verifies that a single message is published to the bus, and checks that the
    published event is 'CALC_RESULT' with the correct result data (8).
    """
    c = calcAdapter(fake_bus, pure_calc())
    msg = {"target": "calc", "cmd": "add", "args": [5, 3]}
    c.handle_message(msg)
    assert len(fake_bus.published) == 1
    published = fake_bus.published[0]
    assert published.get("event") == "CALC_RESULT"
    assert published.get("data") == 8

def test_divide_by_zero(fake_bus):
    """
    Test the divide operation with zero as the divisor via the calcAdapter using a fake message bus.

    This test sends a 'divide' command with arguments 4 and 0 to the calcAdapter,
    verifies that a single message is published to the bus, and checks that the
    published event is 'CALC_ERROR' with an appropriate error message indicating
    that division by zero is not allowed.
    """
    c = calcAdapter(fake_bus, pure_calc())
    msg = {"target": "calc", "cmd": "divide", "args": [4, 0]}
    c.handle_message(msg)
    assert len(fake_bus.published) == 1
    published = fake_bus.published[0]
    assert published.get("event") == "CALC_ERROR"
    assert "division by zero" in published.get("error", "").lower()