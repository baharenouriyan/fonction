
#شمارش اعداد مثبت ..یه لیست بگیره. و بشماره چند تا عدد مثبت داخلشه و و تعدادش رو  چاپ کنه

def numbers(a):
    total=0
    for i in a:
        if i>0:
            total+=1
            return total
        num=numbers([4,3,-9,1,-5,-10])
        print(num)