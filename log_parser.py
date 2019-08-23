def log_reader(logfile):
    """
    อ่านไฟล์จากชื่อที่ส่งมา แล้ว print เนื้อหาออกไป
    :param logfile: file path + file name
    """
    with open(logfile) as f:
        log = f.read()
    print(log)


if __name__ == '__main__':
    log_reader('access.log')
