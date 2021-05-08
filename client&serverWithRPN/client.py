import socket

def client():
    host = socket.gethostname() #getting host adress
    port = 5000 #port must be higher than 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
    except socket.error as e:
        print(str(e))

    while True:
        message = input("Type operation\n -> ")  # take input

        if message.lower().strip() == 'quit':
            break
        else:
            client.send(message.encode())
            response = client.recv(1024)
            print("Result: "+response.decode("utf-8"))
    client.close()
if __name__ == '__main__':
    client()
