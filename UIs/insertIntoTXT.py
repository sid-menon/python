
def insert(filename, text):
    file = open(filename,"a")

    file.write(text)
    file.close()
