
#میانیگن اعداد  یک لیست عدد رو بگیره ..میانگین اعداد رو حساب و چاپ کنه

def average(a):
    total=0
    count=0
    for i in a:
        total+=i
        count+=1

        return total/count
    num=average([3,6,12,65])
    print(num)
