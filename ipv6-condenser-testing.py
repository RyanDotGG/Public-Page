
import re

def condenser(ipv6:str):
    split = ipv6.split(":")
    removedLeading = removeLeadingZeros(split)
    return removelargestZeroGroup(removedLeading)

def removeLeadingZeros(splits:list):
    answer=[]
    for hextet in splits:
        if int(hextet,16) == 0:
            answer.append(hextet)
        else:
            answer.append(hextet.lstrip("0"))
    return answer

def removelargestZeroGroup(removedleadzeros:list):
    totalZerosCount = removedleadzeros.count("0000")
    if totalZerosCount == 0:
        return ":".join(removedleadzeros)
    elif totalZerosCount == 8:
        return "::"
    highest = 0
    current = 0
    for item in removedleadzeros:
        if item == "0000":
            current+=1
        else:
            if current > highest:
                highest = current
                current = 0
    if current > highest:
        highest = current
    joined = ":".join(removedleadzeros)
    pattern = r"(0{4}:?){"+f"{highest}"+r"}"
    result = re.sub(pattern,":",joined,flags=re.IGNORECASE,count=1)
    if result.startswith(":"):
        result = ":"+result
    return result.replace("0000","0")


a="2001:0db8:85a3:0000:0000:8a2e:0370:7334"#2
b="2001:0db8:0000:0000:0000:0000:0000:0001"#5
c="0000:0000:0000:0000:0000:0000:0000:0000"#8

d="0000:0000:0000:0000:0000:0000:0000:0001"#7
e="2001:0db8:85a3:0000:0000:8a2e:0000:7334"#2
f="2001:0000:0000:0db8:0000:0000:0db8:0001"#2
g="2001:0000:0000:0db8:0000:0000:0000:0001"#3

q="0000:0000:0000:0000:0000:0000:0000:0000"#8
r="0000:0000:0000:0000:0000:0000:0000:0001"#7
s="1000:0000:0000:0000:0000:0000:0000:0000"#7

t="1000:0000:0000:0000:0000:0000:0000:1000"#6
u="0000:0000:0000:0000:0000:0000:1000:1000"#6
v="1000:1000:0000:0000:0000:0000:0000:0000"#6
w="0001:0000:0000:0000:0000:0000:0000:0001"#6

x="2001:0db8:85a3:0000:8a2e:8a2e:0370:7334"#1
y="0000:0db8:85a3:0000:0000:8a2e:0370:7334"#2
z="2001:0db8:85a3:0001:0001:8a2e:0370:0001"#0

assert(condenser(a)=="2001:db8:85a3::8a2e:370:7334"),"error"
assert(condenser(b)=="2001:db8::1"),"error"
assert(condenser(c)=="::"),"error"

assert(condenser(d)=="::1"),"error"
assert(condenser(e)=="2001:db8:85a3::8a2e:0:7334"),"error"
assert(condenser(f)=="2001::db8:0:0:db8:1"),f"{condenser(f)}"
assert(condenser(g)=="2001:0:0:db8::1"),"error"

assert(condenser(q)=="::"),"error"
assert(condenser(r)=="::1"),f"{condenser(r)}"
assert(condenser(s)=="1000::"),f"{condenser(s)}"

assert(condenser(t)=="1000::1000"),"error"
assert(condenser(u)=="::1000:1000"),f"{condenser(u)}"
assert(condenser(v)=="1000:1000::"),"error"
assert(condenser(w)=="1::1"),"error"

assert(condenser(x)=="2001:db8:85a3::8a2e:8a2e:370:7334"),f"{condenser(x)}"
assert(condenser(y)=="0:db8:85a3::8a2e:370:7334"),f"{condenser(y)}"
assert(condenser(z)=="2001:db8:85a3:1:1:8a2e:370:1"),"error"

