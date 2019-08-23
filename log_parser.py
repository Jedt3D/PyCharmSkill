import re
from collections import Counter


def log_reader(logfile):
    """
    อ่านไฟล์จากชื่อที่ส่งมา แล้ว print เนื้อหาออกไป
    :param logfile: file path + file name
    """
    re_ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        ip_list = re.findall(re_ip_pattern, log)
        ip_count = Counter(ip_list)

        for k, v in ip_count.items():
            print('IP Address: ' + k + ' occures ==> ' + str(v) + ' times.')

        # print(log)


if __name__ == '__main__':
    log_reader('access.log')
