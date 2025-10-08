from pyUtils.src.message_bus import msgBus
from pyUtils.src.calc_adapter import calcAdapter
from pyUtils.src.pure_calc import pure_calc

if __name__ == "__main__":
    bus = msgBus()
    calc = pure_calc()
    adapter = calcAdapter(bus, calc)

    bus.publish({"target": "calc", "cmd": "divide", "args": [1, 2]})
    msg = bus.listen()
    if msg is not None:
        adapter.handle_message(msg)
    result_msg = bus.listen()
    print(result_msg)  # Should print the result of the addition