import socket
import operator

def isItANumber(num):
    try:
        float(num)
        return True
    except ValueError:
        pass

def calculator(equation):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                 '/': operator.floordiv}  # RPN claculator operators
    stack = [] #RPN calculator stack
    for tk in equation:
        if isItANumber(tk):
            stack.insert(0,tk)
        else:
            if len(stack) < 2:
                print('Error: Check the equation.')
                break
            else:
                print ('All values in stack: ', stack)
                operator1 = float(stack.pop(1))
                operator2 = float(stack.pop(0))
                result = OPERATORS[tk](operator1,operator2)
                stack.insert(0,str(result))
    return result

def server():
    host = socket.gethostname() #getting host adress
    port = 5000 #port must be higher than 1024
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((host, port)) #bind takes tuple as argument
    while True:
        serv.listen(1)  # max number of clients connected - in excercise only 1 client
        conn, addr = serv.accept()  # accept new connection
        print("Connection from: " + str(addr))
        while True:
            data = conn.recv(4096)
            if not data:
                 break
            equation = data.decode().split(' ')
            answer = calculator(equation)
            print('RESULT: ', answer)
            conn.send(str(answer).encode())
        conn.close() #connection closed
        print('client disconnected')

if __name__ == '__main__':
    server()
