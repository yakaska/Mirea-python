# void decrypt(uint32_t v[2], const uint32_t k[4]) {
#     uint32_t v0 = v[0], v1 = v[1], sum = 0xC6EF3720, i;
#     uint32_t delta = 0x9E3779B9;
#     uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];
#     for (i = 0; i < 32; i++) {
#         v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
#         v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
#         sum -= delta;
#     }
#     v[0] = v0; v[1] = v1;
# }


from ctypes import c_uint32


def lshift4(a):
    return c_uint32(a << 4).value


def rshift5(a):
    return c_uint32(a >> 5).value


def lshift4_add(a, b):
    result = lshift4(a) + c_uint32(b).value
    return c_uint32(result).value


def rshift5_add(a, b):
    result = rshift5(a) + c_uint32(b).value
    return c_uint32(result).value


def add(a, b):
    result = c_uint32(a).value + c_uint32(b).value
    return c_uint32(result).value


def sub(a, b):
    result = c_uint32(a).value - c_uint32(b).value
    return c_uint32(result).value


def xor(a, b, c):
    middle = c_uint32(a).value ^ c_uint32(b).value
    return c_uint32(middle ^ c_uint32(c).value).value


def decrypt_block(block, key):
    summation = 0xC6EF3720
    delta = 0x9E3779B9
    for _ in range(0, 32):
        block[1] = sub(
            block[1],
            xor(
                lshift4_add(block[0], key[2]),
                add(block[0], summation),
                rshift5_add(block[0], key[3])
            )
        )
        block[0] = sub(
            block[0],
            xor(
                lshift4_add(block[1], key[0]),
                add(block[1], summation),
                rshift5_add(block[1], key[1])
            )
        )
        summation = c_uint32(summation - delta).value
    return block


message = "E3238557 6204A1F8 E6537611 174E5747 5D954DA8 8C2DFE97 2911CB4C 2CB7C66B " \
          "E7F185A0 C7E3FA40 42419867 374044DF 2519F07D 5A0C24D4 F4A960C5 31159418 " \
          "F2768EC7 AEAF14CF 071B2C95 C9F22699 FFB06F41 2AC90051 A53F035D 830601A7 " \
          "EB475702 183BAA6F 12626744 9B75A72F 8DBFBFEC 73C1A46E FFB06F41 2AC90051 " \
          "97C5E4E9 B1C26A21 DD4A3463 6B71162F 8C075668 7975D565 6D95A700 7272E637"

k = [0, 4, 5, 1]

message = message.split(' ')
res = []
for i in range(1, len(message), 2):
    block1 = c_uint32(int(message[i - 1], 16)).value
    block2 = c_uint32(int(message[i], 16)).value
    res.extend(decrypt_block([block1, block2], k))
res = "".join(map(chr, res))
print(res)
