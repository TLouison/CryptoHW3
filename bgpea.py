#Implementation of Blum-Goldwasser cryptosystem for Cryptography I 
#Written by: Todd Louison

#Please make sure to install 
try:
    import gmpy
except ImportError:
    print("You must install the gmpy package for this script to run.")
    quit()
    
import math
import numpy
import random

#Defining given constants
P = 499
Q = 547
A = -57
B = 52

m = '10011100000100001100'

#Takes a list of binary integers and concatenates them all into a string
def printableList(l):
    return ''.join([str(x) for x in l])

#Computes the B list, gathering the least significant bits of x_i
def computeB():
    global X
    #Generating bits for BBS
    b = []
    for i in range(L):
        #Getting b_i = least sig. bit of x_i
        b.insert(0, int(bin(X[i])[-1]))

        #Calculating x_(i+1) = (x^2)%N
        X.append( (X[i]*X[i])%N )
    
    return b

if __name__ == "__main__":
    #Printing long lines because im anal about separating output from commands ¯\_(ツ)_/¯
    print("\n=====================================================")

    global X
    X = [159201]

    #Quickly converting string to list of ints for easier bitwise operating
    m = [int(x) for x in m]
    print("The plaintext is:\t", printableList(m))

    ############################### KEY GENERATION ###########################

    #Generating public key and bitlength of m
    N = P*Q
    L = len(m)

    ################################# ENCRYPTION #############################

    b = computeB()

    #XORing bits to generate ciphertext
    c = []
    for i in range(L):
        bit = int(m[i])

        #XOR operation on plaintext[i] ^ X[i]
        c.append(bit ^ b[i])

    print("The ciphertext is:\t", printableList(c))

    print("\nSent to Alice: \t\t({}, {})\n".format(printableList(c), X[L]))

    ################################# DECRYPTION #############################

    r_p = pow(X[L], (((P+1)//4)**L), P)
    r_q = pow(X[L], (((Q+1)//4)**L), Q)

    #Getting the multiplicative inverses of the primes
    P_inverse = int(gmpy.invert(499, 547))
    Q_inverse = int(gmpy.invert(547, 499))

    #Redefining our global X for our new B array
    X = [((Q * (Q_inverse % P) * r_p) + (P * (P_inverse % P) * r_q)) % N]

    new_B = computeB()

    #XORing the ciphertext to recompute the plaintext
    new_m = []
    for i in range(L):
        bit = int(c[i])

        #XOR operation on ciphertext[i] ^ X[i]
        new_m.append(bit ^ new_B[i])

    print("Alice deciphered to:\t", printableList(new_m))
    print("Original message was:\t", printableList(m))
    print("=====================================================\n")

