
#تعداد عدد زوج و فرد

def numbers(a):
    even=0
    odd=0
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
            return even,odd
        num=numbers([10,4,3,1,7,6,2])
        print(num)
