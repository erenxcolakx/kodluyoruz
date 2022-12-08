liste=[[2,['i','abc'],3,','],[['i',3],6]]
resultList=[]
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            resultList.append(i)
flatten(liste)
print(resultList)