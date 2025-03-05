import os
import socket
import subprocess
import json

def get_ip_addresses():
    """Get local and external IP addresses."""
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        external_ip = subprocess.getoutput("curl -s ifconfig.me")
        return {"local_ip": local_ip, "external_ip": external_ip}
    except Exception as e:
        return {"error": str(e)}

def scan_network():
    """Scan the local network for connected devices."""
    try:
        result = subprocess.getoutput("arp -a")
        return {"network_scan": result}
    except Exception as e:
        return {"error": str(e)}

def log_network_data():
    """Logs network data and integrates it with AI learning models."""
    network_data = {
        "IP_Info": get_ip_addresses(),
        "Devices": scan_network()
    }
    
    with open("network_log.json", "w") as f:
        json.dump(network_data, f, indent=4)

    return "✅ Network data logged successfully."

if __name__ == "__main__":
    print(log_network_data())
