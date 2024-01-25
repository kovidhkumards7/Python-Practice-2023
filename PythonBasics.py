import math
import time
import re
import random
import os
import shutil
import copy
import functools


# name = "KOVIDH KUMAR D S"
# print(len(name))
# print(name.find("O"))
# print(name.lower())
# print(name.isalnum())
# print(name.isdigit())
# print(name.count("K"))
# print(name.replace("K","k"))
# print((name + "    ")*3)


# a = 15.645
# print(round(a))
# print(math.ceil(a))
# print(math.floor(a))
# print(math.sqrt(a))
# print(abs(a))
# print(pow(a,4))


# name = "KOVIDH KUMAR D S"
# Name = name.split(" ")
# slice = name[::-1]
# print(Name)
# print(slice)
# webLink = "http://google.com"
# webLink1 = "http://wikkipedia.com"
# slice = slice(7,-4)
# print(webLink[slice])
# print(webLink1[slice])
# print(webLink[7:len(webLink) - 4])


# for i in range(10,0,-1):
#     time.sleep(1)
# print("Happy new year!")


# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of coloumns: "))
# for i in range(rows):
#     for j in range(cols):
#         print("@",end=" ")
#     print()


# def mul(a, b):
#     return (a*b)
# s = mul(5,20)
# print(s)
# def name(fir, mid=" ", las=" bgfdfbvdnhgmfgy"):
#     print("Hello "+fir+" "+mid+" "+las)
# print(name(fir="hdb",mid="vgdf"))
# print(round(abs(float(input("enter decimal value")))))


# #Call by value
# def val(n):
#     n += 10
#     print(n)
# n = 10
# print(n)
# val(n)
# print(n)
# #Call by reference
# def ref(a):
#     a.append(45341)
#     print(a)
# a = [545,485.54,45]
# print(a)
# ref(a)
# print(a)


# def sm(*args):
#     s = 0
#     a = list(args)
#     a[0] = 0
#     args = tuple(a)
#     for i in args:
#         s += i
#     return s
# print(sm(5,4,8,9,6,5,4))


# def du(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
# du(grg="grgs", fgedfvg="dbsa", dcas="feuib")


# fir_name = "fcnkjsad"
# las_name = "fcnkjsad"
# print(f"Halle {fir_name} l {las_name}")


# cards = ["gvdsvb","vbds",456,4463,79,7464,1,4,45,85,45,7,98,746,4,5]
# print(random.choice(cards))
# random.shuffle(cards)
# print(cards)


# a = 4153
# b = 0
# try:
#     print(a / 4)
#     print(c)
# except ZeroDivisionError as e:
#     print("0 / err")
#     print(e)
# except NameError:
#     print("name err")
# else:
#     print(a / 5)
# finally:
#     print("err occured")


# path = "text.txt"
# if os.path.exists(path):
#     print("exist")
#     if os.path.isfile(path):
#         print("it is file")
#     elif os.path.isdir(path):
#         print("it is dirtectory")
# else:
#     print("no exist")


# try:
#     with open("jfcndewkj.txt") as f:
#         print(f.read())
#     print(f.closed)
# except FileExistsError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
# except:
#     print("err")


# with open("jfwnbfdkj.txt", "a") as f:
#     f.write("ebfcked\nygi jhb")


# src = "bcksad.txt"
# s = "ghchg"
# dest = "fkj"
# print(os.path.exists(dest))
# shutil.copy(src,dest)
# print(os.path.exists(dest))
# os.replace(src,dest)
# os.remove(src)
# try:
#     os.rmdir(s)
#     os.remove(src)
# except FileNotFoundError as e:
#     print(e)
# except FileExistsError as e:
#     print(e)


# import module as m
# m.hel()
# m.yo()
# from module import hel,yo
# hel()
# yo()


# say = print
# say("jfcasn fbsahf dasf basjk f")
# def hel(a):
#     print(a)
# hel("cscug")
# b = hel
# b("dsad")


##sort()
# stu = ["kkds","asha","dad","mom"]
# print(stu)
# stu.sort(reverse=True)
# print(stu)


##sort()
# a = [("fdj","n",48),
#      ("gf","b",15),
#      ("dc","r",74),
#      ("mh","g",58),
#      ("edrf","a",54)]
# print(a)
# a.sort()
# print(a)
# grade = lambda grades:grades[1]
# a.sort(key=grade)
# print(a)


##map() - applies func to each item in an iterables (Ex - list, tup, etc) (syntax - map(func,iterables))
# a = [("fdj","n",48),
#      ("gf","b",15),
#      ("dc","r",74),
#      ("mh","g",58),
#      ("edrf","a",54)]
# dollars_to_rup = lambda d:[d[0], d[1], d[2] * 80]
# a_dollars = list(map(dollars_to_rup, a))
# print(a_dollars)


# i = [1,5,8,9,6,41,5,8,4,58]
# squares = list(map(lambda j:j**2,i))
# print(squares)


# #filter() - creates a collection of elements from an iterable for which a func returns True (syntax - filter(func,iterable))
# a = [("fdj","n",48),
#      ("gf","b",15),
#      ("dc","r",74),
#      ("mh","g",58),
#      ("edrf","a",54)]
# b = lambda d:d[2] >= 50
# print(list(filter(b,a)))


# reduce() - apply a func 2 an iterable n reduce it to a single cumulative value, performs func on first 2 elements
# and repeats process until 1 value remains (syntax - reduce(func,iterables))
# letters = ["h","e","l","l","o"]
# word = functools.reduce(lambda a,b:a+b,letters)
# print(word)


# #zip() - aggregates elements from 2 or more iterables (list,tup,set)
# a = ("ghfd","hdfh","hgf","hfd")
# b = [4,8,5,25]
# users = dict(zip(b,a))
# print(users)


# print(time.ctime())
# print(time.time())
# print(time.gmtime())
# print(time.ctime(time.time()))
# print(time.localtime())


# def cal(v1,v2):
#     while v1 != v2:
#         if v1 > v2:
#             return cal(v1-v2,v2)
#         else:
#             return cal(v1,v2-v1)
#     return v1
# print(cal(10,55))
# print(cal(60,30))
# print(cal(27,47))
# print(cal(45,20))
# a = None
# print(a)


# def f(v):
#     if v < 1:
#         return 0
#     elif v % 2 == 0:
#         return f(v - 1)
#     else:
#         return v + f(v - 2)
# a = time.time()
# print(a)
# print(f(11))
# print(f(12))
# print(f(9))
# print(f(10))
# print(time.time())
# print(abs(float((a - time.time()))))


# def f(v1,v2):
#     try:
#         v3 = (int)(v1)
#         v2 = v3 + "A"
#         print(v2)
#     except TypeError:
#         print("T")
#     finally:
#         print("IF")
# try:
#     f("R",13)
# except ValueError:
#     print("V")
# finally:
#     print("OF")


# def f():
#     try:
#         1/0
#         return 1
#     except ZeroDivisionError:
#         "ABC"+1
#         return 2
#     finally:
#         int("A")
#         return 3
# try:
#     res = f()
#     print(res)
# except:
#     print(4)


# a = 2
# print(type(type(a)))


