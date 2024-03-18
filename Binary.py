import math
class Binary:
    def int(self,binaryinput):
        integer=0
        binaryinput=list(str(binaryinput))
        binaryinput.reverse()
        digitplace=0
        for digit in binaryinput:
            if digit=="1":
                integer+=2**digitplace
            elif digit=="0":
                pass
            else:
                print("ERROR OCCURED, INVALID BINARY INPUT")
                return
            digitplace+=1
        return integer
    def binary(self,intinput):
        binaryoutput="1"
        digits=int(math.log2(intinput))
        remainder=intinput-2**digits
        digitslist=list(range(digits))
        digitslist.reverse()
        for item in digitslist:
            if remainder>=2**item:
                remainder-=2**item
                binaryoutput+="1"
            else:
                binaryoutput+="0"

            remainder
        return binaryoutput
    def add(self,binaryinput1,binaryinput2):
        intoutput=self.int(binaryinput1)+self.int(binaryinput2)
        return self.binary(intoutput)
    def multiply(self,binaryinput1,binaryinput2):
        intoutput=self.int(binaryinput1)*self.int(binaryinput2)
        return self.binary(intoutput)
    def power(self,binaryinput1,binaryinput2):
        intoutput=self.int(binaryinput1)**self.int(binaryinput2)
        return self.binary(intoutput)

binary=Binary()
print(binary.power(11,(binary.multiply(binary.binary(30),binary.binary(4)))))