import ast


def listtofile(l, path):
    file = open(path, 'w')
    file.write(str(l))
    file.close()


def filetolist(path):
    file = open(path, 'r')
    l = ast.literal_eval(file.read())
    return l
