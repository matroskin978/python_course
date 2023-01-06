import datetime


def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)


print(get_date(1672984650, 0))
