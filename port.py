import socket


def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Setzen Sie einen Timeout für die Verbindung
        sock.connect((host, port))
        print(f"Port {port} auf {host} ist erreichbar")
    except socket.error:
        print(f"Port {port} auf {host} ist nicht erreichbar")
    finally:
        sock.close()


def main():
    host = input("Geben Sie die IP-Adresse oder den Hostnamen ein: ")
    ports = input(
        "Geben Sie die zu überprüfenden Ports (durch Leerzeichen getrennt) ein: ")
    port_list = [int(port) for port in ports.split()]

    for port in port_list:
        check_port(host, port)


if __name__ == "__main__":
    main()
