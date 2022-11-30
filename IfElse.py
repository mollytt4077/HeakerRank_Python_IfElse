# import math
# import os
# import random
# import re
# import sys


# def caculate():
#     if 2<n<5 and n%2==0:
#         print("Not Werid")
#     elif 6<n<20 and n%2==0:
#         print("Werid")
#     elif n>20 and n%2==0:
#         print("Not Werid")
#     else:
#         print("Werid")

# if __name__ == '__main__':
#     n = int(input("請輸入一個數字 :").strip())
#     caculate()


def caculate():
    if 1<=a<=10**10 and 1<=b<=10**10:
        print("以下為計算結果:")
        print(a,"+",b,"=",a+b)
        print(a,"-",b,"=",a-b)
        print(a,"*",b,"=",a*b)
    else:
        print("請輸入對的數字!!")

if __name__ == '__main__':
    a = int(input("請輸入第一個數字:"))
    b = int(input("請輸入第一個數字:"))
    caculate()