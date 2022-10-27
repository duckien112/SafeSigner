import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def changeSeeds(seeds, number, isOrigin):
    t = seeds.split(" ")
    t1 = t.copy()
    for index in range(len(number)):
        if(isOrigin == '1'):
            t1[index] = t[int(number[index])-1]
        else:
            t1[int(number[index])-1] = t[index]
    return ' '.join(t1)
    
def encryptSeeds(action, number, password, seeds):
    integer_val=16
    salt = integer_val.to_bytes(16, 'big')
    #print(salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(str.encode(password)))
    f = Fernet(key)

    if(action == '1'):
        mixSeeds = changeSeeds(seeds, number, action)
        token = f.encrypt(str.encode(mixSeeds))
        return token.decode("utf-8")
    else:
        encryptedSeeds = f.decrypt(str.encode(seeds)).decode("utf-8")
        return changeSeeds(encryptedSeeds, number, action)