
#جمع اعداد زوج یک لیست

def numbers(a):
    total=0
    for i in a:
        if i%2==0:
            total+=i
            return total
        num=numbers([5,6,8,2,3,1])
        print(num)