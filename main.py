# Создать генератор списка из исходного, который:
# 1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}
arr=[1,2,3,4,5,6,7]
newarr={x:x**3 for x in arr if x%2!=0}

print(newarr)

# 2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}

arr=[1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
newarr={x for x in arr if x%2==0 }
print(newarr)
# 3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного
arr=[x*10 for x in range(10) ]
print(arr)
# 4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
def devisibleBy7(list):
    for i in list:
        if i%7==0:
            yield i
n = int(input("Enter n:"))
arr=[x for x in range(n)]
for i in devisibleBy7(arr):
    print(i)
