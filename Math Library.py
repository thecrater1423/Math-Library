import math
class Binary:
    class Operations:
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
    compute=Operations()
class Constants:
    pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    e=2.7182818284590452353602874713527
class Functions:
    def factorial(n):
        if int(n)!=n:
            print("Error! Factorial Function Only Takes Int")
            return
        product=1
        for i in range(2,n+1):
            product*=i
        return product
class Series:
    class MaclaurenEmpty:
        radiusOfConvergence=0
        def nthterm(self,x,i):
            return 0
        def approximation(self,x):
            if self.radiusOfConvergence is not None:
                if x>=self.radiusOfConvergence:
                    print(f"Warning, this output may be divergent for values of x greater than {self.radiusOfConvergence}")
            sum=0
            for i in range(100):
                try :
                    sum+=self.nthterm(x,i)
                except:
                    return sum
            return sum
    class MaclaurenExp(MaclaurenEmpty):
        def nthterm(self,x, i):
            return (x**i)/Functions.factorial(i)
        radiusOfConvergence=None
    class MaclaurenSin(MaclaurenEmpty):
        def nthterm(self,x,i):
            if i%2==0:
                return 0
            if (i+1)%4==0:
                return -(x**i)/Functions.factorial(i)
            return (x**i)/Functions.factorial(i)
        radiusOfConvergence=None
    maclaurenExp=MaclaurenExp()
    maclaurenSin=MaclaurenSin()

    
print(Series.maclaurenSin.approximation(Constants.pi))