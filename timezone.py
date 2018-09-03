from datetime import datetime
from pytz import timezone


def convert_timestamp_to_utc(dt, tz):
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    utc_dt = dt.astimezone(timezone(tz))
    return print ("Result: " + utc_dt.strftime(fmt))


mnl_time = datetime.now(timezone('Asia/Manila'))
ust_time = 'America/New_York'

convert_timestamp_to_utc(mnl_time, ust_time)


