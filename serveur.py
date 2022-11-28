import socket

def server():

    host = ""
    port = 10000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))







   """ connected = True
    print("connected to server")
    while True:

        data = conn.recv(1024).decode()
        if data == 'bye':
            conn.close()
            server_socket.close()
            break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())
        conn.close()

        try:

            message = server_socket.recv(1024).decode("UTF-8")
            server_socket.send(bytes("Client wave", "UTF-8"))
            print(message)
        except socket.error:

            connected = False
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("connection lost... reconnecting")
            while not connected:

                try:
                    server_socket.connect((host, port))
                    connected = True
                    print("re-connection successful")
                except socket.error:
                    sleep(2)
    conn.close()"""



   # server_socket.listen(5)

   # while True:
   #     conn, address = server_socket.accept()
    #    print(conn.recv(1000).decode())

     #   data = conn.recv(1024).decode()
   #     if data == 'arret':
       #     conn.shutdown(socket.SHUT_RDWR)
      #      conn.close()
       #     break
     #   print("from connected user: " + str(data))
      #  data = input(' -> ')
      #  conn.send(data.encode())
   # conn.close()



        #try:
            #server_socket.listen(5)
           # while True:
           #     if data == 'arret':
                 #   (a, b) = server_socket.accept()
                   # print(a.recv(1000))
      #  except KeyboardInterrupt:
      #      print("arret")
         #   server_socket.shutdown(socket.SHUT_RDWR)
        #    server_socket.close()
      #  if data == 'arret':
           # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
           # server_socket.bind((host, port))
           # print("serveur reset ")
          #  break


if __name__ == '__main__':
    server()