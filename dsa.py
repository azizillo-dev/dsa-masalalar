# def linerSearch(arr, target):
#     if target in arr:
#         return arr.index(target)
#     else:
#         return -1
    
# arr = [1, 3 , 4, 6, 7, 8, 11, 32, 123]
# target = 8
# print(linerSearch(arr, target))


# myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

# def binarySearch(lst, target):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         medium = (low + high) // 2
#         if lst[medium] == target:
#             return medium
#         elif lst[medium] > target:
#             high = medium - 1
#         else:
#             low = medium + 1
#     return -1
# print(binarySearch(myList, 10))
        





# def large(a, b, c):
#     if a > b > c:
#         return a
#     elif b > a > c:
#         return b
#     return c
# print(large(3, 6, 9))




# n = int(input("n = "))
# def sum_juftlar(n):
#     s = 0
#     for i in range(n):
#         if i % 2 == 0:
#             s += i
#     return s
# print(sum_juftlar(n))


# word = input("word = ")
# def reverse(word):
#     return word[::-1]

# print(reverse(word))




# def linerSearch(list, target):
#     index = -1
#     for i in list:
#         index += 1
#         if i == target:
#             return f"{target} {index} - indexda topildi"
#     return -1

# myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# target = 45

# print(linerSearch(myList, target))




# def FizzBuzz(n):
#     if n % 3 == 0 and n % 5 != 0:
#         return "Fizz"
#     elif n % 3 != 0 and n % 5 == 0:
#         return "Buzz"
#     elif n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     return -1

# print(FizzBuzz(15))
# print(FizzBuzz(7))








# mylist = [5, 6,67, 76, 32, 43,  54, 43, 2324, 2,23, 32, 4345,54, 653]

# def maks(mylist):
#     max_val = mylist[0]
#     for i in mylist:
#         if i > max_val:
#             max_val = i
#     return max_val
# def minn(mylist):
#     min_val = mylist[0]
#     for i in mylist:
#         if i < min_val:
#             min_val = i
#     return min_val

# print(maks(mylist))
# print(minn(mylist))





# mevalar = ["olma", "banan", "olma", "uzum", "olma", "banan"]

# def count(list):
#     takror = {}
#     for i in mevalar:
#         if i not in takror:
#             takror[i] = 1
#         else:
#             takror[i] += 1
#     return takror

# print(count(mevalar))



# mylist = [5, 6,67, 76, 32, 43,  54,23, 4345, 653]

# def func(mylist):
#     takror = {}
#     for i in mylist:
#         if i not in takror:
#             takror[i] = 1
#         else:
#             takror[i] += 1
#     for v in  takror.values():
#         if v != 1:
#             return False
#     return True
# print(func(mylist))





# mylist = [2, 3, 5, 7, 9, 11, 45, 54]
# def two_sum(mylist, target):
#     i = 0
#     j = len(mylist) - 1
#     while i < j:
#         if mylist[i] + mylist[j] == target:
#             return f"{mylist[i]} + {mylist[j]} = {target}"
#         elif mylist[i] + mylist[j] > target:
#             j -= 1
#         else:
#             i += 1
# print(two_sum(mylist, 12))







# def two_sum_unsorted(nums, target):
#     seen = {} 
    
#     for i, num in enumerate(nums):
#         needed = target - num 
        
#         if needed in seen:
#             return [seen[needed], i]
#         seen[num] = i
        
#     return "Topilmadi"
# mylist = [11, 15, 2, 7] 
# print(two_sum_unsorted(mylist, 9)) 





# #hash map




# data = {
#    "Ali":"99890...",
#    "Vali":"99891..."
# }

# def number(name):
#     if name in data:
#         return data[name]
#     return "Bunday ism yo'q" 
# print(number("Ali")) 



# data = {
#    "Aziz":90,
#    "Ali":70
# }


# def max_val_key(data):
#     mkey = list(data.keys())[0]
#     mval = data[mkey]

#     for k, v in data.items():
#         if v > mval:
#             mval = v
#             mkey = k
#     return f"Eng katta ball: {mval}\nEgasi: {mkey}"
# print(max_val_key(data))





# def avarage_st(data):
#     return sum(data.values())/len(list(data.values()))
# print(avarage_st(data))

# def add_student(name, score):
#     if name not in data:
#         data[name] = score
#         return f"{name} qo'shildi"
#     return "Bunday key band"
# print(add_student("Azizillo", 100))
# print(data)



# def word_counter(matn):
#     sozlar = matn.split()
#     new = {}

#     for soz in sozlar:
#         if soz not in new:
#             new[soz] = 1
#         else:
#             new[soz] += 1
#     return new

# print(word_counter("apple banana apple orange banana apple"))

# nums = [1, 2, 3, 4, 2]

# # time O(n)
# # memory O(n)

# def seen(nums):
#     set_nums = set(nums)
#     for i in nums:
#         if i in set_nums:
#             return True
#     return False
# print(seen(nums))







# def first(nums):
#     seen = set(nums)
#     for i in nums:
#         if i in seen:
#             return i
#     return False

# # time O(n**2)
# # memory O(n)

# nums = [5, 1, 3, 4, 3, 5]
# print(first(nums))







# def counter(sentence):
#     new = {}
#     characters = sentence.strip()
#     for i in characters:
#         if i in new:
#             new[i] += 1
#         else:
#             new[i] = 1
#     return new
# s = " banana"
# print(counter(s))






# # s = "listen"
# # t = "silent"

# # def func(s, t):
# #     st = s.strip()
# #     ts = t.strip()
    



# nums = [2, 7, 11, 15]
# target = 9

# def two_sum(mylist, target):
#     i = 0
#     j = len(mylist) - 1
#     while i < j:
#         if mylist[i] + mylist[j] == target:
#             return f"{mylist[i]} + {mylist[j]} = {target}"
#         elif mylist[i] + mylist[j] > target:
#             j -= 1
#         else:
#             i += 1
# print(two_sum(nums, 12))
    






# def two_sum(nums, target):
#     seen = {}

#     for i, num in enumerate(nums):
#         need = target - num

#         if need in seen:
#             return [seen[need], i]
#         seen[num] = i
#     return []       

# nums = [2, 7, 11, 15]
# target = 9

# print(two_sum(nums, target))        

# nums = [2, 3, 5, 7, 9, 11]
# target = 12
        


# def taget(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while right > left:
#         if nums[left] + nums[right] == target:
#             return f"{nums[left]} + {nums[right]} = {target}"
#         elif nums[left] + nums[right] > target:
#             right -= 1
#         else:
#             left += 1
#     return

# print(taget(nums, target))




# def two_sum_sorted(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         total = nums[left] + nums[right]
#         if total == target:
#             return [left, right]
#         elif total > target:
#             right -= 1
#         else:
#             left += 1
#     return "Topilmadi"

# nums = [2, 3, 5, 7, 9, 11]
# print(two_sum_sorted(nums, 12))
        


# # takrorlangan birinchi sonni topish

# nums = [4, 2, 7, 2, 9, 4, 1]

# def takror(nums):
#     seen = {}

#     for num in nums:
#         if num in seen:
#             seen[num] += 1
#         else:
#             seen[num] = 1
#     for v, k in seen.items():
#         if k == 2:
#             return v
#             break
#     return
# print(takror(nums))




# #2. Har bir harfni sanash
# s = "banana"

# def counter(s):
#     seen = dict()  
#     harflar = s.strip()
#     for harf in harflar:
#         if harf not in seen:
#             seen[harf] = 1
#         else:
#             seen[harf] += 1
#     return seen
# print(counter(s)) 




# nums = [3, 8, 4, 7, 2]
# target = 10

# def two_sum(nums, target):
#     seen = {}

#     for index, num in enumerate(nums):
#         need = target - num
#         if need in seen:
#             return [seen[need], index]
#         seen[num] = index
#     return []
# print(two_sum(nums, target))       



# # 4. Eng ko‘p uchragan son
# nums = [1, 3, 2, 3, 4, 3, 2, 2, 2]

# def maxx(nums):
#     new = {}

#     for num in nums:
#         if num in new:
#             new[num] += 1
#         else:
#             new[num] = 1
#     key = max(new, key = new.get)
#     return key
# print(maxx(nums))




# # 5. Nollarni oxiriga surish

# nums = [0, 1, 0, 3, 12]

# def zero(nums):
#     nollar = nums.count(0)
#     for num in nums:
#         if num == 0:
#             nums.remove(num)
#     for i in range(nollar):
#         nums.append(0)
#     return nums
# print(zero(nums))
    



# # 6. Palindrome tekshirish
# s = "level"

# def isPanlindrom(s):
#     return s == s[::-1]
# print(isPanlindrom(s))










# # 7. Faqat bir marta qatnashgan sonlar


# nums = [1, 2, 2, 3, 4, 4, 5]

# def sett(nums):
#     seen = set()



# 8. Ikkinchi eng katta unikal son


# nums = [10, 5, 8, 20, 20, 3]

# def second_max(nums):






# n = int(input())
# s = input()

# if len(s) > n:
#     s = s[len(s)-n:]
# elif len(s) < n:
#     s = "." * (n - len(s)) + s

# print(s)







# C++ exe dasturdagi masalalae
# 13.06.2026


# # integer1
# l = int(input("L : "))
# print(f"{l} sm = {l/100} m")


# # 2
# m = int(input("m : "))
# print(f"{m} kg = {m/1000} t")


# # 3
# m = int(input("m : "))
# print(f"{m} bayt = {m//1024} kb")



# 4
# a = int(input("a : "))
# b = int(input("b : "))
# print(a//b)
# time: O(1)
# memory: O(1)




# 5
# a = int(input("a : "))
# b = int(input("b : "))
# n = a // b
# c = a - b * n
# print(f"Joylashishlar soni: {n}")
# print(f"Ortiqcha qism: {c}")
# time: O(1)
# memory: O(1)



# # 6
# n = int(input("2 xonali son kiriting: "))
# print(f"O'nlar xonasi: {n // 10}")
# print(f"Birlar xonasi: {n % 10}")
# time: O(1)
# memory: O(1)


# 7
# n = int(input("2 xonali son kiriting: "))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)
# time: O(log n)
# memory: O(1)

    


# # 8
# n = int(input("2 xonali son kiriting: "))
# print(int(str(n)[::-1]))
# # time: O(n)
# # memory: O(n)

# teskari = 0
# while n > 0:
#     teskari = teskari * 10 + n % 10
#     n //= 10
# print(teskari)
# # time: O(n)
# # memory: O(1)



# # 9
# n = int(input("3 xonali son: "))
# print(f"100 lar xonasidagi son: {n//100}")
# # time: O(1)
# # memory: O(1)



# # 10
# n = int(input("3 xonali: "))
# bir = n % 10
# on = (n // 10) % 10
# print(f"Birlar xonasi: {bir}")
# print(f"O'nlar xonasi: {on}")
# time: O(1)
# memory: O(1)



# print(f"Birlar: {str(n)[-1]}")
# print(f"O'nlar: {str(n)[1:2]}")
# # time: O(n)
# # memory: O(n)



# # 11
# a = int(input("3 xonali: "))
# s = 0

# while a > 0:
#     s += a % 10
#     a //= 10
# print(s)

# # time: O(n)
# # memory: O(1)




# # 12
# a = int(input("3 xonali: "))
# print(int(str(a)[::-1]))
# # time: O(n)
# # memory: O(n)

# teskari = 0
# while a > 0:
#     teskari = teskari * 10 + a % 10
#     a //= 10
# print(teskari)
# # time: O(n)
# # memory: O(1)



# 13
# a = int(input("3 xonali: "))
# b = str(a)[1:] + str(a)[0]
# print(int(b))
# # time: O(n)
# # memory: O(n)


# c = a // 100
# b = a % 100
# d = b * 10 + c
# print(d)
# # time: O(1)
# # memory: O(1)



# # 15
# a = int(input("3 xonali: "))
# yuz = a // 100
# on = (a // 10) % 10
# new = on * 100 + yuz * 10 + a % 10
# print(new)
# # time: O(1)
# # Memory: O(1)




# # 17
# n = int(input())
# print((n // 100) % 10)
# # time: O(1)
# # Memory: O(1)




# # 19
# N = int(input())
# minut = N // 60
# print(minut)
# # time: O(1)
# # Memory: O(1)




# # 20
# N = int(input())
# soat = N // 3600
# print(soat)
# # time: O(1)
# # Memory: O(1)




# # 21
# N = int(input())
# minut = N // 60
# sekund = N % 60
# print(f"{minut} minut va {sekund} sekund")
# # time: O(1)
# # Memory: O(1)




# # 22
# N = int(input())
# soat = N // 3600
# sekund = N % 3600
# print(f"{soat} soat va {sekund} sekund")
# # time: O(1)
# # Memory: O(1)




# # 23
# n = int(input("n : "))
# soat = n // 3600
# minut = (n % 3600) // 60
# sekund = n % 60
# print(f"{soat} soat, {minut} minut va {sekund} sekund")
# # time: O(1)
# # Memory: O(1)



# 24
# hafta_kunlari = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
# kun = int(input("Kun raqamini kiriting: "))
# print(hafta_kunlari[kun % 7])



# # 25
# k = int(input("Kun raqamini kiriting: "))
# print(hafta_kunlari[(k + 3) % 7])




# 26
# hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# kun = int(input("Kun raqamini kiriting: "))
# print(hafta_kunlari[(kun + 5) % 7])








# bool ga oid masalalar
# bool ga oid masalalar
# bool ga oid masalalar
# bool ga oid masalalar
# bool ga oid masalalar
# bool ga oid masalalar

# # 1
# def is_musbat(a):
#     return a > 0
# print(is_musbat(-4))





# # 2
# def is_toq(a):
#     return a % 2 ==1
# print(is_toq(7))





# 3
# def is_juft(a):
#     return a % 2 ==0
# print(is_juft(7))




# # 4
# def func(a, b):
#     return a > 2 and b <= 3
# print(func(3, 2))




# # 5
# def func(a, b):
#     return a > 0 or b < -2
# print(func(-1, -3))




# # 6
# def func(a, b, c):
#     return a <= b and b <= c
# print(func(1, 2, 3)) 





# # 7
# def func(a, b, c):
#     return a > b and b < c
# print(func(3, 2, 4))





# # 8
# def toqmi(a, b):
#     return a % 2 == 1 and b % 2 == 1
# print()





# # 9
# def toqmi(a, b):
#     return a % 2 == 0 or b % 2 == 0



# # 10
# def func(a, b):
#     return (a % 2 == 1 and b % 2 != 1) or (a % 2 != 1 and b % 2 == 1)
# print(func(5, 5))




# # 11
# def func(a, b):
#     return (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0)
# print(func(5, 2))



# # 12
# def func(a, b, c):
#     return a > 0 and b > 0 and c > 0
# print(func(5, 2, -2))




# # 13
# def func(a, b, c):
#     return a > 0 or b > 0 or c > 0
# print(func(-4, -5, -6))



# # 14
# def func(a, b, c):
#     return a > 0 and (b < 0 and c < 0) or b > 0 and (a < 0 and c < 0) or c > 0 and (b < 0 and a < 0)
# print(func(3, -3, -4))




# # 15
# def func(a, b, c):
#     return (a > 0 and b > 0 and c < 0) or (b > 0 and c > 0 and a < 0) or (a > 0 and c > 0 and b < 0)
# print(func(3, 3, -4))




# # 16
# def func(a):
#     return a % 2 == 0 and len(str(a)) == 2
# print(func(32))



# # 17
# def func(a):
#     return a % 2 == 1 and len(str(a)) == 3
# print(func(432))




# # 18
# def func(a, b, c):
#     return (a == b and b != c) or (a == c and a != b) or (b == c and b != a) or (a == b and b == c)
# print(func(2, 1, 3))





# # 19
# def func(a, b, c):
#     return (a == -b) or (a == -c) or (b == -c) or (a == -b and -c)
# print(func(-2, -2, -2))





# # 20
# def diff(a):
#     x, y, z = a % 10, (a // 10) % 10, a // 100
#     return x != y != z
# print(diff(322))
# # Time: O(n)
# # Memory: O(1)




# 21
# a = int(input())
# yuz = a // 100
# on = (a // 10) % 10
# bir = a % 10
# print(yuz < on < bir)
# # Time: O(1)
# # Memory: O(1)




# # 22
# a = int(input())
# yuz = a // 100
# on = (a // 10) % 10
# bir = a % 10
# print(yuz < on < bir or yuz > on > bir)
# # Time: O(1)
# # Memory: O(1)





# # 23
# def func(a):
#     return str(a) == str(a)[::-1]
# print(func(121))
# # Time: O(n)
# # Memory: O(n)

# def func(a):
#     yuz = a // 100
#     bir = a % 10
#     return yuz == bir
# print(func(121))
# # Time: O(1)
# # Memory: O(1)




# # 24
# def func(a, b, c):
#     d = b**2 - 4*a*c
#     if d >= 0:
#         return True
#     return False
# print(func(1, -4, 4))




# # 25
# def func(x, y):
#     return x < 0 and y > 0
# print(func(-3, 4))


# s = ["H","a","n","n","a","h"]

# def reverseString(s):
#     new = []
#     i = len(s) - 1
#     while i >= 0:
#         new.append(s[i])
#         i -= 1
#     return new

# print(reverseString(s))






# # 26
# def func(x , y):
#     return x > 0 and y < 0
# print(func(3, -4))



# # 27
# def func(x, y):
#     return (x < 0 and y > 0) or (x < 0 and y < 0)
# print(func(1, 2))
# print(func(1, -2))
# print(func(-1, -2))




# # 29
# def func(x, y, x1, y1, x2, y2):
#     return x > x1 and x < x2 and y > y2 and y < y1
# print(func(1, 2, 3,2, 4,5))
    



# # 30
# def func(a, b, c):
#     return a == b == c
# print(func(3, 2, 3))



# # 31
# def func(a, b, c):
#     return a == b and a != c or a == c and a != b or b == c and b != a
# print(func(3, 2, 1))



# # 32
# def func(a, b, c):
#     return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2
# print(func(3, 4, 5))


# # 33
# def func(a, b, c):
#     return a + b > c and b + c > a and a + c > b
# print(func(3, 2, 1))





# # 34
# def func(x, y):
#     if x == y:
#         return False
#     elif x % 2 == 0 and y % 2 != 0 or y % 2 == 0 and x % 2 != 0:
#         return True
#     return False
# print(func(4, 5))



# # 35
# def func(x, y, x1, y1):
#     return (x + y) % 2 == (x1 + y1) % 2
# print(func(3, 4, 8, 7))



# # 36
# def func(x, y, x1, y1):
#     if x == x1 or y == y1:
#         return True
#     return False
# print(func(1, 1, 1, 7))





# # 37
# def func(x1, y1, x2, y2):
#     return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1





# # 38
# def func(x1, y1, x2, y2):
#     return abs(x1-x2)==abs(y1-y2)
# print(func(3,5,5,7))




# # 39
# def boolean39(x1, y1, x2, y2):
#     k = (x1 == x2) or (y1 == y2)
#     diagonal = abs(x1 - x2) == abs(y1 - y2)
    
#     return k or diagonal

# print(boolean39(4, 4, 4, 8)) 
# print(boolean39(4, 4, 1, 7))  




# 40
# def boolean40(x1, y1, x2, y2):
#     dx = abs(x1 - x2)
#     dy = abs(y1 - y2)
#     return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
# print(boolean40(4, 4, 5, 6))










#######################################################################################
#                                                                                     #
#                         shart opertoriga oid 30 ta masala                           #
#                                                                                     #
#######################################################################################

# # 1
# def if1(a):
#     x = a + 1 if a > 0 else a
#     return x
# print(if1(5))


# # 2
# def if2(a):
#     x = a + 1 if a > 0 else a -2
#     return x
# print(if2(5))



# # 3
# def if3(a):
#     x = a + 1 if a > 0 else (a - 2 if a < 0 else 2)
#     return x
# print(if3(3))





# # 4
# def if4(data):
#     s = 0
#     for i in data:
#         if i > 0:
#             s += 1
#     return s
# print(if4([1, -3, -4]))





# 5
# def if9(a, b):
#     if b > a:
#         a, b = b, a
#     return f"a = {a} b = {b}"
# print(if9(3, 4))
# print(if9(5, 3))


# # 6
# def if10(a, b):
#     if a != b:
#         a = b = a + b
#     else:
#         a = b = 0
#     return a, b
# print(if10(5, 3))
# print(if10(5, 5))




# # 7
# def if11(a, b):
#     if a != b:
#         if a > b:
#             a = b = a
#         b = a = b
#     else:
#         a = b = 0
#     return a, b
# print(if11(5, 3))
# print(if11(1, 1))




# # 8
# def if12(a, b, c):
#     if a > b > c:
#         return f"Eng kattasi a = {a}"
#     elif b > a > c:
#         return f"b = {b}"
#     else:
#         return f"c = {c}"
# print(if12(3, 5, 2))




# # 9
# def if13(a, b, c):
#     if a > b and a < c:
#         return a
#     elif b > a and b < c:
#         return b
#     else:
#         return c
# print(if13(78, 6, 4))





# # 10
# def if14(a, b, c):
#     if a > b > c:
#         return a, b
#     elif b > a > c:
#         return b, a
#     elif b > c > a:
#         return b, c
#     elif a > c > b:
#         return a, c
#     elif c > a > b:
#         return c, a
#     elif c > b > a:
#         return c, b
# print(if14(18, 118, 54))





# # 11
# def if15(a, b, c):
#     if a > b > c:
#         return a + b
#     elif b > c > a:
#         return b + c
#     elif c > a > b:
#         return c + a
# print(if15(218, 118, 254))  







# # 12
# def if16(a, b, c):
#     if a < b < c:
#         return a *2, b*2, c*2
#     else:
#         return -a, -b, -c
# print(if16(3, 5, 8))
# print(if16(3, 5, 2))





# # 13
# def if17(a, b, c):
#     return (a*2, b*2, c*2) if (a > b > c or c > b > a) else (-a, -b, -c)
# print(if17(8, 4, 1))
        



# # 14
# def if18(a, b, c):
#     if a == b != c:
#         return int(3)
#     elif b == c != a:
#         return int(1)
#     elif a == c != b:
#         return int(2)
# print(if18(3, 4, 3))


# # 15
# def if19(a, b, c, d):
#     if a == b == c != d:
#         return 4
#     elif a == b == d != c:
#         return 3
#     elif a == d == c != b:
#         return 2
#     else:
#         return 1
# print(if19(2, 2, 3, 2))



# # 16
# def if20(A, B, C):
#     if abs(A - B) < abs(A - C):
#         print("B", abs(A - B))
#     else:
#         print("C", abs(A - C))

# if20(2, 4, 5)





# # 17
# def if21(x, y):
#     if x == y == 0:
#         return 0
#     elif x == 0 and y != 0:
#         return 2
#     elif y == 0 and x != 0:
#         return 1
#     else:
#         return 3
# print(if21(0, 3))




# # 18
# def if22(x, y):
#     if x > 0 and 0 < y:
#         return 1
#     elif x > 0 and 0 > y:
#         return 4
#     elif y > 0 and x < 0:
#         return 2
#     elif x < 0 and 0 > y:
#         return 3
#     else:
#         return "Kordinata o'qida yotmasligi kerak"

# print(if22(-2, 12))










                             ####################################################
                             #                                                  # 
                             #  19.07.2026 if davomi va tanlashga oidlar        #
                             #                                                  #
                             ####################################################                                                        



# # 20
# import math

# def if24(x):
#     if x > 0:
#         fx = 2 * math.sin(x)
#     else:
#         fx = x - 6
#     return fx
# print(if24(-1))





# # 21
# def if25(x):
#     if x > 2 and x < -2:
#         fx = 2 * x
#     else:
#         fx = -3 * x
#     return fx
# print(if25(3))



# # 22
# def if26(x):
#     if x <= 0:
#         fx = -x
#     elif x > 0 and x < 2:
#         fx = x**2
#     else:
#         fx = 4
#     return fx
# print(if26(2))




# # 23
# import math
# def if27(x):
#     if x < 0:
#         fx = 0
#     elif math.floor(x) % 2 == 0:
#         fx = 1
#     elif math.floor(x) % 2 == 1:
#         fx = -1

#     return fx

# print(if27(4.2))





# # 24
# def if28(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return 366
#     return 365
# print(if28(2020)) 




# # 25
# def if29(x):
#     if x % 2 == 0 and x > 0:
#         return "Musbat juft son"
#     elif x % 2 == 0 and x < 0:
#         return "Manfiy juft son"
#     elif x % 2 != 0 and x > 0:
#         return "Musbat toq son"
#     elif x % 2 != 0 and x < 0:
#         return "Manfiy toq son"
#     return "Nol"
# print(if29(-3))




# # 26
# def if30(x):
#     if len(str(x)) == int(1):
#         return "1 xonali juft" if x % 2 == 0 else "1 xonali toq"
#     elif len(str(x)) == 2:
#         return "2 xonali juft" if x % 2 == 0 else "2 xonali toq"
#     else:
#         return "3 xonali juft" if x % 2 == 0 else "3 xonali toq"
# print(if30(34))


















