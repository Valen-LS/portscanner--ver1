#Socket funciona como interfas para Berkeley socket IP 
import socket
#Se importara ipaddress para comprobar que sea valida la ip
import ipaddress
#Esto solo funciona para regular las expressiones asi parea asegurarnos que lo puesto este formado correctamente
import re

port_range_p = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

print(r"""
 __| |________________________________________________________________| |__
__   ________________________________________________________________   __
  | |                                                                | |  
  | |                        _                                       | |  
  | |                       | |                                      | |  
  | |__   ___ __   ___  _ __| |_ ___  ___ __ _ _ __  _ __   ___ _ __ | |  
  | |\ \ / / '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|| |  
  | | \ V /| |_) | (_) | |  | |_\__ \ (_| (_| | | | | | | |  __/ |   | |  
  | |  \_/ | .__/ \___/|_|   \__|___/\___\__,_|_| |_|_| |_|\___|_|   | |  
  | |      | |                                                       | |  
  | |      |_|                                                       | |  
__| |________________________________________________________________| |__
__   ________________________________________________________________   __
  | |                                                                | |  """)
print("\n****************************************************************")
print("\n* Made by Valen")
print("\n* https://github.com/Valen-LS")
print("\n****************************************************************")

open_ports = []
#Preguntar al usuario la ip que quiera escanear
while True:
    ip_add_ent = input("\n Please enter the ip address that you want to scan: ")
    #esto hara que si introducimos una ip invalida repita la pregunta
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_ent)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalida ip address")
    
while True:
    #puedes escanear 0-65535 puertos. Pero este scanner es basico por lo que no tiene multitrheading
    # por lo que scannear todos los puertos no es recomendado...
    print("Please enter the range of ports you want to scan in format: 80-120 <inicialport>-<finalport>")
    port_range = input("Enter port range: ")
    #esto funciona para que cuando pongas un valor agregando espacios que el programa continue por ejemplo en vez de
    # ser 80-100 siga funcionando con 80 - 100 ambas serian correctas para el programa
    port_range_valid = port_range_p.search(port_range.replace(" ",""))
    if port_range_valid:
        #aqui extraemos el iniciop del rango que el usuario quiere escanear
        port_min = int(port_range_valid.group(1))
        #aqui extraemos finalp del rango que el usuario quiere escanear
        port_max = int(port_range_valid.group(2))
        break
# socket port scanning ( basico ;c )
for port in range(port_min, port_max + 1):
    #aca el socket conecta al objetivo. por lo que necesitamos la ip y el puerto que queremos conectar
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         #esto hara que cada 0.5s cada puerto le de ese tiempo para escanear
         #mientras mas tiempo puede soltar resultados mejores
         s.settimeout(0.5)
         # en esto si el puerto no logra conectarse a este socket causara una exception y la lista open_port no aparecera valor
         s.connect((ip_add_ent, port))
         # si la siguiente linea corre y entonces es una coneccion exitosa al puerto (puerto abierto)
         open_ports.append(port)

    except:
        pass
    
for port in open_ports:
    print(f"port {port} is open on {ip_add_ent}.")
