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
   
   ## Algorithm Walkthrough
   ### Key Generation
   The first step of this algorithm is generating the public key, which is simply created by multiplying our two predetermined primes, 499 and 547. This provides us with N=272953.
   
   ## Encryption
   The encryption process is defined by two main steps, since we already have X<sub>0</sub>.
   1. Generate bitstream B by:
      a. For each bit in the original message, generate b<sub>i</sub> by taking the least significant bit of x<sub>i</sub>.
      b. After each iteration of the above, calculate the next x by x<sub>i</sub> = (x<sub>i-1</sub>)<sup>2</sup> mod N.
   2. For each bit in B, determine c<sub>i</sub> = m<sub>i</sub> XOR b<sub>i</sub>
      
   We now send a message in the format of (c, x<sub>L</sub>) to Alice for decryption.
   
   ## Decryption
   Now that Alice has the ciphertext c and the y = x<sub>L</sub>, she can decrypt the ciphertext.
   1. Determine two values r<sub>p</sub> and r<sub>q</sub> using the following formulas:</br>
      a. r<sub>p</sub> = y<sup>((p+1)/4)<sup>L</sup></sup>mod p</br>
      b. r<sub>q</sub> = y<sup>((q+1)/4)<sup>L</sup></sup>mod q</br>
      
   2. Get the initial seed for x using the formula x<sub>0</sub>= (q(q<sup>-1</sup>mod p)r<sub>p</sub> + p(p<sup>-1</sup>mod q)r<sub>q</sub>) mod N.
   
   3. Perform the same step as Encryption 1.
   
   4. Finally get the plaintext by XORing each bit m<sub>i</sub> = c<sub>i</sub> XOR b<sub>i</sub>.
      
      
