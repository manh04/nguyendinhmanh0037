
x=int(input("Nhập số nguyên tố:"))
if x%1==0 and x%x == 0:
    print("True")
elif x%2==0:
    print("Flase")