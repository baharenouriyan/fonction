
#پیدا کردن بزرگ ترین عدد لیست
def numbers(a):
    max=a[0]
    for i in a:
        if i>max:
            max=i
            return max
        b=numbers([2,5,8,1,12])
        print(numbers)