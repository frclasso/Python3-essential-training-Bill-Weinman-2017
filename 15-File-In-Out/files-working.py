#!/ussr/bin/python3


def main():
    buffersize = 500000
    infile = open('olives.jpg', 'rb') #read binary mode
    outfile = open('new.jpg', 'wb')  #write binary mode
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done.')


if __name__ == " __main__":main()