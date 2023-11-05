def asterisk(i):
    if i > 1:
        asterisk(i / 2)
        asterisk(i / 2)
    print('*', end=' ')

asterisk(5)