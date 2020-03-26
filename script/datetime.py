import time, datetime



start_time = "2020-03-26T22:49:19.433788553+08:00"
start_time = time.strptime(start_time[:19], "%Y-%m-%dT%H:%M:%S")
#
# start_time = time.strftime("%Y-%m-%d %H:%M:%S", start_time)
print(start_time)