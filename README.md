# 🌐 Network Packet Analyzer

> A Python-based network monitoring and packet analysis tool designed to capture, inspect, filter, and visualize network traffic in real time.

---

## 📌 Overview

The **Network Packet Analyzer** is an educational cybersecurity project developed using Python and Scapy.

The application captures network packets from the local system and extracts useful information such as source and destination IP addresses, communication protocols, port numbers, packet size, payload size, and timestamps.

A graphical dashboard provides real-time packet statistics and makes the captured traffic easier to understand.

The project was developed as part of **Task 5 of the Prodigy Infotech Cyber Security Internship**.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Understand how network packets are captured
- Analyze basic network traffic information
- Identify commonly used network protocols
- Extract IP addresses and port information
- Monitor packet sizes and payload sizes
- Store packet information in CSV format
- Provide protocol-based filtering
- Display network statistics in real time
- Build a simple cybersecurity monitoring interface

---

## ✨ Key Features

### 📡 Live Packet Capture

Captures network packets from the local system using Scapy.

### 🔍 Packet Analysis

Extracts important packet information including:

- Source IP
- Destination IP
- Protocol
- Source port
- Destination port
- Packet size
- Payload size
- Timestamp

### 🌐 Protocol Identification

The analyzer identifies common protocols such as:

- TCP
- UDP
- ICMP

### 📊 Real-Time Statistics

The dashboard displays:

- Total packets
- TCP packets
- UDP packets
- ICMP packets

### 🔎 Protocol Filtering

Packets can be filtered by protocol:

```text
ALL
TCP
UDP
ICMP
