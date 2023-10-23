from random import randrange
 
N = 10
arr = [randrange(50) for i in range(N)]
print(arr)
 
for item in arr:
    if arr.count(item) > 1:
        print("Есть одинаковые")
        break
else:
    print("Все элементы уникальны")