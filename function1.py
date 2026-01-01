
#ضرب همه اعداد یک لیست

def numbers(a):
    total=1
    for i in a:
        total*=i
        return total
    num=numbers([2,5,7])
    print(num)