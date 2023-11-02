for i in range(10):
    for j in range(i+1):
        print('*', end='')
        print()

        total=0

for i in range(1,20,2):
    total+=1
print("1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19", total)

numbers=(951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263)

a=0
while a < len (numbers):
    if numbers [a] % 2!=0:
      print(numbers [a],end=" ")
    if numbers [a] == 553:
       break
    a+=1





