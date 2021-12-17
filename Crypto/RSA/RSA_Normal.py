from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

e  = 3
ct = 39207274348578481322317340648475596807303160111338236677373 
p  = 752708788837165590355094155871
q  = 986369682585281993933185289261 
n  = p*q

phi = (p-1) * (q-1)

d = inverse(e, phi)
pt = pow(ct, d, n)
#print(pt)
decrypted = long_to_bytes(pt)
print(decrypted)
