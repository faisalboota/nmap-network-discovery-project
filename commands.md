
# Nmap Commands Documentation

## 1. Ping Scan

### Command

```bash
nmap -sn 192.168.1.0/24
```

### Purpose

Discover all active devices on the network.

---

## 2. Service Version Detection

### Command

```bash
nmap -sV 192.168.1.10
```

### Purpose

Identify running services and their versions.

---

## 3. Operating System Detection

### Command

```bash
sudo nmap -O 192.168.1.10
```

### Purpose

Detect the target operating system.

---

## 4. Aggressive Scan

### Command

```bash
sudo nmap -A 192.168.1.10
```

### Purpose

Perform OS detection, version detection, script scanning, and traceroute.