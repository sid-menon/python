from winreg import HKEY_LOCAL_MACHINE


def encode(message):
    charA = []
    new = []

    for i in message:
        charA.append(i)
    
    for x in charA:
        q = ord(charA[x])
        new.append(q)
    for i in new:
        new[x] << 2
    return new

mes = encode(input("enter:"))

print(mes)