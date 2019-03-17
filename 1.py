from hashlib import md5
from time import time
from itertools import count, product
from string import printable

counter = 0

def passwords():
    chars = [i.encode("ascii") for i in printable]
    for length in count(start=0):
        for pwd in product(chars, repeat=length):
            yield b''.join(pwd)


def crack(search_hash):
    global counter
    for pwd in passwords():
        counter = counter + 1
        if counter == 600000:
            return(0)
        if md5(pwd).hexdigest() == search_hash:
            return ("The password is: "+ pwd.decode("ascii") + " and the hash is: " + md5(pwd).hexdigest())

def main(password):
    
    hashedPassword = md5(password.encode('ascii')).hexdigest()
    start = time()
    hashPassword = md5(hashedPassword.encode("ascii")).hexdigest()
    cracked = crack(hashedPassword)
    end = time()
    if cracked == 0:
        return 0
    else:  
        return("The Password is " + cracked + " Time: " + str(end - start) + " seconds.")


main(password)