import socket
import threading

# Escaneo de un puerto específico de una IP
def scan_port(ip, port):
    try:
        # Creamos un socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establecemos un tiempo de espera
        sock.settimeout(1)
        # Intentamos conectarnos al puerto
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Puerto {port} en {ip} está ABIERTO.")
        else:
            print(f"Puerto {port} en {ip} está CERRADO.")
        sock.close()
    except socket.error:
        print(f"No se pudo conectar a la IP {ip}")
    except Exception as e:
        print(f"Error: {e}")

# Escaneo de un rango de puertos en una IP
def scan_ip(ip, start_port, end_port):
    print(f"\nEscaneando IP {ip} desde el puerto {start_port} hasta el {end_port}:")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

# Escanear una red de IPs locales
def scan_network(base_ip, start_range, end_range, start_port, end_port):
    for i in range(start_range, end_range + 1):
        ip = f"{base_ip}.{i}"
        thread = threading.Thread(target=scan_ip, args=(ip, start_port, end_port))
        thread.start()

if __name__ == "__main__":
    # Modifica esto a la red que quieras escanear
    base_ip = "192.168.1"  # Parte de la IP común en la red local
    start_ip_range = 1
    end_ip_range = 5
    start_port = 20  # Puerto inicial a escanear
    end_port = 95    # Puerto final a escanear

    scan_network(base_ip, start_ip_range, end_ip_range, start_port, end_port)
