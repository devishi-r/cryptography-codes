def galois_mult(a, b):
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        h = a & 0x80
        a <<= 1
        if h:
            a ^= 0x1b
        b >>= 1
    return res & 0xff

def shift_rows(s):
    return [
        s[0],
        s[1][1:] + s[1][:1],
        s[2][2:] + s[2][:2],
        s[3][3:] + s[3][:3]
    ]

def mix_cols(s):
    m = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
    return [[galois_mult(m[r][0], s[0][c]) ^ galois_mult(m[r][1], s[1][c]) ^
             galois_mult(m[r][2], s[2][c]) ^ galois_mult(m[r][3], s[3][c])
             for c in range(4)] for r in range(4)]

s = [[0x32, 0x88, 0x31, 0xE0], [0x43, 0x5A, 0x31, 0x37],
     [0xF6, 0x30, 0x98, 0x07], [0xA8, 0x8D, 0xA2, 0x34]]

print("Original:", [' '.join(f'{x:02X}' for x in r) for r in s])
s = shift_rows(s)
print("Shifted:", [' '.join(f'{x:02X}' for x in r) for r in s])

s = [[0xD4, 0xBF, 0x5D, 0x30], [0xE0, 0xB4, 0x52, 0xAE],
     [0xB8, 0x41, 0x11, 0xF1], [0x1E, 0x27, 0x98, 0xE5]]

print("Original:", [' '.join(f'{x:02X}' for x in r) for r in s])
s = mix_cols(s)
print("Mixed:", [' '.join(f'{x:02X}' for x in r) for r in s])