import ast

def listToFile(l,path):
    file = open(path,'w')
    file.write(str(l))
    file.close()

def filetoList(path):
    file = open(path,'r')
    l = ast.literal_eval(file.read())
    return l