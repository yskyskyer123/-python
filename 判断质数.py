# author='skyu'
# -*- coding: utf-8 -*-



def checkPrime(x):

    for i in range(2, x + 1):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


if __name__=='__main__':

    x=int(raw_input())

    print 'YES\n' if checkPrime(x) else 'NO\n' #python中的 ？ ：


