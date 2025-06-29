#!/bin/bash

# Input
IP="$1"
USER="$2"
PASS="$3"

# Cek input
if [[ -z "$IP" || -z "$USER" || -z "$PASS" ]]; then
    echo "Usage: $0 <ip> <username> <password>"
    exit 1
fi

# URL sumber
RTSP_LIST_URL="https://raw.githubusercontent.com/nmap/nmap/master/nselib/data/rtsp-urls.txt"

# Unduh daftar URL
TMP_FILE=$(mktemp)
curl -s "$RTSP_LIST_URL" > "$TMP_FILE"

echo "[*] Mulai brute force RTSP URLs ke $IP ..."

# Loop dan coba satu per satu
while read -r path; do
    # Skip baris kosong atau komentar
    [[ -z "$path" || "$path" =~ ^# ]] && continue

    # Ganti token
    FULL_URL="rtsp://$USER:$PASS@$IP${path//\{\{username\}\}/$USER}"
    FULL_URL="${FULL_URL//\{\{password\}\}/$PASS}"
    FULL_URL="${FULL_URL//\{\{ip\}\}/$IP}"

    echo "[+] Mencoba: $FULL_URL"

    # Coba dengan ffmpeg (timeout 5 detik)
    ffmpeg -stimeout 5000000 -i "$FULL_URL" -t 1 -f null - 2>/dev/null

    if [[ $? -eq 0 ]]; then
        echo "[✓] BERHASIL: $FULL_URL"
        echo "$FULL_URL" >> found_rtsp.txt
        break
    fi
done < "$TMP_FILE"

# Cleanup
rm -f "$TMP_FILE"
echo "[*] Selesai."

