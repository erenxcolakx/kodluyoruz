liste=[[1, 2], [3, 4], [5, 6, 7]]
liste.reverse()
def listControl(n):
    for i in n:
       i.reverse()
    print(liste)
listControl(liste)