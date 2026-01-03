
#جمع اعداد زوج یک لیست

def numbers(a):
    total=0
    for i in a:
     if i%2==0:
            total+=i
            return total
    result=numbers([2,5,4,8,10,3])
    print(result)