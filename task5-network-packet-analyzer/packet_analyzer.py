import tkinter as tk
from tkinter import ttk
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import threading

CSV_FILE = "packet_results.csv"

packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

capturing = False


def create_csv():

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Packet Number",
            "Time",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size",
            "Payload Size"
        ])


def analyze_packet(packet):

    global packet_count
    global tcp_count
    global udp_count
    global icmp_count

    if not capturing:
        return

    if IP not in packet:
        return

    # Identify protocol
    if TCP in packet:

        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

        tcp_count += 1

    elif UDP in packet:

        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

        udp_count += 1

    elif ICMP in packet:

        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

        icmp_count += 1

    else:

        protocol = "Other"
        source_port = "-"
        destination_port = "-"

    # Packet number
    packet_count += 1

    # Packet information
    source = packet[IP].src
    destination = packet[IP].dst

    packet_size = len(packet)
    payload_size = len(packet.payload)

    current_time = datetime.now().strftime("%H:%M:%S")

    # Print in PowerShell
    print("--------------------------------")
    print("Packet Number   :", packet_count)
    print("Time            :", current_time)
    print("Source IP       :", source)
    print("Destination IP  :", destination)
    print("Protocol        :", protocol)
    print("Source Port     :", source_port)
    print("Destination Port:", destination_port)
    print("Packet Size     :", packet_size)
    print("Payload Size    :", payload_size)

    # Save to CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            packet_count,
            current_time,
            source,
            destination,
            protocol,
            source_port,
            destination_port,
            packet_size,
            payload_size
        ])

    # Update GUI
    root.after(
        0,
        update_dashboard,
        packet_count,
        tcp_count,
        udp_count,
        icmp_count,
        current_time,
        source,
        destination,
        protocol,
        source_port,
        destination_port,
        packet_size,
        payload_size
    )


def update_dashboard(
    total,
    tcp,
    udp,
    icmp,
    time,
    source,
    destination,
    protocol,
    source_port,
    destination_port,
    packet_size,
    payload_size
):

    # Update statistics

    total_label.config(
        text=f"TOTAL\n{total}"
    )

    tcp_label.config(
        text=f"TCP\n{tcp}"
    )

    udp_label.config(
        text=f"UDP\n{udp}"
    )

    icmp_label.config(
        text=f"ICMP\n{icmp}"
    )

    # Packet information

    packet_table.insert(
    "",
    "end",
    values=(
        total,
        time,
        source,
        destination,
        protocol,
        packet_size
    )
)

def start_capture():

    global capturing

    if capturing:
        return

    capturing = True

    status_label.config(
        text="● CAPTURING",
        fg="green"
    )

    start_button.config(
        state="disabled"
    )

    stop_button.config(
        state="normal"
    )

    thread = threading.Thread(
        target=capture_packets,
        daemon=True
    )

    thread.start()


def capture_packets():

    sniff(
        prn=analyze_packet,
        store=False
    )


def stop_capture():

    global capturing

    capturing = False

    status_label.config(
        text="● STOPPED",
        fg="red"
    )

    start_button.config(
        state="normal"
    )

    stop_button.config(
        state="disabled"
    )


def clear_output():

    global packet_count
    global tcp_count
    global udp_count
    global icmp_count

    packet_table.delete(
        *packet_table.get_children()
    )

    packet_count = 0
    tcp_count = 0
    udp_count = 0
    icmp_count = 0

    total_label.config(
        text="TOTAL\n0"
    )

    tcp_label.config(
        text="TCP\n0"
    )

    udp_label.config(
        text="UDP\n0"
    )

    icmp_label.config(
        text="ICMP\n0"
    )


def exit_program():

    global capturing

    capturing = False

    root.destroy()


# ==========================================
# CREATE CSV
# ==========================================

create_csv()


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title(
    "Network Packet Analyzer"
)

root.geometry(
    "1000x750"
)

root.configure(
    bg="#0b1020"
)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="🌐 NETWORK PACKET ANALYZER",
    font=("Arial", 25, "bold"),
    bg="#0b1020",
    fg="white"
)

title.pack(
    pady=(25, 3)
)


subtitle = tk.Label(
    root,
    text="Real-Time Network Traffic Monitoring",
    font=("Arial", 11),
    bg="#0b1020",
    fg="#9ca3af"
)

subtitle.pack(
    pady=(0, 10)
)


# ==========================================
# STATUS
# ==========================================

status_label = tk.Label(
    root,
    text="● STOPPED",
    font=("Arial", 11, "bold"),
    bg="#0b1020",
    fg="red"
)

status_label.pack(
    pady=5
)


# ==========================================
# STATISTICS
# ==========================================

stats_frame = tk.Frame(
    root,
    bg="#0b1020"
)

stats_frame.pack(
    pady=15
)


total_label = tk.Label(
    stats_frame,
    text="TOTAL\n0",
    font=("Arial", 15, "bold"),
    bg="#171d31",
    fg="white",
    width=15,
    height=3
)

total_label.grid(
    row=0,
    column=0,
    padx=6
)


tcp_label = tk.Label(
    stats_frame,
    text="TCP\n0",
    font=("Arial", 15, "bold"),
    bg="#171d31",
    fg="white",
    width=15,
    height=3
)

tcp_label.grid(
    row=0,
    column=1,
    padx=6
)


udp_label = tk.Label(
    stats_frame,
    text="UDP\n0",
    font=("Arial", 15, "bold"),
    bg="#171d31",
    fg="white",
    width=15,
    height=3
)

udp_label.grid(
    row=0,
    column=2,
    padx=6
)


icmp_label = tk.Label(
    stats_frame,
    text="ICMP\n0",
    font=("Arial", 15, "bold"),
    bg="#171d31",
    fg="white",
    width=15,
    height=3
)

icmp_label.grid(
    row=0,
    column=3,
    padx=6
)
# ==========================================
# PROTOCOL FILTER
# ==========================================

filter_frame = tk.Frame(
    root,
    bg="#0b1020"
)

filter_frame.pack(
    pady=5
)

filter_label = tk.Label(
    filter_frame,
    text="Protocol Filter:",
    font=("Arial", 11, "bold"),
    bg="#0b1020",
    fg="white"
)

filter_label.pack(
    side="left",
    padx=10
)


protocol_var = tk.StringVar(
    value="ALL"
)


protocol_menu = tk.OptionMenu(
    filter_frame,
    protocol_var,
    "ALL",
    "TCP",
    "UDP",
    "ICMP"
)

protocol_menu.config(
    font=("Arial", 10),
    width=10
)

protocol_menu.pack(
    side="left"
)


# ==========================================
# OUTPUT
# ==========================================

# ==========================================
# PACKET TABLE
# ==========================================

table_frame = tk.Frame(
    root,
    bg="#0b1020"
)

table_frame.pack(
    padx=30,
    pady=15,
    fill="both",
    expand=True
)


columns = (
    "number",
    "time",
    "source",
    "destination",
    "protocol",
    "size"
)


packet_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)


packet_table.heading(
    "number",
    text="#"
)

packet_table.heading(
    "time",
    text="Time"
)

packet_table.heading(
    "source",
    text="Source IP"
)

packet_table.heading(
    "destination",
    text="Destination IP"
)

packet_table.heading(
    "protocol",
    text="Protocol"
)

packet_table.heading(
    "size",
    text="Size"
)


packet_table.column(
    "number",
    width=60
)

packet_table.column(
    "time",
    width=90
)

packet_table.column(
    "source",
    width=150
)

packet_table.column(
    "destination",
    width=150
)

packet_table.column(
    "protocol",
    width=90
)

packet_table.column(
    "size",
    width=90
)


scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=packet_table.yview
)

packet_table.configure(
    yscrollcommand=scrollbar.set
)


packet_table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

packet_table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(
    root,
    bg="#0b1020"
)

button_frame.pack(
    pady=20
)


start_button = tk.Button(
    button_frame,
    text="▶ START CAPTURE",
    command=start_capture,
    font=("Arial", 11, "bold"),
    padx=25,
    pady=10,
    bg="#536dfe",
    fg="white",
    relief="flat"
)

start_button.grid(
    row=0,
    column=0,
    padx=8
)


stop_button = tk.Button(
    button_frame,
    text="■ STOP",
    command=stop_capture,
    font=("Arial", 11, "bold"),
    padx=25,
    pady=10,
    bg="#29334d",
    fg="white",
    relief="flat",
    state="disabled"
)

stop_button.grid(
    row=0,
    column=1,
    padx=8
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_output,
    font=("Arial", 11, "bold"),
    padx=25,
    pady=10,
    bg="#29334d",
    fg="white",
    relief="flat"
)

clear_button.grid(
    row=0,
    column=2,
    padx=8
)


# ==========================================
# CLOSE
# ==========================================

root.protocol(
    "WM_DELETE_WINDOW",
    exit_program
)


# ==========================================
# START GUI
# ==========================================

root.mainloop()