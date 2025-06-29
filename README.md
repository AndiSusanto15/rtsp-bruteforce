# RTSP Bruteforce

Jadi saya baru beli CCTV [Eyesec ES07](https://s.shopee.co.id/5fdMkkdpYI).
Dan mau pantau via RTSP pake aplikasi [CCTV Viewer](https://github.com/iEvgeny/cctv-viewer),
semalaman cari di forum tidak ketemu. Terus tanya chatGPT minta buatkan script untuk bruteforce nya.
Dan inilah dia.

## how to use

```
Clone repo

git clone https://github.com/AndiSusanto15/rtsp-bruteforce.git

cd rtsp-brutefoce

./rtsp_bruteforce.sh <IP>:<PORT> <USERNAME> <PASSWORD> # Menggunakan shell script

python3 rtsp_bruteforce.py <IP>:<PORT> <USERNAME> <PASSWORD> # Menggunakan shell python3

e.g
./rtsp_bruteforce.sh 192.168.100.40:8554 admin P4ssw0rd

python3 rtsp_bruteforce.py 192.168.100.40:8554 admin P4ssw0rd
```

RTSP ini juga bisa digunakan untuk menghubungkan ke NVR.