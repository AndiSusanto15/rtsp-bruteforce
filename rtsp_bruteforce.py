import requests
import subprocess
import tempfile
import os
import sys

# Argument input
if len(sys.argv) != 4:
    print(f"Usage: python3 {sys.argv[0]} <ip> <username> <password>")
    sys.exit(1)

ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

# URL list RTSP path dari GitHub
url_list = "https://raw.githubusercontent.com/nmap/nmap/master/nselib/data/rtsp-urls.txt"

print("[*] Mengunduh daftar RTSP URL...")
resp = requests.get(url_list)
if resp.status_code != 200:
    print("Gagal mengunduh daftar URL.")
    sys.exit(1)

paths = resp.text.splitlines()
found = None

print(f"[*] Mulai brute force RTSP ke {ip} dengan user '{username}'...")

for path in paths:
    path = path.strip()
    if not path or path.startswith("#"):
        continue

    # Ganti placeholder
    rtsp_path = path.replace("{{ip}}", ip)\
                    .replace("{{username}}", username)\
                    .replace("{{password}}", password)
    full_url = f"rtsp://{username}:{password}@{ip}{rtsp_path}"

    print(f"[+] Mencoba: {full_url}")

    try:
        # Jalankan ffmpeg dengan timeout 5 detik
        result = subprocess.run(
            ["ffmpeg", "-stimeout", "5000000", "-i", full_url, "-t", "1", "-f", "null", "-"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=7
        )

        if result.returncode == 0:
            print(f"[✓] BERHASIL: {full_url}")
            found = full_url
            with open("found_rtsp.txt", "w") as f:
                f.write(found + "\n")
            break
    except subprocess.TimeoutExpired:
        print("[-] Timeout")
    except Exception as e:
        print(f"[-] Error: {e}")

print("[*] Selesai.")
if found:
    print(f"[✓] URL ditemukan: {found}")
else:
    print("[!] Tidak ada URL yang cocok.")

