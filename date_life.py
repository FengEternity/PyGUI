import datetime
import random
import pytz


def fun_choose(number):
    '''
    fun : 选择所需功能
    '''
    if number == 1:
        date_now = datetime.datetime.now()
        print(date_now)
        internet_connect(date_now.weekday()+1, date_now.hour, date_now.minute)
    elif number == 2:
        trip_mode()
    elif number == 3:
        choose_meal()
    elif number == 4:
        run()
    elif number == 5:
        class_detect()


def internet_connect(week, hour, min):
    '''
    fun ：判断校园网连接时间
    return : True or False
    '''
    if week >= 6 and week <= 7:
        print("今天不断网啦！")
        return False
    else:
        if hour >= 23 and min >= 30:
            print("So Sorry…断网啦!")
            return False
        elif hour <= 7:
            print("So Sorry…断网啦!")
            return False
        else:
            print("好耶！可以使用校园网啦！")
            return True


def trip_mode():
    '''
    fun : 选择出行方式
    return : 选择项
    '''
    ch_1 = input("请问你有车吗(t or f):")
    ch_2 = input("请问共享单车多吗(yes or no):")
    if ch_1 == 't':
        print("你可以选择骑车，当然步行也是一个不错的选择")
    else:
        if ch_2 == 'yes':
            print("你可以选择共享单车，当然步行也是一个不错的选择")
        else:
            print("共享单车不多啦，快冲啊……")


def choose_meal():
    '''
    fun : 随机选择饭菜
    '''
    choice = random.choice(["鲜约水饺", "咖哩饭", "咖喱法式牛排饭", "牛肉汤", "馋嘴鱼", "水煮肉片"])
    print(choice)


def run():
    rain_str = input("今天下雨了吗(yes or no):")
    if rain_str == 'yes':
        print("太遗憾啦，你失去了一个强身健体的机会……")
    elif rain_str == 'no':
        print(" 这又是一个跑操次数++的机会")


def class_detect():

    class_start_1 = pytz.utc.localize(datetime.time(8, 00))
    class_end_1 = pytz.utc.localize(datetime.time(11, 35))
    class_start_2 = pytz.utc.localize(datetime.time(13, 45))
    class_end_2 = pytz.utc.localize(datetime.time(17, 15))    
    study_start = pytz.utc.localize(datetime.time(18,30))
    study_end = pytz.utc.localize(datetime.time(21,00))

    cur = pytz.utc.localize(datetime.datetime.utcnow().time())
    if cur >= class_start_1 and cur <= class_end_1:
        print("如果没猜错现在是上课时间吧……\n抓到一只摸鱼的小柚子")
    elif cur >= class_start_2 and cur <= class_end_2:
        print("如果没猜错现在是上课时间吧……\n抓到一只摸鱼的小柚子")
    elif cur >= study_start and cur <= study_end:
        print("如果没猜错现在是上课时间吧……\n抓到一只摸鱼的小柚子")    
    else:
        print("你没有触发神秘事件\n好好休息吧~~~")


if __name__ == "__main__":
    print("1 校园网\n2 出行\n3 随机选择饭菜\n4 跑操\n5 这是一个神奇的选项")
    number = int(input("请输入你的选择："))
    fun_choose(number)
