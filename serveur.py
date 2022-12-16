import socket
import sys
import os , subprocess ,psutil



host = "localhost"
port = int(input("Mettez votre port :"))

message_client = ""

def help():

    return ("""COMMANDE: --ip-- -- hostname -- -- ram-- -- os -- -- cpu -- -- kill -- -- reset -- -- disconnect \n- ping - PYHTON -VERSION - DOS: - linux:- PowerShell: """)

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
    return f"Memoire Total :{ram1}\n"\
           f"Memoire utilisée :{ram2}\n"\
           f"Memoire libre :{ram3}"

def DOS(cmd):

    try:
        if sys.platform == "win32":
            re = cmd.split(':')[1]
            res = subprocess.check_output(re, shell=True).decode("cp850")
            return res
        else:
            return "DOS n'est pas correcte essayer linux ou PowerShell"
    except:
        return 'Error command'

def linux(cmd):
    try:
        if sys.platform == "linux" or sys.platform == "linux2":
            x = cmd.split(":", 1)[1]
            res= subprocess.getoutput(x)
            return res
        else:
            return "Linux n'est pas correcte essayer DOS ou PowerShell"

    except:
        return 'Error command'

def powershell(cmd):
    try:
        if sys.platform == "win32":
            shell = cmd.split(":", 1)[1]
            res = subprocess.getoutput('PowerShell -command "' + shell + '"')
            return res
        else:
            return 'PowerShell commands are not recognized try Linux'
    except:
        return 'Error command'



def OS():
    res = sys.platform
    if res == 'win32':
        res = 'La machine est un Windows'
    elif res == 'linux' or res == 'linux2':
        res = 'La machine est un Linux'
    elif res == 'darwin':
        res = 'La machine est un MAC OS '
    return res


def cpu ():
    res = psutil.cpu_percent()
    return f'Capaciter du CPU: {res} %'


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
        res = DOS(cmd)
        return f"{res}"

    elif cmd[0:6].lower() == 'linux:':
        res = linux(cmd)
        return f"{res}"

    elif cmd[0:11].lower() == 'powershell:':
        res = powershell(cmd)
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
    while message_client.lower() != "kill":

        message_client = ""
        while message_client.lower() != "kill":
            server_socket = socket.socket()
            server_socket.bind((host, port))
            server_socket.listen(2)
            print(f"Socket ouverte sur {host} - {port}")

            message_client = ""
            while message_client.lower() != "kill" and message_client.lower() != "reset":
                print('> En attente du client')
                conn, address_client = server_socket.accept()
                print(f'Client connecté {address_client}')
                try:
                    message_client = ""
                    while message_client.lower() != "kill" and message_client.lower() != "reset" and message_client.lower() != "disconnect":

                        message_client = conn.recv(1024).decode()
                        print(f"Message reçu {message_client}")
                        execution = execute(message_client)
                        conn.send(execution.encode())
                except:
                    pass
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