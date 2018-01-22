from ctypes import c_char_p

CONVERT_TABLE = [];
for i in range(64):
    CONVERT_TABLE.append((chr(ord('a') + (i % 8)) + chr(ord('1') + int(i / 8))));
CONVERT_TABLE.append("pa");
CONVERT_TABLE.append("--");


def moveToString(x):
    """
    Convert move coordinate to string.
    
    :param int x: move coordinate(0-63,64,65)
    :return: move string(a1-h8,pa,--)
    """
    if (x >= 0 and x <= 65):
        return CONVERT_TABLE[x];
    else:
        return "??";


def to_cstr_array(array):
    """
    convert python array to c_char_p array.
    
    :param array array: array of string.
    :return: c_char_p array.
    """
    ret = (c_char_p * len(array))();
    for i, val in enumerate(array):
        ret[i] = val.encode();
    return ret;


def create_buffer(len):
    """
    Create String buffer for out parameter.
    
    :param int len: length of buffer.
    :return: String of length len.
    """
    return (" " * len).encode();

