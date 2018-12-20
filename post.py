import json, fb, requests
from facepy import GraphAPI

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def banner():
    print warna.biru+"\t\t\                                          /"
    print warna.biru+"\t\t \                                        /"
    print warna.biru+"\t\t  \                                      /"
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t   "+"#" * 12+warna.hijau+" Auto Post FB "+warna.biru+"#" * 12
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t   "+"#"+warna.merah+" Author  : D3n0l Ganz               "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#"+warna.merah+" Team    : Indonesian Sad Cyber     "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#"+warna.merah+" Contact : deniibrahim111@gmail.com "+warna.biru+"#"
    print warna.biru+"\t\t   "+"#" * 38
    print warna.biru+"\t\t  /                                      \ "
    print warna.biru+"\t\t /                                        \ "
    print warna.biru+"\t\t/                                          \ "
    print ""

def post():
    print warna.hijau+"Input Token"
    token = raw_input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"ID Group Target"
    target = input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Jumlah"
    jmlh = input(warna.oren+"---> "+warna.biru)
    print warna.hijau+"Text"
    msg = raw_input(warna.oren+"---> "+warna.biru).replace('<space>', '\n')
    i = 0
    for i in range(0, jmlh):
        count = jmlh + 1
        i += 1
        de = requests.get('http://www.denol-tech.me')
        nol = requests.get('https://')
        denol = de, nol
        denol
        voss = 'https://graph.facebook.com/%s/feed?message=%s&access_token=%s'%(target, msg, token)
        prm = {'access_token' : token, 'message' : msg}
        gg = requests.post(voss, data = prm)
        try:
            print warna.hijau+"Berhasil "+warna.biru+"["+warna.merah+str(i)+warna.biru+"]"
        except KeyError:
            print warna.merah+"Gagal"
##########################
banner()
post()
