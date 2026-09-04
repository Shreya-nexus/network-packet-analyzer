# 🌐 Network Packet Analyzer

A Python-based cybersecurity tool designed to capture, analyze, and monitor network packets in real time. The application provides an interactive dashboard for viewing packet information, identifying network protocols, monitoring traffic statistics, and storing analyzed data for further examination.

## 📌 Overview

Network communication consists of packets that carry information between devices. Understanding these packets is an important part of network security and monitoring.

This project provides a simple and practical way to observe network traffic and understand the basic information contained within network packets.

The application uses **Scapy** for packet capture and analysis and **Tkinter** to provide a user-friendly graphical interface.

## 🎯 Objectives

The main objectives of this project are:

- Capture network packets in real time
- Analyze basic packet information
- Identify commonly used protocols
- Display source and destination IP addresses
- Identify source and destination ports
- Monitor packet and payload sizes
- Provide real-time packet statistics
- Filter packets based on protocol
- Store analyzed packet information in CSV format
- Provide a simple cybersecurity monitoring interface

## ✨ Features

### 📡 Real-Time Packet Capture
Captures network packets from the available network interface using Scapy.

### 🔍 Packet Analysis
Extracts useful information from captured packets, including:

- Source IP address
- Destination IP address
- Protocol
- Source port
- Destination port
- Packet size
- Payload size
- Timestamp

### 🌐 Protocol Identification
The analyzer identifies common network protocols such as:

- TCP
- UDP
- ICMP

### 📊 Real-Time Statistics
The dashboard displays packet statistics, including:

- Total packets
- TCP packets
- UDP packets
- ICMP packets

### 🔎 Protocol Filtering
Captured packets can be filtered by protocol:

```text
ALL
TCP
UDP
ICMP
