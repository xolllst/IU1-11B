def find_max(a):
    maxim = -10**8
    for elem in a:
        if elem > maxim:
            maxim = elem
    return maxim
len = int(input("Введите длину массива:"))
a = []
for i in range(len):
    a.append(int(input("Введите " + str(i+1) + " элемент массива:")))
print("Максимум:", find_max(a))