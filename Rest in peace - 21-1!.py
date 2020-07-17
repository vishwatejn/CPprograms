for _ in range(int(input())):
    n=int(input())
    s=str(n)
    if "21" in s or n%21==0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
