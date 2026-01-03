
#پیدا کردن بزرگ ترین عدد لیست

def numbers(a):
    max=a[0]
    for i in a:
        if i>max:
            max=i
            return max
        result=numbers([2,5,19,65,34])
    print(result)