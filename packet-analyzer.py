#https://en.wikipedia.org/wiki/IPv4
ipPacketBinary=\
        "01000101	00000000	00000000	00111100\
        10101001	10011010	01000000	00000000\
        01000000	00000110	01001111	10010011\
        11000000	10101000	10000000	10000000\
        10011111	11001011	01100000	10011010".split()

class IPHeader:
    def __init__(self,byte:list):
        self.version=int(byte[0][:4],2)
        self.ihl=int(byte[0][4:],2)*4
        self.dscp=int(byte[1][:6],2)
        self.ecn=int(byte[1][6:],2)
        self.totlength=int(byte[2]+byte[3],2)
        self.identifier=int(byte[4]+byte[5],2)
        self.flags=int(byte[6][:3],2)
        self.fragoffset=int(byte[6][3:]+byte[7],2)
        self.ttl=int(byte[8],2)
        self.embedprot=int(byte[9],2)
        self.checksum=int(byte[10]+byte[11],2)
        self.sourceip=str(int(byte[12],2))+"."+str(int(byte[13],2))\
                +"."+str(int(byte[14],2))+"."+str(int(byte[15],2))
        self.destip=str(int(byte[16],2))+"."+str(int(byte[17],2))\
                +"."+str(int(byte[18],2))+"."+str(int(byte[19],2))
        #self.options=20 through 448

    def printOut(self):
        print(vars(self))
        # for attribute in dir(self):
        #     if not attribute.startswith("__"):
        #         attributeValue = getattr(self, attribute)
        #         print(f"{attribute}: {attributeValue}")

test = IPHeader(ipPacketBinary)
test.printOut()

# test = ['01000101']
# print(test[0][:4])
# print(test[0][0:])
# print(test[0][4:])
