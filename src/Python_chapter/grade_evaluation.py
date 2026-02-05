def Evaluation(grade):
    if grade < 10:
        out = "نیاز به تلاش بیشتر"
    elif (grade >= 10 and grade <=13):
        out = "قابل قبول"
    elif (grade>13 and grade<=17):   #اینجا بین ۱۳ تا ۱۴ تعریف نشده بود منم تعریفش کردم
        out = "خوب"
    elif (grade > 17):
        out = "عالی"
    return out[::-1]


def main():
    while(True):
        grade = input('Please enter your grade or type done:')
        if grade!='done':
            print(Evaluation(int(grade)))
        else:
            break
    


if __name__ == "__main__":
   main()