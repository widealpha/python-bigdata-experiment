if __name__ == '__main__':
    import os
    import hashlib

    fileName = 'ex_file.py'
    if os.path.isfile(fileName):
        with open(fileName, 'rb') as fp:
            data = fp.read()
            print(hashlib.md5(data).hexdigest())


