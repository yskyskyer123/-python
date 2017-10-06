# author='skyu'
# -*- coding: utf-8 -*-

maxn=50
Fib=[]

def preCope():
    Fib.append(0)   #Fib[0]=0 IndexError: list assignment index out of range
    Fib.append(1)
    for i in range(2,51):
        Fib.append(Fib[i-2]+Fib[i-1])


if __name__=='__main__':

    preCope()
    while True:
        try:
            x=int(raw_input().strip())
            print Fib[x]
        except EOFError:
            break



