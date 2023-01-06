import datetime


# def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
#     tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
#     return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)


# print(get_date(1672984650, 0))

print(tz := datetime.timezone(datetime.timedelta(seconds=7200)))
# print(datetime.timedelta(seconds=7200))
print(datetime.datetime.fromtimestamp(1672984650, tz=tz).strftime("%H:%M:%S"))

# def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
#     tz = datetime.timezone(datetime.timedelta(seconds=timezone))
#     return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)
