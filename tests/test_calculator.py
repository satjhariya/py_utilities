import pytest

from pyUtils.src.calculator import calc
from pyUtils.src.message_bus import msgBus


class FakeBus:
    def __init__(self):
        self.published = []

    def publish(self, msg: dict):
        self.published.append(msg)


@pytest.fixture
def fake_bus():
    return FakeBus()


def test_add_publishes_result(fake_bus):
    c = calc(fake_bus)
    msg = {"target": "calc", "cmd": "add", "args": [5, 3]}
    c.handle_message(msg)

    assert len(fake_bus.published) == 1
    published = fake_bus.published[0]
    assert published.get("event") == "CALC_RESULT"
    assert published.get("data") == 8


def test_unknown_command_returns_error(fake_bus):
    c = calc(fake_bus)
    msg = {"target": "calc", "cmd": "pow", "args": [2, 3]}
    c.handle_message(msg)

    assert len(fake_bus.published) == 1
    published = fake_bus.published[0]
    assert published.get("event") == "CALC_ERROR"
    assert "unknown command" in published.get("error", "").lower()


def test_divide_by_zero_returns_error(fake_bus):
    c = calc(fake_bus)
    msg = {"target": "calc", "cmd": "divide", "args": [4, 0]}
    c.handle_message(msg)

    assert len(fake_bus.published) == 1
    published = fake_bus.published[0]
    assert published.get("event") == "CALC_ERROR"
    assert "division by zero" in published.get("error", "").lower()


def test_integration_with_msgbus():
    bus = msgBus()
    c = calc(bus)

    # publish a message to the queue
    bus.publish({"target": "calc", "cmd": "multiply", "args": [6, 7]})

    # simulate the listener loop: get message and pass to calculator
    incoming = bus.listen()
    assert incoming is not None
    c.handle_message(incoming)

    # result should be published back to the bus queue
    outgoing = bus.listen()
    assert outgoing is not None
    assert outgoing.get("event") == "CALC_RESULT"
    assert outgoing.get("data") == 42


@pytest.mark.parametrize(
    "msg,expected",
    [
        ({"target": "calc", "cmd": "add", "args": [1, 2]}, 3),
        ({"target": "calc", "cmd": "multiply", "args": [3, 5]}, 15),
        ({"target": "calc", "cmd": "subtract", "args": [10, 4]}, 6),
    ],
)
def test_dynamic_messages(msg, expected):
    """Demonstrates feeding dynamic inputs (parametrized) into the message bus.

    Each message is published to a real `msgBus`, popped with `listen()`, passed to
    the calculator, and then the result is read back from the bus.
    """
    bus = msgBus()
    c = calc(bus)

    bus.publish(msg)
    incoming = bus.listen()
    assert incoming is not None

    c.handle_message(incoming)

    outgoing = bus.listen()
    assert outgoing is not None
    assert outgoing.get("event") == "CALC_RESULT"
    assert outgoing.get("data") == expected
