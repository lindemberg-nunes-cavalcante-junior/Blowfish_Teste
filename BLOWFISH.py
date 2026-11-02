'''pycryptodome'''
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

chave = b"minha-chave-secreta"
texto = input("Digite o texto a ser cifrado: ")
byte = bytes(texto,'utf-8')


iv = get_random_bytes(8)
cifra = Blowfish.new(chave, Blowfish.MODE_CBC, iv)
cifrado = iv + cifra.encrypt(pad(byte, Blowfish.block_size))

print(cifrado)

# decifrar
iv = cifrado[:8]
decifra = Blowfish.new(chave, Blowfish.MODE_CBC, iv)
original = unpad(decifra.decrypt(cifrado[8:]), Blowfish.block_size)
print(original)