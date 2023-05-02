import socket
import json
import random

############################################
# Alice acts as client and connects to Bob #
############################################


# Do not change this function
def connect_and_get_socket():
    port = 4321
    host = 'localhost'  # socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


# Do not change this function
def send(p, q, g, gx, client_socket):
    encoded_data = json.dumps({'p': p, 'q': q, 'g': g, 'gx': gx})
    client_socket.send(encoded_data.encode('ascii'))


# Do not change this function
def receive(client_socket):
    # Receive no more than 1024 bytes
    data = client_socket.recv(1024)
    return json.loads(data)


def generate_x(q):
    # Replace this with the generation of a random integer x in the proper range
    x = random.randint(1,q-1)
    return x


def compute_g_x_mod_p(g, x, p):
    # Replace this with the computatoin of g ** x. For performance reason, use
    # pow(base, exponent, modulo) instead of base ** exponent % modulo
    gx = pow(g,x,p)
    return gx


def compute_shared_secret(gy, x, p):
    # Replace this with the computation of the shared secret
    shared_secret = pow(gy,x,p)
    return shared_secret


def exchange_shared_secret():
    """This is the main DH function for Alice. It computes gx = g ** x, and
    sends it to Bob. Then, it uses gy = g ** y received from Bob to compute the
    shared secret."""
    #######################################################
    # Some public parameters. Both q and 2q+1 are primes. #
    #######################################################
    q = 51733955177920554523556498583707150890400087957938764433568354798808049950581
    p = 2 * q + 1
    g = 2
    ######################################################

    # Generate x and compute gx:
    x = generate_x(q)
    # Change the parameters with the correct ones
    gx = compute_g_x_mod_p(g, x, p)

    # Connect to Bob and run DH
    s = connect_and_get_socket()
    # Send public parameters as well as gx to
    send(p, q, g, gx, s)
    # Receive gy
    data = receive(s)
    gy = data['gy']
    # Compute shared secret
    # Change the parameters with the correct ones
    gxy = compute_shared_secret(gy, x, p)
    print(gxy)


if __name__ == "__main__":
    exchange_shared_secret()
