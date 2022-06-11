# Hometask_13_1
# Из полученного списка чисел создайте список с суммами этих чисел, отсортированными
# по возрастанию In: 965 582 023 8 695210 Out: [5, 8, 15, 20, 23]


def f(nums):
    sum_nums = []
    for i in nums:
        while nums != 0:
            last = nums % 10
            sum_nums += last
            num = nums // 10
    return sum_nums.sort()


print(f(965, 582, 23, 8, 695210))


# Hometask_13_2
# Напишите функцию f(x), которая возвращает значение следующей
# функции, определённой на всей числовой прямой:

# def f(x):
#     if x <= -2:
#         return 1 - ((x+2)**2)
#     elif - 2 < x <= 2:
#         return -x / 2
#     else:
#         return (x - 2) ** 2 + 1
#
# print(f(4.5))


# Hometask_13_3
# Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# все нечётные значения, а чётные нацело делит на два. In: 852 85 784 58 Out: [852, 784, 58]

# #вариант 1 (мой)
#
#
# def num(nums1, nums2, nums3, nums4):
#     even = []
#     number = [nums1, nums2, nums3, nums4]
#     for nums in number:
#         if nums % 2 == 0:
#             even.append(nums/2)
#     return even
#
#
# print(num(852,85,784,58))

# #вариант 2 (правильный)
#
# def f(nums):
#     even = []
#     for i in nums:
#         if nums % 2 == 0:
#             even.append(nums/2)
#     return even
#
# print(f(852,85,784,58))