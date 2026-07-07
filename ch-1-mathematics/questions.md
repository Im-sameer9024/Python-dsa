

Question:1 --------------------- Print numbers form 1 to N ------------------
def naturalNum(n):
    for i in range(1,n+1):
        print(i)


naturalNum(10)


Question:2 --------------------- Print numbers form N to 1 ------------------
def naturalNum(n):
    for i in range(n,0,-1):
        print(i)


naturalNum(10) #[0, 2, 4, 6, 8, 10]


Question:3 --------------------- Print all even numbers from 1 to N ------------------

def naturalNum(n):
    evens =[]
    for i in range(0,n+1):
        if i%2==0:
            evens.append(i)
    print(evens)


naturalNum(10) #[1, 3, 5, 7, 9]

Question:4 --------------------- Find the sum of first N natural numbers ------------------

def naturalNum(n):
    return n*(n+1)//2


print(naturalNum(10)) # 55


Question:5 --------------------- Find the factorial of a number ------------------

def factorial(n):
    if n < 2:
        return 1
    
    return n*factorial(n-1)

print(factorial(10)) # 3628800


Question:6 --------------------- Count the number of digits ------------------

Input : 12345 , Output : 5


def countDigits(n):
    copy = n
    count =0
    while copy >0:
        count+=1
        copy = copy//10
    return count 

print(countDigits(12345)) # 5

Question:7 --------------------- Reverse the number ------------------

Input : 12345  , Output : 54321

def countDigits(n):
    copy = n
    reversed = 0
    while copy > 0:
        reminder = copy % 10
        reversed = reversed * 10 + reminder
        copy = copy // 10
    return reversed 

print(countDigits(12345)) # 54321


Question:8 --------------------- Sum of Digits ------------------

Input : 1234 , Output : 10



def sumDigits(n):
    sum = 0
    copy = n
    while copy > 0:
        reminder = copy % 10
        sum += reminder
        copy = copy // 10
    return sum

print(sumDigits(12345)) # 15



Question:9 --------------------- Product of Digits ------------------

Input : 123 , Output : 6

def productDigits(n):
    product = 1
    copy = n
    while copy > 0:
        reminder = copy % 10
        product = product*reminder
        copy = copy // 10

    return product

print(productDigits(12345))


Question:10 --------------------- Check Even or Odd ------------------



def checkEvenOdd(n):
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(checkEvenOdd(1)) # ODD


Question:11 --------------------- find the largest Digit ------------------

Input : 987654 , Output : 9

def largestDigit(n):
    largest = 0
    copy = n
    while copy > 0:
        reminder = copy % 10
        if reminder > largest:
            largest = reminder
        copy = copy // 10
    return largest


print(largestDigit(12345)) # 5


Question:12 --------------------- find the Smallest Digit ------------------


def smallDigit(n):
    smallest = 9
    copy = n
    while copy > 0:
        reminder = copy % 10
        if reminder < smallest:
            smallest = reminder
        copy = copy // 10
    return smallest


print(smallDigit(12345)) # 1


Question:13 --------------------- find the Palindrome Number ------------------

Input : 121 , Output : True

def palindrome(n):
    copy = n
    reversed = 0
    while copy > 0:
        reminder = copy % 10
        reversed = reversed * 10 + reminder
        copy = copy // 10
    return reversed == n

print(palindrome(121)) # True


Question:14 --------------------- Swap two numbers (with and without using third variable) ------------------

( without using )

def swap(a,b):
    
   a = a+b
   b = a-b
   a = a-b
   

   return a, b

print(swap(4,5))

(With using)

def swap(a,b):
    
   temp = a
   a = b
   b = temp
   return a,b

print(swap(4,5))


Question:15 --------------------- Check Prime Number ------------------


import math

def prime(n):

    if n < 2 :
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True

Question:16 --------------------- Check Prime Number -----------------


def printPrimes(n):
    primes = []
    for i in range(2,n+1):
        if prime(i):
            primes.append(i)
    return primes

print(printPrimes(100)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


Question:17 --------------------- Count Prime Number -----------------

def printPrimes(n):
    primes = []
    count = 0
    for i in range(2,n+1):
        if prime(i):
            primes.append(i)
            count+=1
    return primes,count

print(printPrimes(1000000))

Question:18 --------------------- Find All Factors include the number also -----------------

Input : 10 , Output : [1,2,5,10]

import math

def factors(n):
    facts = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            facts.append(i)
            if i != n//i:
                facts.append(n//i)


    return sorted(facts)

print(factors(10))

Question:19 --------------------- Find GCD -----------------

def GCD(a,b):
    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a

print(GCD(5,10)) # 5

Question:20 --------------------- Find LCM -----------------


def LCM(a,b):
    return a*b//GCD(a,b)

print(LCM(5,10))


Question:21 --------------------- Check Perfect Number -----------------

factors sum == Number

def perfect(n):
    copy = n
    facts = []
    # calculate factors
    for i in range(1,int(n**0.5)+1):
        if n % i==0:
            facts.append(i)
            if i != n//i and n != n//i:
                facts.append(n//i)

    # sum of all factors
    sum = 0
    for value in facts:
        sum+=value

    return sum == n

print(perfect(6))


Question:22 --------------------- Check ArmStrong Number -----------------

Input : 153 ---> 1**3 + 5**3 + 3**3 == 153

def armStrong(n):
    copy = n
    count = 0

    while copy > 0:
        count+=1
        copy = copy // 10

    copy = n
    sum = 0
    while copy > 0:
        reminder = copy % 10
        sum = sum + reminder**count
        copy = copy // 10

    return sum == n

print(armStrong(153))



Question:22 --------------------- Check Strong Number -----------------

class StrongNumber:
    def __init__(self,n):
        self.n = n
    

    def factorial(self,num):
        if num < 2 :
            return 1
        
        return num * self.factorial(num-1)
    
    def calculate_strong_num(self):
        copy = self.n
        sum = 0

        while copy > 0:
            reminder = copy % 10
            sum = sum + self.factorial(reminder)
            copy = copy // 10

        return sum
    
    def is_strong(self):
        return self.n == self.calculate_strong_num()
    

num = StrongNumber(145)

print(num.calculate_strong_num())
print(num.is_strong())



Question:23 --------------------- Fibonacci Service-----------------


class Fibonacci:
    def __init__(self,step):
        self.step = step
    
    def fibonacci_service(self):
        if self.step == 0:
            return []
        
        if self.step < 2:
            return [0]
        
        seq = [0,1]

        for i in range(2,self.step):
            seq.append(seq[i-1]+seq[i-2])
        return seq
    

first = Fibonacci(5)
print(first.fibonacci_service())




Question:24 --------------------- Get Nth  Fibonacci Number -----------------


class Fibonacci:
    def __init__(self,step,n):
        self.step = step
        self.n = n
    
    def fibonacci_service(self):
        if self.step == 0:
            return []
        
        if self.step < 2:
            return [0]
        
        seq = [0,1]

        for i in range(2,self.step):
            seq.append(seq[i-1]+seq[i-2])
        return seq
    
    def get_fibonacci_num(self):
        fib = self.fibonacci_service()
        if self.n > len(fib):
            return "NO Element Found"
        return fib[self.n-1]

    

first = Fibonacci(5,3)
# print(first.fibonacci_service())
print(first.get_fibonacci_num())

    
Question:25 --------------------- Convert Decimal to Binary Number -----------------


class DecimalToBinary:
    def __init__(self,num):
        self.num = num

    def convert_decimal_to_binary(self):
        copy = self.num
        binary = 0
        place = 1

        while copy > 0:
            reminder = copy % 2
            binary = binary + place * reminder
            place = place*10
            copy = copy // 2
        
        return binary
    

first_num = DecimalToBinary(9)
print(first_num.convert_decimal_to_binary())

    
    
Question:26 --------------------- Convert Binary To Decimal Number -----------------

class BinaryToDecimal:
    def __init__(self,num):
        self.num = num
    
    def convert_binary_to_decimal(self):
        copy = self.num
        decimal = 0
        power = 1

        while copy > 0:
            reminder = copy % 10
            decimal = decimal + reminder * power
            power = 2*power
            copy = copy // 10

        return decimal
    

first_binary = BinaryToDecimal(1111)
print(first_binary.convert_binary_to_decimal())
        