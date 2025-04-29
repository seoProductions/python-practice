#file io is very simple in python

fileobject = open("matrix.txt", "r")

for i in range(4):
    #read in 1 character at a time
    #remember, python uses a file pointer, smilar to instruction pointer
    print(f" { fileobject.readline() } ", end= "")

    

