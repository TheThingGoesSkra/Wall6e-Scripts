ciphertext = open('ciphertext', 'r').read().rstrip()
for i in range(1, 165): # key length assuming that key is not greater than the length of encrypted ciphertext
    for j in range(33, 127): # from ! to ~ (including all A-Z,a-z and 0-9)
        key = chr(j) * i
        msg = decrypt(key, ciphertext)
        if 'the ' in msg or 'be ' in msg or 'and ' in msg or 'of ' in msg :
            exit("Key: {0}, Key length: {1}, Msg: {2}".format(key, len(key), msg))
