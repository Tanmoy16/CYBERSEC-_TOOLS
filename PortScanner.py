
import subprocess
import socket

def run_scan(target, options, report_name):
    print(f"\n[+] Running scan on {target} with options: {options}")
    result = subprocess.getoutput(f"nmap {options} {target}")
    with open(report_name, "a") as f:
        f.write("\n" + "="*60 + "\n")
        f.write(f"Scan Type: {options}\n")
        f.write(result + "\n")
    print(f"[+] Scan complete. Results saved in {report_name}\n")


def custom_port_scan(target, start_port, end_port, report_name):
    print(f"\n[+] Starting custom port scan on {target} ({start_port}-{end_port})")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass
    
    with open(report_name, "a") as f:
        f.write("\n" + "="*60 + "\n")
        f.write(f"Custom Port Scan ({start_port}-{end_port})\n")
        if open_ports:
            f.write("Open Ports: " + ", ".join(map(str, open_ports)) + "\n")
        else:
            f.write("No open ports found in this range.\n")
    print(f"[+] Custom port scan complete. Results saved in {report_name}\n")


def main():
    print("==== Advanced Port Scanner ====")
    target = input("Enter Target IP/Domain: ")
    report_name = input("Enter report filename (e.g., report.txt): ")

    while True:
        print("\nChoose Scan Type:")
        print("1. TCP Connect Scan (-sT)")
        print("2. SYN Scan (-sS)")
        print("3. UDP Scan (-sU)")
        print("4. Service Version Detection (-sV)")
        print("5. OS Detection (-O)")
        print("6. Aggressive Scan (-A)")
        print("7. Vulnerability Scan (--script=vuln)")
        print("8. Custom Port Scan (Python)")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            run_scan(target, "-sT", report_name)
        elif choice == "2":
            run_scan(target, "-sS", report_name)
        elif choice == "3":
            run_scan(target, "-sU", report_name)
        elif choice == "4":
            run_scan(target, "-sV", report_name)
        elif choice == "5":
            run_scan(target, "-O", report_name)
        elif choice == "6":
            run_scan(target, "-A", report_name)
        elif choice == "7":
            run_scan(target, "--script=vuln", report_name)
        elif choice == "8":
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            custom_port_scan(target, start_port, end_port, report_name)
        elif choice == "9":
            print("[+] Exiting. All results saved in", report_name)
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

