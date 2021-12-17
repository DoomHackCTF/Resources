from binascii import crc32

correct_crc = int('0db3f6c0',16)

for h in range(2000):
    for w in range(2000):
        data = (
            b"\x49\x48\x44\x52"
            + w.to_bytes(4, byteorder="big")
            + h.to_bytes(4, byteorder="big")
            + b"\x08\x06\x00\x00\x00"
        )
        if crc32(data) & 0xffffffff == correct_crc:
            print("Width: ", end="")
            print(hex(w))
            print("Height :", end="")
            print(hex(h))
            exit()
