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
This makes it easier to inspect specific types of network traffic.

📁 CSV Logging

Analyzed packet information is stored in:

packet_results.csv

This allows the captured information to be reviewed and analyzed later.

🖥️ Interactive Dashboard

The application provides a graphical interface containing:

Packet capture controls
Capture status
Packet statistics
Protocol filter
Packet information table
Clear functionality
⚙️ How It Works

The application follows a simple packet-analysis process:

Network Traffic
       ↓
Packet Capture
       ↓
Packet Inspection
       ↓
Protocol Identification
       ↓
Information Extraction
       ↓
Real-Time Dashboard
       ↓
CSV Logging
1️⃣ Packet Capture

The application uses Scapy to capture packets from the available network interface.

2️⃣ Packet Inspection

Each captured packet is inspected to determine whether it contains relevant network information.

3️⃣ Protocol Identification

The application checks the packet structure and identifies supported protocols such as TCP, UDP, and ICMP.

4️⃣ Information Extraction

Important information is extracted from the packet:

Source IP
Destination IP
Protocol
Source Port
Destination Port
Packet Size
Payload Size
Timestamp
5️⃣ Real-Time Display

The extracted information is displayed in the graphical dashboard as packets are captured.

6️⃣ Statistics Update

Packet counters are updated based on the identified protocol.

For example:

Total Packets: 25
TCP: 15
UDP: 7
ICMP: 3
7️⃣ CSV Storage

The analyzed packet information is saved into a CSV file for later examination.

📊 Example Packet Analysis

A captured packet may contain information similar to:

Packet Number : 1
Time          : 15:20:01
Source IP     : 192.168.1.5
Destination IP: 8.8.8.8
Protocol      : UDP
Source Port   : 53000
Destination Port: 53
Packet Size   : 74 bytes
Payload Size  : 32 bytes

The actual values depend on the network traffic captured by the system.

🛠️ Technologies Used
Technology	Purpose
Python 3	Core programming language
Scapy	Network packet capture and analysis
Tkinter	Graphical user interface
CSV	Structured packet-data storage
Threading	Background packet processing
Datetime	Timestamp generation
📂 Project Structure
network-packet-analyzer/
│
├── packet_analyzer.py
├── packet_results.csv
└── README.md
File Description
File	Description
packet_analyzer.py	Main application for packet capture, analysis, filtering, statistics, and GUI
packet_results.csv	Stores analyzed packet information
README.md	Project documentation
🚀 Installation
Prerequisites

Before running the project, make sure you have:

Python 3.x
Scapy
Npcap on Windows
Appropriate permissions for packet capture
Install Scapy

Open PowerShell and run:

py -m pip install scapy
▶️ Running the Application

Navigate to the project directory:

cd "path-to-network-packet-analyzer"

Run the application:

py packet_analyzer.py

The Network Packet Analyzer dashboard will open.

Use the application's capture controls to start and stop packet monitoring.

🔎 Protocol Filtering

The application supports protocol-based filtering.

ALL

Displays all supported packets.

TCP

Displays TCP packets.

UDP

Displays UDP packets.

ICMP

Displays ICMP packets.

This filtering capability helps users focus on specific network communication types.

📁 CSV Output

The application stores analyzed packet information in:

packet_results.csv

The file contains information such as:

Packet Number
Time
Source IP
Destination IP
Protocol
Source Port
Destination Port
Packet Size
Payload Size

The CSV file can be opened using spreadsheet software or analyzed programmatically using Python.

🔐 Cybersecurity Relevance

Network packet analysis is an important concept in cybersecurity and network monitoring.

Analyzing network traffic can help security professionals understand:

Which systems are communicating
Which protocols are being used
Which ports are involved
How much traffic is being generated
Basic communication patterns
Potentially unusual network activity

This project provides a simplified practical introduction to these concepts.

⚠️ Limitations

This project is designed as an educational packet-analysis tool and is not intended to replace professional network monitoring or intrusion-detection solutions.

Current limitations include:

Limited protocol coverage
Basic packet inspection
No advanced threat detection
No deep packet inspection
No automated intrusion detection
No machine-learning-based classification
No analysis of encrypted packet contents
Capture capabilities depend on the available network interface and system configuration
🔮 Future Improvements

The project can be further improved by adding:

📈 Real-time traffic graphs
🚨 Suspicious traffic detection
🛡️ Basic anomaly detection
🔎 Advanced packet filtering
📊 Protocol distribution charts
🌐 Network interface selection
📁 PCAP file import and analysis
🤖 Machine-learning-based traffic classification
📋 Automated security reports
🔔 Alerts for suspicious traffic patterns
🔍 Packet search functionality
📚 Learning Outcomes

Through this project, I gained practical experience in:

Network packet analysis
Python programming
Scapy
TCP/IP concepts
Protocol identification
IP address analysis
Port analysis
Packet structure
CSV data processing
Tkinter GUI development
Multithreading
Real-time data processing
Basic network-security monitoring
🔒 Ethical & Responsible Use

This project is intended for educational purposes and authorized network analysis only.

Network packet capture can expose sensitive information. Therefore, the tool should only be used on systems and networks where appropriate permission has been obtained.

Do not use this project to intercept, monitor, or analyze network traffic belonging to other users or networks without authorization.
