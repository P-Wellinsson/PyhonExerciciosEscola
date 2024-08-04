from funções.erros import *
# Ainda bem que temos o sort e sorted.
nums1 = []
nums2 = []
num = []
for i in range(5):
    n = LeiaInt(f'Digite o {i+1}º número da 1ª lista: ')
    nums1.append(n)
    if i == 0 or n > num[-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                break
            pos += 1
print('-' * 40)

for i in range(5):
    n = LeiaInt(f'Digite o {i+1}º número da 2ª lista: ')
    nums2.append(n)
    if n > num[-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                break
            pos += 1
print('-' * 40)
print(num)
