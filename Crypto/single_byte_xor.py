import binascii
encoded = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    decoded = ''.join(chr(b ^ key) for b in encoded)
    if "crypto" in decoded:
        print(decoded)
        break
