from message_bus import msgBus


class calc:
    def __init__(self, bus: msgBus):
        self.bus = bus
        self.ops = {
            "add": self.add,
            "subtract": self.subtract,
            "multiply": self.multiply,
            "divide": self.divide,
        }

    def handle_message(self, msg: dict):
        """Process an incoming message intended for the calculator.

        Expected message shape:
          {"target": "calc", "cmd": "add", "args": [a, b]}
        """
        try:
            if msg.get("target") != "calc":
                return

            cmd = msg.get("cmd")
            args = msg.get("args", [])

            if cmd not in self.ops:
                raise ValueError(f"unknown command: {cmd}")

            result = self.ops[cmd](*args)
            # publish a consistent event name and data
            self.bus.publish({"event": "CALC_RESULT", "data": result})
        except Exception as e:
            # publish error information
            self.bus.publish({"event": "CALC_ERROR", "error": str(e)})

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b


if __name__ == "__main__":
    pass