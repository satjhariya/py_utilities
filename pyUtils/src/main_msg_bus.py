from pyUtils.src.calculator import calc
from pyUtils.src.message_bus import msgBus
import time


if __name__ == "__main__":
    bus = msgBus()
    calculator = calc(bus)

    # Example usage
    bus.publish({"target": "calc", "cmd": "subtract", "args": [5, 3]})

    while True:
        msg = bus.listen()
        if msg:
            # route messages for calculator
            if msg.get("target") == "calc":
                # call the instance method, not the class
                calculator.handle_message(msg)
            # listen for calculator results
            elif msg.get("event") == "CALC_RESULT":
                print("Result:", msg.get("data"))
            elif msg.get("event") == "CALC_ERROR":
                print("Calculator error:", msg.get("error"))
        else:
            time.sleep(0.1)
