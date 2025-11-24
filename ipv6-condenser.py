
def condenser(ipv6:str):
    split = ipv6.split(":")
    removedLeading = removeLeadingZeros(split)
    return removelargestZeroGroup(removedLeading)

def removeLeadingZeros(splits:list):
    answer=[]
    for hextet in splits:
        if int(hextet,16) != 0:
            answer.append(hextet)
        else:
            answer.append(hextet.lstrip("0"))
    return answer

def removelargestZeroGroup(removedleadzeros:list):
    highest = 0
    current = 0
    for item in removedleadzeros:
        if int(item,16) == 0:
            current+=1
    else:
        if current > highest:
            highest = current
    result = ":".join(removedleadzeros)
    pattern = r"0000:"*highest
    result = result.split(pattern)
    result = result[0]+":"+result[1]
    return result

