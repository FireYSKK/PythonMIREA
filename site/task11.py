import struct


def main(data):
    format_a = '<3bH2IfBq7H'
    format_b = '<2I4c'
    format_c = '<qBl'
    format_d = 'bQHLHl2B'

    struct_a = struct.unpack_from(format_a, data)
    struct_b = struct.unpack_from(format_b + format_d, data, struct_a[3])

    address_c = struct.unpack_from(f'<{struct_b[0]}H', data, struct_b[1])
    list_c = []
    for i in address_c:
        struct_c = struct.unpack_from(format_c, data, offset=i)
        new_c_dict = {'C1': struct_c[0],
                      'C2': struct_c[1],
                      'C3': struct_c[2]}
        list_c.append(new_c_dict)

    b2line = ""
    for i in range(2, 6):
        b2line += struct_b[i].decode("utf-8")

    return {'A1': {'B1': list_c,
                   'B2': b2line,
                   'B3': {'D1': struct_b[6],
                          'D2': struct_b[7],
                          'D3': struct_b[8],
                          'D4': struct_b[9],
                          'D5': struct_b[10],
                          'D6': struct_b[11],
                          'D7': list(struct_b[12:])}
                   },
            'A2': list(struct.unpack_from(f'<{struct_a[4]}q',
                                          data,
                                          offset=struct_a[5])),
            'A3': struct_a[6],
            'A4': struct_a[7],
            'A5': struct_a[8],
            'A6': list(struct_a[9:])}
