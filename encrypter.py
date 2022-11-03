import methods
import key


def encrypt(s: str, met: key.KeyIndicator):
    result = ""
    rev_res = ""
    if met.method == methods.i1d1:
        for i in s:
            result += chr(ord(i) + 1)
    if met.method == methods.i1d1pr:
        for i in s:
            result += chr(ord(i) + 1)
        for i in range(len(result) - 1, 0):
            rev_res += result[i]
    if met.method == methods.i1d1:
        return result
    if met.method == methods.i1d1pr:
        return rev_res
