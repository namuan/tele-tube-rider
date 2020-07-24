import json
import os
import time
from datetime import datetime


def datetime_from_timestamp(unix_timestamp):
    return datetime.fromtimestamp(int(unix_timestamp)).strftime("%Y-%m-%d %H:%M:%S")


def datetime_now():
    return datetime_from_timestamp(time.time())


def load_json(file_name):
    with open(file_name, "r") as json_file:
        return json.loads(json_file.read())


def save_json(file_name, data):
    with open(file_name, "w") as json_file:
        return json_file.write(json.dumps(data))


def format_size(size):
    units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])


def rename_file(old_filename, new_filename):
    full_path, filename = os.path.split(old_filename)
    filename, extension = os.path.splitext(filename)
    temp_filename = os.path.join(full_path, new_filename + extension)
    os.rename(old_filename, temp_filename)
    return temp_filename
