ciphertext = open('pass','r').read()
dict = open('/home/prosen/opt/dict/rockyou.txt', 'r').read().split('\n')
for key in dict:
    msg = decrypt(key, ciphertext)
    if 'the ' in msg or 'be ' in msg or 'and ' in msg or 'of ' in msg:
            exit("Key: {0}, Key length: {1}, Msg: {2}".format(key, len(key), msg))
