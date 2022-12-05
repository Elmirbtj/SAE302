import socket
import sys
import os , subprocess

m_kill = "kill"
m_disconnect = "disconnect"
m_reset = "reset"

host = "localhost"
port = 5006

message_client = ""

def execute(cmd):
    return str(cmd)

def ipconfig():
    print ("Your OS is ", sys.platform)
    if sys.platform == 'win32':
        print (os.system("ipconfig"))
    elif sys.platform == 'linux2':
        print (os.system("ifconfig"))
    time.sleep(5)


def ram():
    cmd = str(subprocess.check_output("wmic computersystem get totalphysicalmemory.", shell=True))
    return cmd


def OS():
    cmd=sys.platform
    if cmd == "win32":
        #print("voici l'OS de votre pc")

        return cmd

def cpu ():
    cmd = str(subprocess.check_output("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status", shell=True))
    return cmd

def serveur():
    message_client = ""
    while message_client != "kill":

        message_client = ""
        while message_client != "kill":
            server_socket = socket.socket()
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Socket ouverte sur {host} - {port}")

            message_client = ""
            while message_client != "kill" and message_client != "reset":
                print('FD> En attente du client')
                conn, address_client = server_socket.accept()
                print(f'Client connecté {address_client}')

                message_client = ""
                while message_client.lower() != m_kill and message_client.lower() != m_reset and message_client.lower() != m_disconnect:
                    message_client = conn.recv(1024).decode()
                    print(f"Message reçu {message_client}")
                    execution = execute(message_client)
                    conn.send(execution.encode())
                    if message_client == 'cpu':
                        res = cpu()
                        conn.send(res.encode())
                        print(f'voici le cpu de la machine: {res}')
                    if message_client == 'os':
                        res = OS()
                        conn.send(res.encode())
                        print(f"L OS est un {res}")
                    if message_client == 'ram':
                        res = ram()
                        conn.send(res.encode())
                        print(f"ram {res}")
                conn.close()
                print("Fermeture de la socket client")

            server_socket.close()
            print("Fermeture du serveur")


if __name__ == '__main__':
    serveur()