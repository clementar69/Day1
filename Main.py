
if __name__=='__main__':
    f = open("input.txt","r")
    data = f.read().split("\n")
    result = 0
    compteur = 0

    for i in range(0,len(data)):
        data[i]=int(data[i])
    for i in range(0,len(data)-3):
        n1 = data[i]
        n2 = data[i+1]
        n3 = data[i+2]
        n4 = data[i+3]
        if n1 + n2 + n3 <  n2 + n3 + n4:
            compteur = compteur + 1

    print(compteur)










    print(compteur)







