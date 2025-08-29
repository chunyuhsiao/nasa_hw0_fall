import base64
from Cryptodome.Util.number import *
cipher = r"TGrWiRVLkgERlb11jN3lhwhBrCSwR5gbS/YMs0WzinxXrV9AG4ieZwf/NpEn3wEn57h+gmL5ckJmdhxryGzX8A=="
N = 11886078828575428410020184764338155811658327177871252212581222928669891297689718738754964192534523861584253899371187963332753196380561253587057164370681391
d = 3251501003077655073238657131926308152515533052243401584862843350553028231151523084809142358650966102613814652594272729839958098853130285914704018410410881
byt = base64.b64decode(cipher)
enc_m = bytes_to_long(byt)
def fast_power(a, n, mod):
    a %= mod
    result = 1
    while n > 0:
        if n & 1:
            result = result * a % mod
        a = a * a % mod
        n >>= 1 
    return result
outfile = open('output.txt', 'w')
dec_m = fast_power(enc_m, d, N)
message = long_to_bytes(dec_m).decode()
outfile.write('hey message is ' + message)
outfile.close()