# device_card.py 
# stores and displays device record information
MAX_CONNECTIONS = 100
device_name = "Mazen_PC"
device_ip = "192.0.2.1"
service = "HTTPS"
open_port = 22

print ("Device:",device_name)
print ("IP address:",device_ip)
print ("Service:",service)
print ("Port:",open_port)
print ("Max connections:",MAX_CONNECTIONS)
service = "SSH"
open_port = 24

print ("Updated service:",service ,"on port",open_port)
