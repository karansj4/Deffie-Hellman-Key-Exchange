import socket
import json
import random

################################################
# Bob acts as server and waits for connections #
################################################


# Do not change this function
def wait_and_get_socket():
    port = 4321
    host = 'localhost'  # socket.gethostname()
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind((host, port))
    serversocket.listen(1)
    (clientsocket, address) = serversocket.accept()
    print("Running Diffie-Hellman key exchange protocol with %s" % str(address))
    return clientsocket


# Do not change this function
def send(gy, client_socket):
    encoded_data = json.dumps({'gy': gy})
    client_socket.send(encoded_data.encode('ascii'))


# Do not change this function
def receive(client_socket):
    # Receive no more than 1024 bytes
    data = client_socket.recv(1024)
    return json.loads(data)


def generate_y(q):
    # Replace this with the generation of a random integer x in the proper range
    y = random.randint(1,q-1)
    return y


def compute_g_y_mod_p(a, b, c):
    # Replace this with the computatoin of g ** x. For performance reason, use
    # pow(base, exponent, modulo) instead of base ** exponent % modulo
    gy = pow(a,b,c)
    return gy


def compute_shared_secret(a, b, c):
    # Replace this with the computation of the shared secret
    shared_secret = pow(a,b,c)
    return shared_secret


def exchange_shared_secret():
    """This is the main DH function for Bob. It computes gy = g ** y, and sends
    it to Alice. Then, it uses gx = g ** x received from Alice to compute the
    shared secret."""
    # Establish socket and wait for incoming connections
    s = wait_and_get_socket()

    # Receive public parameters from Alice
    data = receive(s)
    q = data['q']
    p = data['p']
    g = data['g']
    gx = data['gx']

    # Generate y and compute gy:
    y = generate_y(q)
    # Change the parameters with the correct ones
    gy = compute_g_y_mod_p(g, y, p)

    # Compute shared secret
    # Change the parameters with the correct ones
    gxy = compute_shared_secret(gx, y, p)
    print(gxy)

    # Now send what is missing to Alice, so that she can complete the protocol
    # Change the first parameter with the correct one
    send(gy, s)
    s.close()


if __name__ == "__main__":
    exchange_shared_secret()
