import os


def deletefile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist") 

def fileopen(filename):
    f = open(filename, "r")
    print(f.read())
    f.close()


def writefile(filename,text):
    f = open(filename, "w")
    f.write(text)
    f.close()
    # open and read the file after the appending:
    return fileopen(filename)


