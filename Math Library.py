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
    def doubleFactorial(n):
        if n==0:
            return 1
        if int(n)!=n:
            print("Error! Double Factorial Function Only Takes Int")
            return
        product=1
        if n%2==0:
            for i in range(2,n+1,2):
                product*=i
            return product
        for i in range(1,n+1,2):
            product*=i
        return product
class Limit:
    def inf(function,increment,final):
        for i in range(0,final,increment):
            try:
                print(function(i))
            except:
                print("Error Occured While Calculating. Possibly due to a value too large.")
        return

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
class LinAl:
    class Vectors:
        def collumns(matrix):
            pass
        def rows(matrix):\
            pass
        def dotProduct(vector1,vector2):
            pass
        def crossProduct(vector1,vector2):
            pass
    class Matrices:
        def compileFromCollumns(collumns):
            pass
        def compileFromRows(rows):
            values=[]
            rowNumber=len(rows)
            collumnNumber=len(rows[0].values)
            for row in rows:
                for value in row.values:
                    values.append(value)
            return rowNumber,collumnNumber,values
        def multiply(matrix1,matrix2):
            pass
    class Matrix:
        def __init__(self,rows,collumns,values):
            self.rows=rows
            self.collumns=collumns
            self.values=values
        
    class Vector:
        def __init__(self,values):
            self.values=values
rowa=LinAl.Vector([1,2,3])
rowb=LinAl.Vector([1,2,3])
rowc=LinAl.Vector([1,2,3])
rows,collumns,values=LinAl.Matrices.compileFromRows([rowa,rowb,rowc])
MatrixA=LinAl.Matrix(rows,collumns,values)
print (MatrixA.values)