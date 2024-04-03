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
            rownumber,collumnnumber,values=matrix
            collumns=[]
            for i in range(collumnnumber):
                collumns.append([])
            i=0
            for value in values:
                collumns[i%rownumber].append(value)
                i+=1
            while len(collumns[collumnnumber-1])!=rownumber:
                collumns[i%rownumber].append(0)
                i+=1
            return collumns
        def rows(matrix):
            rownumber,collumnnumber,values=matrix
            rows=[]
            index=0
            for row in range(rownumber):
                rowvector=[]
                for i in range(collumnnumber):
                    try:
                        rowvector.append(values[index])
                    except:
                        rowvector.append(0)
                    index+=1
                rows.append(rowvector)
            return rows
        def dotProduct(vector1,vector2):
            dotproduct=0
            i=0
            for value in vector1:
                try:
                    dotproduct+=value*vector2[i]
                except:
                    dotproduct+=0
                i+=1
            return dotproduct
        def crossProduct(vector1,vector2):
            pass
    class Matrices:
        def compileFromCollumns(vectors):
            return LinAl.Matrices.transpose(LinAl.Matrices.compileFromRows(vectors))
        def compileFromRows(vectors):
            values=[]
            rowNumber=len(vectors)
            collumnNumber=len(vectors[0])
            for row in vectors:
                for i in range(collumnNumber):
                    if i<len(row):
                        values.append(row[i])
                    else:
                        values.append(0)
            return rowNumber,collumnNumber,values
        def transpose(matrix):
            return LinAl.Matrices.compileFromRows(LinAl.Vectors.collumns(matrix))
        def multiply(matrix1,matrix2):
            rows1,collumns1,values1=matrix1
            rows2,collumns2,values2=matrix2
            if collumns1!=rows2:
                print("These Matrices can not be multiplied, they are the wrong size!")
                return
            newrows=rows1
            newcollumns=collumns2
            newvalues=[]
            for row in LinAl.Vectors.rows(matrix1):
                for collumn in LinAl.Vectors.collumns(matrix2):
                    newvalues.append(LinAl.Vectors.dotProduct(row,collumn))
            return newrows,newcollumns,newvalues
    class Matrix:
        def printMatrix(self):
            rowslist=[]
            i=0
            for row in range(self.rows):
                rowstring="["
                for collumn in range(self.collumns):
                    try:
                        addition=str(self.values[i])
                    except:
                        addition="0"
                    rowstring=rowstring+" "+addition
                    i+=1
                rowstring= rowstring+" ]"
                rowslist.append(rowstring)
            for row in rowslist:
                print(row)
    class MatrixTriple(Matrix):
        def __init__(self,triple):
            rows,collumns,values=triple
            self.key=triple
            self.rows=rows
            self.collumns=collumns
            self.values=values
            self.collumnslist=LinAl.Vectors.collumns(triple)
            self.rowslist=LinAl.Vectors.rows(triple)
    class MatrixRows(Matrix):
        def __init__(self,rowslist):
            rows,collumns,values=LinAl.Matrices.compileFromRows(rowslist)
            self.key=LinAl.Matrices.compileFromRows(rowslist)
            self.rows=rows
            self.collumns=collumns
            self.values=values
            self.collumnslist=LinAl.Vectors.collumns(LinAl.Matrices.compileFromRows(rowslist))
            self.rowslist=rowslist
    class MatrixCollumns(Matrix):
        def __init__(self,collumnslist):
            rows,collumns,values=LinAl.Matrices.compileFromCollumns(collumnslist)
            self.key=LinAl.Matrices.compileFromCollumns(collumnslist)
            self.rows=rows
            self.collumns=collumns
            self.values=values
            self.collumnslist=collumnslist
            self.rowslist=LinAl.Vectors.rows(LinAl.Matrices.compileFromCollumns(collumnslist))
    class Vector:
        def __init__(self,values):
            self.values=values
vectora=LinAl.Vector([1,2,3])
vectorb=LinAl.Vector([1,9])
vectorc=LinAl.Vector([1,8,6])
vectord=LinAl.Vector([1,0,0])
vectore=LinAl.Vector([0,0,1])
vectorf=LinAl.Vector([0,1,0])
MatrixA=LinAl.MatrixCollumns([vectora.values,vectorb.values,vectorc.values])
MatrixB=LinAl.MatrixRows([vectord.values,vectore.values,vectorf.values])
MatrixC=LinAl.MatrixTriple(LinAl.Matrices.multiply(MatrixA.key,MatrixB.key))
MatrixC.printMatrix()


