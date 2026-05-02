import datetime

def get_time():
    now = datetime.datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    am_pm = now.strftime("%p")
    return f"Sir, the time is {hour}:{minute} {am_pm}"

def get_date():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    date = now.strftime("%d")
    month = now.strftime("%B")
    year = now.strftime("%Y")
    return f"Today is {day}, {date} {month} {year}"

def get_day():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    return f"Today is {day}, Sir"

def get_datetime():
    return f"{get_date()}. {get_time()}"