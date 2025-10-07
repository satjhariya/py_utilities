import queue

class msgBus:
    def __init__(self):
        self.q = queue.Queue()

    def publish(self, msg:dict):
        self.q.put(msg)

    def listen(self):
        try:
            return self.q.get_nowait()
        except queue.Empty:
            return None
        
if __name__ == "__main__":
    pass