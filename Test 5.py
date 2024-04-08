fruits = ["apple", "banana", "cherry", "pipa", "Xrry", "Test", "Tetu", "TaTa", "Atatat"]

count_a = 0

for element in fruits:
    count_a += element.count('a')
    count_a += element.count('A')
print(count_a)