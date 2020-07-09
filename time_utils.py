import time
import datetime


def get_timeout_line():
    now_timestamps = int(time.mktime(datetime.now().timetuple()))
    target_timestamps = now_timestamps - (3 * 24 * 60 * 60)
    target_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(target_timestamps))

# 时间有三种展现方式 时间戳、时间元祖、格式化的时间
print(time.time())  # 当前时间戳
print(int(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S')) #格式化的时间
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%H:%M:%S'))

print(time.gmtime()) #获取标准时区的时间元组，如果传入了时间戳，就是把时间戳转换成时间元组
print(time.gmtime(1516194265))


# datetime常用方法
now_time = datetime.datetime.now() #获取当前格式化的时间
d1 = now_time - datetime.timedelta(hours=1) #获取前一小时
d2 = now_time - datetime.timedelta(days=1) #获取前一天

print(now_time)
print(d1)
print(d2)


# 四、时间戳和字符串的互相转化
# 字符串格式化时间转换时间戳
str_time = '2018-1-17'
print(time.mktime(time.strptime(str_time,'%Y-%m-%d')))

# 时间戳转换成格式化的时间字符串
gsh_time= time.time()
print(time.strftime('%Y-%m-%d',time.localtime(gsh_time)))

# datetime对象转换成时间戳
dt = datetime.datetime.now()
print(time.mktime(dt.timetuple()))

# 时间戳转换成datetime对象
sjc_time = time.time()
print(datetime.datetime.fromtimestamp(sjc_time))
