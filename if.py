a = int( input())
if (a>100):
    print("Больше ста")
elif (50<a<100):
    print("Между пятьюдесятью и сотней")
else: print("Меньше пятидесяти")
b = 101 if a> 50 else 102
print("Если b равно 101, то a ,больше 50. Иначе b=102")
print("b = ")
print(b)
