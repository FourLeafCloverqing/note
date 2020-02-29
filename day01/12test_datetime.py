# 日期时间库 datetime, 和时间日期相关的都用这个

import datetime
# print('----datetime.datetime--- ')
# now_time = datetime.datetime.now()
# print(now_time.day)
# print(now_time.year)
# print(now_time.second)
# print(now_time.date())
#
# print('----datetime.date --- ')
# today_date = datetime.date.today()
# print(today_date.month)
# 获取明天的这个时间


now_time = datetime.datetime.now()
tomorrow_datetime = now_time + datetime.timedelta(days=1)
# print(tomorrow_datetime)

a = '2019-11-11 00:00:00'
# 字符串转换为时间
b = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
# print(b)


# 时间转为字符串
c = datetime.datetime.now()
d = c.strftime( '%Y-%m-%d %H:%M:%S')
print(d)



