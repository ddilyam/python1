# циклы

# import math
# num = int(input())
# i=1
# while i<=num:
#     print(f' Number is : {i} and cube of the {i} is :{pow(i, 3)}')
#     i=i+1
################################################################
# arr = [int(n) for n in input().split()]
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])
################################################################
# import math
# num = int(input())
# f=1
# for i in range(2, num+1):
#     f=f*i
# print(f)
################################################################
# import math
# num = int(input())
# sum=0
# for i in range(1, num+1):
#     sum=sum+i
# print(sum)
# ################################################################
# x = input('x = ')
# if x != x[::-1]:  #потому что идем от конца к началу
#     print('False')
# else:
#     print('True')
################################################################
# #вложенные циклы
# num = int(input())
# for i in range(num, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()
# ################################################################
# num = int(input())
# for i in range(num+1):
#     for j in range(i, 0, -1):
#         print(i, end='')
#     print(' ')
################################################################
#лямбда функции
# get_discount = lambda x,y: x-((x*y)/100)
# print(get_discount(1500, 50))
# ################################################################
# def sum_number(num):
#     if num == 1:
#         return True
#     return num + sum_number(num-1)
# print(sum_number(5))
################################################################
# is_triplet = lambda a, b, c: print('True') if (a*a)+(b*b) == c*c else print('False')
# is_triplet(1, 2, 3)