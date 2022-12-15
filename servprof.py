import socket
import sys
import os , subprocess ,psutil

m_kill = "kill"
m_disconnect = "disconnect"
m_reset = "reset"

host = "localhost"
port = int(input("Mettez votre port :"))

message_client = ""

def help():
    help =["ip" , "hostname","ram","cpu","os"]
    re =""
    for element in help:
       re = element
    return re

def ip():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    return f"L'ip de votre machine : {ip}"

def nom():
    name = socket.gethostname()
    return f"Le nom de la machine est : {name}"


def ram():
    cmd = psutil.virtual_memory()
    ram1 = cmd[0] / 1000000000
    ram2 = cmd[1] / 1000000000
    ram3 = cmd[3] / 1000000000
    return f"Memoire Total :{ram1}\n " \
           f"Memoire utilisée :{ram2} \n" \
           f"Memoire libre :{ram3}"


def stockage():
    stockage = psutil.disk_usage("/")
    stockage1 = stockage[0] / 1000000000
    stockage2 = stockage[1] / 1000000000
    stockage3 = stockage[2] / 1000000000
    return f"Stockage total {stockage1}\n  , {stockage2}\n , {stockage3}"



def OS():
    cmd=sys.platform
    if cmd == "win32":
        #print("voici l'OS de votre pc")

        return cmd

def cpu ():
    cpu = psutil.cpu_count()
    #cmd = str(subprocess.check_output("wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status", shell=True))
    return cpu

def execute(cmd):
    if cmd == 'cpu':
        res = cpu()

        print(f'voici le cpu de la machine: {res}')

    elif cmd == 'os':
        res = OS()

        print(f"L OS est un {res}")

    elif cmd == 'ram':
        res = ram()

        print(f"ram {res}")


    elif cmd == 'stockage':
        res = stockage()

        print(f"{res}")

    elif cmd == 'ip':
        res = ip()

        print(f"{res}")

    elif cmd == 'help':
        res = help()

        print(f"{res}")

    elif cmd == 'hostname':
        res = nom()

        print(f"{res}")

    elif cmd[0:4] == "DOS:":
        re = cmd.split(':')[1]
        res = subprocess.check_output(re,shell =True).decode("cp850")

        return f"{res}"

    elif cmd[0:4] == "ping":
        re = cmd.split(' ')[1]
        res = subprocess.getoutput(cmd)

        return f"{res}"



    else :
        res = "Unknown Command"
        return str(res)




def serveur():
    message_client = ""
    while message_client != "kill":

        message_client = ""
        while message_client != "kill":
            server_socket = socket.socket()
            server_socket.bind((host, port))
            server_socket.listen(2)
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
                try:
                    conn.send('DISCONNECT'.encode())
                except:
                    pass
                conn.close()
                print("Fermeture de la socket client")

            server_socket.close()
            print("Fermeture du serveur")


if __name__ == '__main__':
    serveur()