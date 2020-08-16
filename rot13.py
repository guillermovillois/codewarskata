def rot13(message):
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alpha2='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    print(''.join([alpha2[alpha.find(each)] for each in message]))

rot13("test")
rot13("Test")

