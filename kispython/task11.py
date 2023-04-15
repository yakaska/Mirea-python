import struct


def read_b_mass(data, address):
    result = []
    for i in range(0, 16, 2):
        b = struct.unpack('>1B1b', data[address + i: address + i + 2])
        result.append({
            'B1': b[0],
            'B2': b[1]
        })
    return result


def read_d_addr(data, address):
    result = {}
    for d_address in struct.unpack('>H', data[address: address + 2]):
        d1 = struct.unpack('>q', data[d_address:d_address + 8])[0]
        d2 = list(struct.unpack('>2B', data[d_address + 8:d_address + 10]))
        d3 = struct.unpack('>I', data[d_address + 10:d_address + 14])[0]
        d4 = struct.unpack('>h', data[d_address + 14:d_address + 16])[0]
        d5 = struct.unpack('>f', data[d_address + 16:d_address + 20])[0]
        d6 = struct.unpack('>Q', data[d_address + 20:d_address + 28])[0]
        result = {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
            'D6': d6,
        }
    return result


def read_e_addr(data, address):
    result = {}
    for e_address in struct.unpack('>I', data[address:address + 4]):
        e1 = list(struct.unpack('>4f', data[e_address:e_address + 16]))
        e2 = struct.unpack('>H', data[e_address + 16:e_address + 18])[0]
        e3 = struct.unpack('>b', data[e_address + 18:e_address + 19])[0]
        result = {
            'E1': e1,
            'E2': e2,
            'E3': e3,
        }
    return result


def read_c_addr(data, address):
    result = {}
    for c_address in struct.unpack('>I', data[address:address + 4]):
        c1 = struct.unpack('>I', data[c_address:c_address + 4])[0]
        c2 = struct.unpack('>d', data[c_address + 4:c_address + 12])[0]
        c3 = struct.unpack('>2I', data[c_address + 12:c_address + 20])
        c3 = struct.unpack('>' + 'b' * c3[0], data[c3[1]:c3[1] + c3[0]])
        c3 = "".join(list(map(chr, c3)))
        c4 = read_d_addr(data, c_address + 20)
        c5 = read_e_addr(data, c_address + 22)
        c6 = struct.unpack('>i', data[c_address + 26: c_address + 30])[0]
        result = {
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
            'C6': c6
        }
    return result


def main(data):
    a1 = read_b_mass(data, 5)
    a2 = read_c_addr(data, 21)
    return {
        'A1': a1,
        'A2': a2
    }


print(main((b'oTTEB~\x91\xc5\xfbtW\x01\xfb\x9e\xae&\xc0d\xb7x6\x00\x00\x00Okkwsxkq'
            b'\x06Z\x86*\xf9.s\xeamW\x10\x90t\xf1\xa2\xd1\xbe\x01\x93\xda\xd2\xa7\xfd\x97'
            b'\x99\xafR7\xbfv\xa5\xd5?/\xbeu\xbf.\xcb\x02\xbe\xc8\xa9/=\xd0+\xc5'
            b'\x94\xf5\xb9\xbf\xec\x04\xaa\x8e2\xeeJ\x00\x00\x00\x07\x00\x00\x00\x19\x00'
            b' \x00\x00\x00<\xe04\xec\xc9')))

import pprint

# Prints the nicely formatted dictionary
pprint.pprint(main((b'oTTEB~\x91\xc5\xfbtW\x01\xfb\x9e\xae&\xc0d\xb7x6\x00\x00\x00Okkwsxkq'
                    b'\x06Z\x86*\xf9.s\xeamW\x10\x90t\xf1\xa2\xd1\xbe\x01\x93\xda\xd2\xa7\xfd\x97'
                    b'\x99\xafR7\xbfv\xa5\xd5?/\xbeu\xbf.\xcb\x02\xbe\xc8\xa9/=\xd0+\xc5'
                    b'\x94\xf5\xb9\xbf\xec\x04\xaa\x8e2\xeeJ\x00\x00\x00\x07\x00\x00\x00\x19\x00'
                    b' \x00\x00\x00<\xe04\xec\xc9')))
