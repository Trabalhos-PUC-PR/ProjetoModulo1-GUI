filePath = "./storage/storage1.txt"

def getPasswordSet():
    file = open(filePath, "r")
    lines = file.readlines()
    rows = len(lines)
    cols = 3
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    cont = 0
    for line in lines:
        passSet = line.strip().split("-")
        matrix[cont][0] = passSet[0]
        matrix[cont][1] = passSet[1]
        matrix[cont][2] = passSet[2]
        cont+=1
    return matrix
    
print(getPasswordSet())