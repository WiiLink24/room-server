import io
import struct

RawMin = 0
FileMagic = 0x11
CompressedMin = 0x00000004
CompressedMax = 0x01400000
RawMax = 0x00FFFFFF

DefaultMask = 0x80
BitShiftCount = 1
MaxNotEncode = 2
MaxOffset = 0x1000
MaxCoded1 = 0x10
MaxCoded2 = 0x110
MaxCoded3 = 0x10110
VRAMCompatible = 1


def encode(data: bytes) -> bytes | None:
    if len(data) <= RawMin:
        return None

    if len(data) > RawMax:
        return None

    out = bytearray()
    header = struct.pack("<I", 0x11 | (len(data) << 8))
    out.extend(header)

    mask = 0
    flag = 0
    index = 0
    _len = 0
    pos = 0
    len_best = 0
    pos_best = 0
    comp_pos = 4

    while index < len(data):
        mask >>= BitShiftCount
        if mask == 0:
            out.extend([0])

            flag = comp_pos
            comp_pos += 1
            mask = DefaultMask

        len_best = MaxNotEncode

        if index >= MaxOffset:
            pos = MaxOffset
        else:
            pos = index

        while pos > VRAMCompatible:
            for _len in range(MaxCoded3):
                if index + _len == len(data):
                    break

                if index + _len >= len(data):
                    break

                if data[index + _len] != data[index + _len - pos]:
                    break

            if _len > len_best:
                pos_best = pos
                len_best = _len

                if len_best == MaxCoded3:
                    break

            pos -= 1

        if len_best > MaxNotEncode:
            index += len_best
            out[flag] |= mask & 0xFF

            if len_best > MaxCoded2:
                len_best -= MaxCoded2 + 1
                cmp = [
                    ((len_best >> 12) | 16) & 0xFF,
                    ((len_best >> 4) & 0xFF),
                    (((len_best & 15) << 4) | (pos_best - 1) >> 8) & 0xFF,
                    ((pos_best - 1) & 0xFF),
                ]

                out.extend(cmp)
                comp_pos += 4
            elif len_best > MaxCoded1:
                len_best -= MaxCoded1 + 1

                cmp = [
                    (len_best >> 4) & 0xFF,
                    (((len_best & 15) << 4) | (pos_best - 1) >> 8) & 0xFF,
                    ((pos_best - 1) & 0xFF),
                ]

                out.extend(cmp)
                comp_pos += 3
            else:
                len_best -= 1
                cmp = [
                    (((len_best & 15) << 4) | (pos_best - 1) >> 8) & 0xFF,
                    ((pos_best - 1) & 0xFF),
                ]

                out.extend(cmp)
                comp_pos += 2
        else:
            out.extend([data[index]])
            comp_pos += 1
            index += 1

    return bytes(out)
