
#ضرب اعداد یک لیست

def numbers(a):
    total=1
    for i in a:
        total*=a
        return total
    num=numbers([3,6,9,10,2,1])   
    print(num)  