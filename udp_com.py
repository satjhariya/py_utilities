import socket
import threading
import queue
from frame_ops import UDPFrame as FrameStruct

class UDPClient(threading.Thread):
    def __init__(self, server_ip, server_port, local_port=0):
        super().__init__(daemon=True)
        self.server_addr = (server_ip, server_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', local_port))
        self.recv_queue = queue.Queue()
        self.running = threading.Event()
        self.last_response = None

    def run(self):
        self.running.set()
        while self.running.is_set():
            try:
                data, addr = self.sock.recvfrom(4096)
                self.recv_queue.put((data, addr))
                self.last_response = (data, addr)
            except Exception:
                break

    def stop(self):
        self.running.clear()
        self.sock.close()

    def send(self, data: bytes):
        self.sock.sendto(data, self.server_addr)

    def send_and_wait(self, data: bytes, timeout=5):
        self.send(data)
        try:
            response = self.recv_queue.get(timeout=timeout)
            self.last_response = response
            return response
        except queue.Empty:
            return None

    def get_last_response(self):
        return self.last_response
        

class UDPFrame:
    def __init__(self, header=0, payload=b'', footer=0):
        self.header = header      # integer
        self.payload = payload    # bytes
        self.footer = footer      # integer

    def set_payload(self, data: bytes):
        self.payload = data

    def set_header(self, value: int):
        self.header = value

    def set_footer(self, value: int):
        self.footer = value


# Example usage: run UDP client in a separate thread and send/receive data
if __name__ == "__main__":
    subFrame = {}
    subFrame["sub1"] = [0x01,1]
    subFrame["sub2"] = [0x02,2]
    subFrame["sub3"] = [0x03,1]
    frame = {
        "wall": [0x00,2],
        "freq": [0x01,1],
        "mode": [0x02,1],
        "start": [56467,3],
        "subframe": subFrame,
        "stop": [0x049878,3],
    }
    frame['wall'][0] = 1<<3
    frame['subframe'] = subFrame
    pack_frame = FrameStruct.pack_frame(frame)
    print(pack_frame)
    msg = pack_frame
    # msg = b"latest changes are to be tested\n"

    client = UDPClient('127.0.0.1', 12345)
    client.start()  # Start the thread
    response = client.send_and_wait(msg, timeout=5)
        # client.send(msg)
    data = None
    if response:
        data, addr = response
        print(f"Received from {addr}: {data}")
    else:
        print("No response received (timeout).")
    # You can access the last response anytime
    last = client.get_last_response()
    print(f"Last response: {last}")
    client.stop()
    print("unpacked data is ")
    unpack_dict = FrameStruct.unpack_frame(data,frame) if data else {}
    print(unpack_dict)
