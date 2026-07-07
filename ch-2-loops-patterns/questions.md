Question-1 --------------------- Print the Rectangle -------------------------
* * * * * * 
* * * * * * 
* * * * * *

class Rectangle:
    def __init__(self,rows,columns):
        
        for i in range(1,rows+1):
            pattern = ""
            for j in range(1,columns+1):
                pattern+="* "
            print(pattern)


Rectangle(3,6)


Question-2 --------------------- Print the Hollow Rectangle -------------------------
* * * * * * * * * * 
*                 * 
*                 * 
*                 * 
* * * * * * * * * *

class Rectangle:
    def __init__(self,rows,columns):

        for i in range(1,rows+1):
            pattern = ""
            for j in range(1,columns+1):
                if(j==1 or j==columns  or i == 1 or i == rows):
                    pattern+="* "
                else:
                    pattern+="  "
            print(pattern)


Rectangle(5,10)

Question-3 --------------------- Print the Square -------------------------
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *



class Square:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n+1):
                pattern+="* "
            print(pattern)


Square(5)



Question-4 --------------------- Print the hollow Square -------------------------
* * * * * 
*       * 
*       * 
*       * 
* * * * * 


class Square:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n+1):
                if (i==1 or i==n or j ==1 or j==n):
                    pattern+="* "
                else:
                    pattern+="  "
            print(pattern)


Square(5)


Question-5 --------------------- Print the Left Triangle -------------------------
* 
* * 
* * * 
* * * * 
* * * * *

class LeftTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+="* "
            print(pattern)


LeftTriangle(5)


Question-6 --------------------- Print the Reverse Left Triangle -------------------------
* * * * * 
* * * * 
* * * 
* * 
* 

class ReverseLeftTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+2):
                pattern+="* "
            print(pattern)


ReverseLeftTriangle(5)


Question-7 --------------------- Print the  Right Triangle -------------------------
        * 
      * * 
    * * * 
  * * * * 
* * * * *


class RightTriangle:
   def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "
            
            for k in range(1,i+1):
                pattern+="* "
            
            print(pattern)

RightTriangle(5)


Question-8 --------------------- Print the Reverse  Right Triangle -------------------------

* * * * * 
  * * * * 
    * * * 
      * * 
        *


class ReverseRightTriangle:
      def __init__(self,n):
            for i in range(1,n+1):
                  pattern = ""

                  for j in range(1,i):
                        pattern+="  "
                  
                  for k in range(1,n-i+2):
                        pattern+="* "

                  print(pattern)
                    

ReverseRightTriangle(5)

Question-9 --------------------- Print the Hollow Left Triangle -------------------------
Note:- practice all Hollow Triangle (left reverse, right , right reverse )
* 
* * 
*   * 
*     * 
* * * * *



class HollowLeftTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                if (j==1 or i == n or i==j):
                    pattern+="* "
                else:
                    pattern+="  "
            print(pattern)



HollowLeftTriangle(5)


Question-10 --------------------- Print the Rombus Pattern -------------------------
        * * * * * 
      * * * * * 
    * * * * * 
  * * * * * 
* * * * *

class Rombus:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "
            
            for k in range(1,n+1):
                pattern+="* "
            
            print(pattern)

Rombus(5)



Question-11 --------------------- Print the Pyramid Pattern -------------------------
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *



class Pyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "
            
            for k in range(1,2*i):
                pattern+="* "
            
            print(pattern)


Pyramid(5)


Question-11 --------------------- Print the Reverse Pyramid Pattern -------------------------
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 


class ReversePyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i):
                pattern+="  "
            
            for k in range(1,2*(n-i+1)):
                pattern+="* "
            
            print(pattern)


ReversePyramid(5)


Question-12 --------------------- Print the Left Pyramid Pattern -------------------------

Logic :- Break into two part like Left triangle and Reverse Left Triangle

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


class LeftPyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+="* "
            print(pattern)
        
        for k in range(1,n):
            pattern =""
            for m in range(1,n-k+1):
                pattern+="* "
            
            print(pattern)

LeftPyramid(5)


Question-13 --------------------- Print the Right Pyramid Pattern -------------------------

Logic :- Break into two part like Right triangle and Reverse Right Triangle

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 


class RightPyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "

            for k in range(1,i+1):
                pattern+="* "
            
            print(pattern)
        
        for x in range(1,n):
            pattern=""
            for y in range(1,x+1):
                pattern+="  "
            
            for z in range(1,n-x+1):
                pattern+="* "
            
            print(pattern)

RightPyramid(5)


Question-14 --------------------- Print the Hollow Pyramid Pattern ------------------------- (Practice All Hollow Pyramid Left , Right , Reverse)


        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * * 


class HollowPyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            patter = ""
            for j in range(1,n-i+1):
                patter+="  "
            
            for k in range(1,2*i):
                if k==1 or k == (2*i)-1 or i == n:
                    patter+="* "
                else:
                    patter+="  "

            print(patter)


HollowPyramid(5)



Question-15 --------------------- Print the Diamond Pattern -------------------------
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 




class Diamond:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1, n-i+1):
                pattern+="  "

            for k in range(1,2*i):
                pattern+="* "
            print(pattern)

        for x in range(1,n):
            pattern = ""
            for y in range(1,x+1):
                pattern+="  "
            
            for z in range(1,2*(n-x)):
                pattern+="* "
            print(pattern)

Diamond(5)


Question-16 --------------------- Print the Diamond Pattern -------------------------
        * 
      *   * 
    *       * 
  *           * 
*               * 
  *           * 
    *       * 
      *   * 
        * 




class Diamond:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1, n-i+1):
                pattern+="  "

            for k in range(1,2*i):
                if k==1 or k == (2*i)-1:
                    pattern+="* "
                else:
                    pattern+="  "
            print(pattern)

        for x in range(1,n):
            pattern = ""
            for y in range(1,x+1):
                pattern+="  "
            
            for z in range(1,2*(n-x)):
                if z == 1 or z == 2*(n-x)-1:
                    pattern+="* "
                else:
                    pattern+="  "
            print(pattern)

Diamond(5)




Question-17 --------------------- Print the Butterfly Pattern -------------------------
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 *


class Butterfly:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+="* "
            for k in range(1,(2*(n-i))+1):
                pattern+="  "
            for l in range(1,i+1):
                pattern+="* "
            print(pattern)

        for w in range(1,n+1):
            pattern=""
            for x in range(1,n-w+2):
                pattern+="* "
            for y in range(1,2*(w-1)+1):
                pattern+="  "
            for z in range(1,n-w+2):
                pattern+="* "
            print(pattern)





Butterfly(5)


Question-18 --------------------- Print the Number Left Pattern Triangle -------------------------

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5



class NumberTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+=f"{j} "
            print(pattern)
    

NumberTriangle(5)

Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5


class NumLeftTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+=f"{i} "
            print(pattern)


NumLeftTriangle(5)    


Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15


class NumberTriangle:
   def __init__(self,n):
      count = 1
      for i in range(1,n+1):
        pattern = ""
        for j in range(1,i+1):
            pattern+=f"{count} "
            count+=1
        print(pattern) 
    

NumberTriangle(5)


Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1


class NumLeftTriangle:
    def __init__(self,n):
        count = 1
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,i+1):
                pattern+=f"{count+1-j} "
            print(pattern)
            count+=1


NumLeftTriangle(5) 


Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1


class NumLeftTriangle:
      def __init__(self,n):
            for i in range(1,n+1):
                pattern = ""
                for j in range(1,n-i+2):
                    pattern+=f"{j} " 
                print(pattern)                   
    

NumLeftTriangle(5) 


Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1

class NumLeftTriangle:
      def __init__(self,n):
            for i in range(1,n+1):
                pattern = ""
                for j in range(1,i+1):
                    if (i+j) % 2 == 0:
                        pattern+="1 "
                    else:
                         pattern+="0 "              
                print(pattern)

NumLeftTriangle(5) 

Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------

1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1

class NumLeftTriangle:
      def __init__(self,n):
            for i in range(1,n+1):
                pattern = ""
                for j in range(1,i+1):
                    pattern+=f"{j % 2 } "           
                print(pattern)

NumLeftTriangle(5) 

Question-19 --------------------- Print the Number Left Pattern Triangle -------------------------
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

class NumLeftTriangle:
      def __init__(self,n):
            for i in range(1,n+1):
                pattern = ""
                for k in range(1,n-i+1):
                    pattern+="  "
                     
                for j in range(1,i+1):
                    pattern+=f"{i} "           
                print(pattern)

NumLeftTriangle(5) 

Question-19 --------------------- Print the Number Pascal Pattern Triangle -------------------------

Logic: nCr ==> n! // (r! * (n-r)!) for every element. 

        1
      1 1
    1 2 1
  1 3 3 1
1 4 6 4 1

class NumLeftTriangle:
    def __init__(self,n):
        self.n = n
    
    def factorial(self,num):
        if num < 2:
            return 1
        
        return num * self.factorial(num-1)
    
    def pascalTriangle(self):
        for i in range(0,self.n):
            pattern = ""
            for j in range(0,self.n -1 -i):
                pattern+="  "
            for k in range(0,i+1):
                pattern+=f"{self.factorial(i) // (self.factorial(k) * self.factorial(i-k))} "
            print(pattern)
      


demo = NumLeftTriangle(5)   
demo.pascalTriangle()


Question-19 --------------------- Print the Number Pascal Pattern Triangle -------------------------


        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9



class NumTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "
            for k in range(1,2*i):
                pattern+=f"{k} "
            print(pattern)


NumTriangle(5)

Question-19 --------------------- Print the Number Pascal Pattern Triangle -------------------------

        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 

class NumTriangle:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            for j in range(1,n-i+1):
                pattern+="  "
            for k in range(1,2*i):
                pattern+=f"{k} "
            print(pattern)

        for x in range(1,n):
            pattern=""
            for y in range(1,x+1):
                pattern+="  "
            for z in range(1,2*(n-x)):
                pattern+=f"{z} "
            print(pattern)




NumTriangle(5)


Question-21 --------------------- Print this pattern -------------------------

        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 



class CharTriangle:
   def __init__(self,n):
       for i in range(1,n+1):
           pattern = ""
           rowValue = i
           
           for j in range(1,n-i+1):
               pattern+="  "

           for k in range(1,i+1):
               pattern+=f"{k} "

           for y in range(1,i):
               pattern+=f"{rowValue-y} "

           print(pattern)

               
CharTriangle(5)

Question-22 --------------------- Print this pattern -------------------------

        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 

class NumPyramid:
    def __init__(self,n):
        count =1
        for i in range(1,n+1):
            pattern=""
            for k in range(1,n-i+1):
                pattern+="  "
            for j in range(1,2*i):
                pattern+=f"{count} "
            print(pattern)
            count+=1

NumPyramid(5)

Question-22 --------------------- Print this concentric square pattern -------------------------

5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5


class NumberSquare:
    def __init__(self,n):
        size = 2*n-1
        for i in range(size):
            pattern = ""
            for j in range(size):
                top = i
                left = j
                bottom = size - 1 - i
                right = size - 1 -j
                layer = min(top,left,bottom,right)
                pattern+=f"{n-layer} "
            print(pattern)

NumberSquare(5)

Question-22 --------------------- Print this sneck pattern -------------------------

1 2 3 4 
8 7 6 5 
9 10 11 12 
16 15 14 13 


class SneckPattern:
    def __init__(self,rows,cols):

        for row in range(rows):
            pattern =""

            start = row * cols + 1
            end = start + cols -1
            
            if row % 2 == 0:
                for num in range(start,end+1):
                    pattern+=f"{num} "
            else:
                for num in range(end,start-1,-1):
                    pattern+=f"{num} "
            
            print(pattern)

SneckPattern(4,4)

Question-22 --------------------- Print this spiral matrix pattern -------------------------             

1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7

class SpiralMatrix:
    def __init__(self,n):

        matrix = [[0]*n for _ in range(n)]
        top = 0 
        left = 0
        right = n-1
        bottom = n-1

        num = 1

        while top <= bottom and left <= right:
            # Left to right 
            for i in range(left,right+1):
                matrix[top][i] = num
                num+=1
            top+=1

            #Top to bottom
            for j in range(top , bottom+1):
                matrix[j][right] = num
                num+=1
            right-=1
            
            # Right to Left 
            if top <= bottom:
                for k in range(right,left-1,-1):
                    matrix[bottom][k] = num
                    num+=1
                bottom-=1
            
            # Bottom to top 
            if left <= right:
                for l in range(bottom,top-1,-1):
                    matrix[l][left] = num
                    num+=1
                left+=1
            
        for row in matrix:
            print(*row)

SpiralMatrix(4)


Question-20 --------------------- Print the Charactors Left Triangle -------------------------

A 
A B 
A B C 
A B C D 
A B C D E 


class CharTriangle:
   def __init__(self,n):
       for i in range(1,n+1):
            pattern =""
            ch = 65
            for j in range(1,i+1):
                pattern+=f"{chr(ch)} "
                ch+=1
            print(pattern)


CharTriangle(5)

Question-23 --------------------- Print this char pattern Pyramid -------------------------
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 


class CharPyramid:
    def __init__(self,n):
        for i in range(1,n+1):
            pattern = ""
            char = 65
            for j in range(1,n-i+1):
                pattern+="  "
            
            for k in range(1,i+1):
                pattern+=f"{chr(char+k-1)} "
            
            for m in range(1,i):
                pattern+=f"{chr(char+i-m-1)} "
            
            print(pattern)
            
CharPyramid(5)