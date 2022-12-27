def find_min(a):
    minimum = 10**8
    for elem in a:
        if elem < minimum:
            minimum = elem
    return minimum
len = int(input("Введите длину массива:"))
a = []
for i in range(len):
    a.append(int(input("Введите " + str(i+1) + " элемент массива:")))
print("Мнимум:", find_min(a))