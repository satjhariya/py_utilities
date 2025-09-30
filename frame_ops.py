class UDPFrame:
    def __init__(self):
        pass

    @staticmethod
    def pack_frame(freame_dict):
        packed = b""
        for key,value in freame_dict.items():
            if isinstance(value, dict):
                packed += UDPFrame.pack_frame(value)
            else:
                packed += value[0].to_bytes(value[1], byteorder='big')
        return packed

    @staticmethod
    def unpack_frame(data, frame_structure):
        unpacked = {}
        offset = 0
        for key, value in frame_structure.items():
            if isinstance(value, dict):
                subframe_size = sum(v[1] for v in value.values())
                unpacked[key], _ = UDPFrame.unpack_frame(data[offset:offset + subframe_size], value)
                offset += subframe_size
            else:
                size = value[1]
                unpacked[key] = int.from_bytes(data[offset:offset + size], byteorder='big')
                offset += size
        return unpacked, offset
    
if __name__ == "__main__":
    
    # Example usage
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

    f = UDPFrame()
    frame['wall'][0] = 1<<3
    frame['subframe'] = subFrame
    packed_frame = f.pack_frame(frame)
    print(packed_frame)
    print(len(packed_frame))

    rx_frame = {
        "st1": [0x00,1],
        "st2": [0x0001,2],
        "st3": [0x0122,2],
    }

    rx = b"\x00\x00\x01\x01\x22"
    unpacked_frame, _ = UDPFrame.unpack_frame(rx, rx_frame)
    print(unpacked_frame)