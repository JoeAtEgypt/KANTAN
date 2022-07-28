def calculate_time_diff(creation_time):
    import datetime as dt
    from datetime import datetime

    expiration_time = datetime.now()
    creation_datetime = dt.datetime(
        creation_time.year,
        creation_time.month,
        creation_time.day,
        creation_time.hour,
        creation_time.minute,
        creation_time.second,
    )
    expiration_datetime = dt.datetime(
        expiration_time.year,
        expiration_time.month,
        expiration_time.day,
        expiration_time.hour,
        expiration_time.minute,
        expiration_time.second,
    )
    return (expiration_datetime - creation_datetime).total_seconds()