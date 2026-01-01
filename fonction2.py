
#اگه عدد منفی بود متوقف بشه..اگه صفر بود چاپ نشه..اگه مثبت بود چاپ بشه
def numbers(a):
    for i in a:
        if i<0:
            break
        elif i==0:
            continue
        else:
            print(i)
            num=numbers([5,12,34,76,23,1])
            print(num)