# -*-coding: utf-8-*-
import time


# 日期转时间戳
def datetime2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))

# 完整日期转时间戳
def date2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))

# 时间戳转成各种时间格式
def ts2datetime_full(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ts))

def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))


if __name__ == '__main__':
	# result = datetime2ts('2019-06-21')             # 1561046400
	# result = date2ts('2019-06-21 21:22:23')        # 1561123343
	#result = ts2datetime_full(1561123343)           # 2019-06-21 21:22:23
	result = ts2datetime(1561123343)                 # 2019-06-21          
	print(result) 