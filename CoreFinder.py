"""
import math
guid = input("Enter mbx guid\n")
def ToUpperCase(guid) -> object:
    guidListUpper = []
    for g in guid:
        guidListUpper.append(g.upper())
    return guidListUpper
print("uppercase",ToUpperCase(guid))
# to add x instead of - in guid
def GuidAddX(guidListUpper):
    guidlistwithx = []
    guidlistwithx = ToUpperCase(guid)
    guidlistwithX = guidListUpper.replace("-","X")
    return guidlistwithX
print("newguids:-",GuidAddX(guidListUpper))

# to get ascii value of each character of guid list
def GetAscii(guidlistwithX):
    arraylistAscii = []
    for g in guid:
            #To get ascii value
        askvl=(ord(g))
            #To append in arrayList
        arraylistAscii.append(askvl)
    return arraylistAscii
print(GetAscii(guidlistwithX))
#  to convert guidlist to upper characters
"""