import datetime
import time



def start_record_time(start=None):
    if start is not None:
        record_time = start
    else:
        record_time = time.time()
    return record_time

def calculate_elapsed_time(record_time=None):
    if record_time is not None:
        elapsed = time.time() - record_time
        return elapsed
    return None

def stop_record_time(record_time=None):
    if record_time is not None:
        stop_time = time.time()
        elapsed = stop_time - record_time
        return stop_time, elapsed
    return stop_time

def calculate_relative_time(target, reference):
    relative_time = target - reference
    return relative_time

def format_time(seconds):
    return datetime.datetime.fromtimestamp(time).strftime("%H:%M:%S")
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def get_current_timestamp():
    return time.time()



