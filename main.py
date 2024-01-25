import itertools


# Задание 5 (dropwhile): Напишите функцию drop_less_than, которая принимает список
# целых чисел и целое число n в качестве входных данных и возвращает список целых
# чисел из входного списка, начиная с первого числа, которое не меньше n.
# Например, drop_less_than([1, 2, 3, 4, 5], 3) должна вернуть [3, 4, 5].


def drop_less_the(nums,n):
    return list(itertools.dropwhile(lambda x:x<n,nums))

print(drop_less_the([1,2,3,4,5],3))



# Задание 4 (accumulate): Напишите функцию accumulate_sums, которая принимает
# список целых чисел и возвращает список накопленных сумм.
# Например, accumulate_sums([1, 2, 3, 4, 5]) должна вернуть [1, 3, 6, 10, 15].

def accumulate_sums(nums):
    return list(itertools.accumulate(nums))

print(accumulate_sums([1,2,3,4,5]))


# Задание 3 (starmap): Напишите функцию multiply_elements, которая принимает
# список кортежей, где каждый кортеж содержит два целых числа, и возвращает список
# произведений чисел в каждом кортеже. Например, multiply_elements([(1, 2), (3, 4), (5,
# 6)]) должна вернуть [2, 12, 30].

def multiply_elements(multy_cast):
    return list(itertools.starmap(lambda x,y:x*y ,multy_cast))

print(multiply_elements([(1,3),(3,4)]))

# Задание 2 (count): Напишите функцию count_from, которая принимает целое
# число start и целое число n в качестве входных данных и возвращает список из n целых
# чисел, начиная от start. Например, count_from(5, 3) должна вернуть [5, 6, 7].

def count_from(start,n):
    return list(itertools.islice(itertools.count(start),n))

count_arr=count_from(1,10)
print(count_arr)


# Задание 1 (cycle): Напишите функцию cycle_string, которая принимает строку и целое
# число n в качестве входных данных и возвращает строку, являющуюся результатом
# повторения входной строки n раз. Например, cycle_string("abc", 3) должна
# вернуть "abcabcabc".

def cycle_string(text,n):
    new_string=''.join(itertools.islice(itertools.cycle(text),len(text)*n))
    return new_string


res=cycle_string("abc",4)
print(res)