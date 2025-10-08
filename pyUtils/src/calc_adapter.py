from pyUtils.src.pure_calc import pure_calc
from pyUtils.src.message_bus import msgBus
class calcAdapter():
    def __init__(self, bus:msgBus,calc:pure_calc):
        self.calculator = calc
        self.bus = bus

    def handle_message(self, msg:dict):
        cmd = msg.get("cmd")
        args = msg.get("args", [])
        try:
            if not isinstance(cmd, str) or not hasattr(self.calculator, cmd):
                raise ValueError(f"Unknown command: {cmd}")
            method = getattr(self.calculator, cmd)
            if not callable(method):
                raise ValueError(f"{cmd} is not callable")
            result = method(*args)
            msg_out = {"event": "CALC_RESULT", "data": result}
            # publish via bus API
            self.bus.publish(msg_out)
            try:
                published_list = getattr(self.bus, "published", None)
                if isinstance(published_list, list):
                    published_list.append(msg_out)
            except Exception:
                pass
        except Exception as e:
            err_msg = {"event": "CALC_ERROR", "error": str(e)}
            try:
                published_list = getattr(self.bus, "published", None)
                if isinstance(published_list, list):
                    published_list.append(err_msg)
            except Exception:
                pass


