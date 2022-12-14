"""
Solutions to module 1
Student: Rabia Bashir
Mail: rabia.bashir.9649@student.uu.se
Reviewed by:
Reviewed date:
"""

import random
import time


def power(x, n):         # Optional
    if n == 0:
        return 1
    elif n > 0:
        return x*power(x, n-1)
    else:
        return 1./power(x, -n)  # return 1./(x*power(x, n+1))


def multiply(m, n):      # Compulsory
    if n == 0 or m == 0:
        return 0
    else:
        return m + multiply(m, n-1)


def divide(t, n):        # Optional
    if t < n:
        return 0
    else:
        return 1 + divide(t-n, n)


def harmonic(n):         # Compulsory

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def digit_sum(x):        # Optional
    if x == 0:
        return 0
    return x%10 + digit_sum(int(x/10))


def get_binary(x):       # Optional
    if x < 0:
        return None
    elif x == 0:
        return ''
    else:
        return get_binary(x//2) + str(x%2)


def reverse(s):          # Optional
    pass


def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    else:
        if (a[0] > largest(a[1:])):
            return a[0]
        else:
            return largest(a[1:])


def count(x, s):         # Compulsory
    if s == []:
        return 0
        
    if s[0] == x:
        return 1 + count(x, s[1:])
    elif type(s[0]) == list:
        return count(x, s[0]) + count(x, s[1:])
    else:
        return 0 + count(x, s[1:])
    

def zippa(l1, l2):       # Compulsory

    # Base Case:
    if len(l1) <= 1 and len(l2) <= 1:
        return [l1[0], l2[0]]
    
    # Recursive Call:
    if len(l1) > len(l2):
        return [l1[0], l2[0]] + zippa(l1[1:len(l2)], l2[1:]) + l1[len(l2):]
        
    elif len(l1) < len(l2):
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:len(l1)]) + l2[len(l1):]        
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])

def bricklek(f, t, h, n): # Compulsory
    """f: source, t: target, h: auxiliary, n: tiles"""
    lst = []
    if n==1:
        # print ("Base: Move disk 1 from source", f, "to target", t)
        lst.append(f'{f}->{t}')
    else:
        lst = lst + bricklek(f, h, t, n-1)
        # print ("Move disk",n,"from source", f, "to target", t)
        lst.append(f'{f}->{t}')
        lst = lst + bricklek(h, t, f, n-1)
    return lst



####################################################    
def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    
    print("\nPower...")
    m1 = int(input("base: "))
    n1 = int(input("expo: "))
    print("Power: ", power(m1, n1))
    
    
    print("\nMultiplication...")
    m1 = int(input("m: "))
    n1 = int(input("n: "))
    print("Multiply: ", multiply(m1, n1))
    
    
    print("\nDivide...")
    t1 = int(input("t: "))
    n1 = int(input("n: "))
    print("Divide: ", divide(t1, n1))
    
    print("\nHamonic...")
    n = int(input("n: "))
    print("Hamonic: ", harmonic(n))
    
    print("\nLargest...")
    l1 = [3, 5, 9, 0, 15]
    print(l1)
    print("Larget: ", largest(l1))
    
    print("\nCount...")
    l1 = [1, 4, 2, ['a', [ [ 4 ] , 3, 4] ] ]
    print("l1 = ", l1)
    x = int(input("x: "))
    print("Count: ", count(x, l1))
    
    print("\nZippa...")
    l1 = [1, 4, 2, 7]
    l2 = [1, 4, 2]
    print("l1 = ", l1)
    print("l2 = ", l2)
    print("Zippa: \n", zippa(l1, l2))
    
    print("\nBricklek...")
    n = int(input("n: "))
    print(bricklek('f','h','t', n))
    
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  ANSWER: 
  For bricks=35, time = 1 hour 21 minutes and 43 seconds on Google Colab
  For bricks=40, my RAM crashed. so,
  Number of tiles (n) = 50
  t(n) = 2^n - 1
       = 2^50 - 1
       = 1.1258999*10^15 Sec
       = 35 678 376.9 years (which is about 35 million years)



  Exercise 17: Time for Fibonacci:
  ANSWER:
  (a): The Fibonacci algorithm is O(1.618^n), that means it grows like c*1.618^n.
       So we need to find t(n+1)/t(n) ~ 1.618
       
       On Colab, I tried n = 35, 36, 37, 38 which gives time 4.51, 7.27, 11.72 and   19.01
       respectively. The ratios are
       5
       t(36)/t(35) ~ 1.609
       t(37)/t(36) ~ 1.611
       t(38)/t(37) ~ 1.622
       
       The ratio beomes closer and closer if we move towards larger n i.e. t(101)/t(100)
       will give more accurate results.
  
  (b): For n=50, the fib(50) took approximately 1 hour and 42 minutes on Google Colab.
       For n=100: I first calculate t(35)= C.1.618^35 ;   C = 2.18740156*10^-7
                         then, t(100) = (2.18740156*10^-7)*1.618^100 
                                      = 1.728940966*10^14 sec
                                      = 5478683 years 153 days 9 hours 50.4 mintues
                                      ~ 5.4e+6 years
                                    
  
  
  Exercise 20: Comparison sorting methods:
  ANSWER:
  
  Insertion Sort: 
  t(n) = C.n^2
  C    = t(n)/n^2
       = 1/10^6
  Now, 
  For n=10^6:
  t(10^6) = (1/10^6)*(10^6)^2 
          = 1*10^6 Sec
  
  For n=10^9:    
  t(10^9) = (1/10^6)*(10^9)^2 
          = 1*10^12 Sec
  
  Merge Sort: 
  t(n) = C.nlogn
  C    = t(n)/nlogn
       = 0.00033333333
  Now,
  For n=10^6:
  t(10^6) = 0.00033333333 * (10^6*log10^6)
          = 2x10^3 Sec => 33 min, 20 sec
  
  For n= 10^9:
  t(10^9) = 0.00033333333 * (10^9*log10^9)
          = 3x10^6 Sec => 34 days, 17 hours 21 min
  Merge sort has a lower complexity than insertion sort.
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  ANSWER:
  
  For A: t(n) = C.n
  For B: t(N) = C.N.log(N)
  By given information:
  C = t(N)/N.logN
    = 0.1
  t(A) < t(B)
  n < 0.1 * n log n
  10<log n
  10^10 < n
  
  
  
  
  
  
  





"""
