# replace - by x
# convert to upper case
# calculate ansi value of each digit and sum them all
import math
guid = input("Enter mbx guid\n")
def addXforDash(guid):
    guidlistWithX = []
    guidListUpper = []
    guidlistWithX = guid.replace("-","X")
    #print("With X",addXforDash(guid))
    #now convert to upper case
    for g in guidlistWithX:
        guidListUpper.append(g.upper())
    return guidListUpper
print(addXforDash(guid))
def AnsiSumMod(guidListUpper):
    