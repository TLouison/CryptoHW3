# Cryptography Homework 3
The code implementation for Cryptography, the Blum-Goldwasser Probabilistic Encryption Algorithm. 

## Setup

This code is very simple to run, the only prerequisite is that the user must have gmpy installed. If it is not, the code will not run and will display an error until such time that the package is installed. Once it is, you can run the following command to execute the program:

```shell
python3 bgpea.py
```

This code has many simplifications built directly into it, as outlined in the assignment. For example, in the Blum Blum Shub generator, normally the initial value would be a randomly generated value. For this implementation, our initial value is seeded to be 159201, which creates a deterministic output.

As well as our initial seeding for the generator, our primes are predetermined as well: P=499 and Q=547. Along with this, the message we are encrypting and decrypting is a predetermined string of bits M=10011100000100001100.

## Answers

1. What is the ciphertext? **10110000000110000111**

2. Verify your answer by showing that D(C(m))=m:

   ```c
   The plaintext is:        10011100000100001100
   The ciphertext is:       10110000000110000111
   
   Sent to Alice:          (10110000000110000111, 36858)
   
   Alice deciphered to:     10011100000100001100
   Original message was:    10011100000100001100
   ```