#replace - by X
#find ascii value of every character
#sum of ascii values
#mod 8
import math

guid=input("Enter mbx guid\n")

def GuidAddX(guid):
    guidlist=[]
    guidlist=guid
    #print("guidlist",guidlist)
    guidlistNew=guidlist.replace("-","x")
    return guidlistNew
print("newguids:-",GuidAddX(guid))

def GetAscii(guid):
    arraylistNew = []
    for g in guid:
            #To get ascii value
        ask=(ord(g))
            #To append in arrayList
        arraylistNew.append(ask)
    return arraylistNew
print(GetAscii(guid))

