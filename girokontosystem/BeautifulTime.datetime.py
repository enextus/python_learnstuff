import BeautifulTime

date_str = '2016-10-30 12:30:30'
dt = BeautifulTime.str2datetime(date_str)
# with a custom format
dt = BeautifulTime.str2datetime(date_str, format='%Y-%m-%d %H:%M:%S')
t = BeautifulTime.str2time(date_str)
ts = BeautifulTime.str2timestamp(date_str)

print(dt, t, ts )

dt = BeautifulTime.str2datetime(date_str)
t = BeautifulTime.str2time(date_str)
ts = BeautifulTime.str2timestamp(date_str)

print(dt, t, ts )

s = BeautifulTime.datetime2str(dt)
t = BeautifulTime.datetime2time(dt)
ts = BeautifulTime.datetime2timestamp(dt)

print(s, t, ts )

s = BeautifulTime.time2str(t)
dt = BeautifulTime.time2datetime(t)
ts = BeautifulTime.time2timestamp(t)

print(s, dt, ts )

dt = BeautifulTime.timestamp2datetime(ts)
t = BeautifulTime.timestamp2time(ts)
s = BeautifulTime.timestamp2str(ts)

print(dt, t, s )