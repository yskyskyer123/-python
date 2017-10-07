# author='skyu'
# -*- coding: utf-8 -*-



while True:
    try:
        a,b,c=map(int,raw_input().strip().split())
        print a+b+c
    except EOFError:
        break

'''
ctrl+D  表示EOF
'''