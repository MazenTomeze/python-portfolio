#port_report.py
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

for port in range(start_port, end_port + 1):
    if 0 <= port <= 1023:
        print(f"{port}: system")
    elif 1024 <= port <= 49151:
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")
number_of_ports = end_port - start_port + 1
print(f"Ports checked: {number_of_ports}")