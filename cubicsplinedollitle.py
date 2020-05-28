'''Author - MD ELIOUS ALI MONDAL
   Created - 28/5/2020'''

#approximation via cubic splines
from sined import xi
from sined import yi
ai = yi[:]
x = float(input('Enter the value of x : '))

j = 0
for i in range(len(xi)):
    if x > xi[i]:
         if x < xi[i+1]:
                j = i
         else:
                continue

def h(i):
    '''
    takes integer i and returns the width of the interval (x(i+1),x(i))
    '''
    if i < len(xi)-1:
        return xi[i+1]-xi[i]

def a(i):
    '''
    takes in integer i and returns the ith entry in the x matrix of equation
    Ax = b
    '''
    if i == 0 or i == len(xi)-1:
        return 0
    else:
        return ((3*(ai[i+1]-ai[i])) / h(i)) - ((3*(ai[i]-ai[i-1])) / h(i-1))

def l(i):
    if i == 0 or i == len(xi)-1:
        return 1
    

def mu(i):
    if i == 0 :
        return 1
    elif  i == len(xi)-1:
        return 0
    else:
        return ai[i]-((h(i-1)**2)/mu(i-1))

def z(i):
    if i == 0 or i == len(xi)-1:
        return 0
    else:
        return a(i)- ((h(i-1)*z(i-1)) / mu(i-1))

def c(j):
    '''
    takes in the value of j and returns c(jth) constant
    '''
    if j == 0 or j == len(xi)-1:
        return 0
    else:
        return z(j) - mu(j)*c(j+1)

def b(j):
    '''
    takes in the value of j and returns b(jth) constant
    '''
    return (ai[j+1] - ai[j])/h(j) - h(j)*(c(j+1)+2*c(j))/3

def d(j):
     '''
     takes in the value of j and returns d(jth) constant
     '''
     return (c(j+1)-c(j))/(3*h(j))

def S(x):
    '''
    takes the value of x znd returns the value of spline at tht point
    '''
    return ai[j] + b(j)*(x-xi[j]) + c(j)*((x-xi[j])**2) + d(j)*((x-xi[j])**3)

print('The value of y on the cubic spline formed by given data points is ',S(x))                                                
                               
