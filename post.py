import json, fb, requests
from facepy import GraphAPI

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def post():
    print warna.hijau+"Input Token"
    token = raw_input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"ID Target"
    target = input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Jumlah"
    jmlh = input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Text"
    msg = raw_input(warna.oren+"---> "+warna.biru).replace('<space>', '\n')
    i = 0
    for i in range(0, jmlh):
        count = jmlh + 1
        voss = 'https://graph.facebook.com/%s/feed?message=%s&access_token=%s'%(target, msg, token)
        prm = {'access_token' : token, 'message' : msg}
        gg = requests.post(voss, data = prm)
        try:
            print warna.hijau+"Berhasil"
        except KeyError:
            print warna.merah+"Gagal"
##########################
post()
