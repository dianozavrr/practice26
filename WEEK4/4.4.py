import hashlib, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

msg = b"Hello, world!"

print("Хеш:", hashlib.sha256(msg).hexdigest())

key = os.urandom(32)
iv = os.urandom(16)
c = Cipher(algorithms.AES(key), modes.CFB(iv))
enc = c.encryptor().update(msg)
dec = c.decryptor().update(enc)
print("AES шифр:", enc)
print("AES дешифр:", dec)

priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pub = priv.public_key()
sig = priv.sign(msg, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
try:
    pub.verify(sig, msg, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    print("Підпис ок ✔")
except:
    print("Підпис ❌")

print("Геш = відбиток, назад не розшифрувати.")
print("AES = можна зашифрувати і розшифрувати ключем.")
