import re
import sqlite3
from collections import Counter

re_ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
re_datetime_pattern = r'\[\d{1,2}/.{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4}\]'


def log_reader(logfile):
    """
    อ่านไฟล์จากชื่อที่ส่งมา แล้ว print เนื้อหาออกไป
    :param logfile: file path + file name
    """

    with open(logfile) as f:
        log = f.read()
        ip_list = re.findall(re_ip_pattern, log)
        ip_count = Counter(ip_list)

        for k, v in ip_count.items():
            print('IP Address: ' + k + ' occures ==> ' + str(v) + ' times.')

        # print(log)


def read_datetime_line_by_line(logfile):
    with open(logfile) as f:
        lines = f.readlines()
        for line in lines:
            access_date_time = re.findall(re_datetime_pattern, line)
            print(access_date_time[0])


def create_sql_line_by_line(logfile):
    with open(logfile) as f:
        lines = f.readlines()
        for line in lines:
            ip_address = re.findall(re_ip_pattern, line)
            access_date_time = re.findall(re_datetime_pattern, line)

            print('insert into access_log values (`{ip}`, `{dt}`)'.format(ip=ip_address[0], dt=access_date_time[0]))


def create_connection_db(dbname):
    try:
        conn = sqlite3.connect(dbname)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def show_total_records(conn):
    sql = 'select count(id) from access_log'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchone()

    return str(rows[0])


if __name__ == '__main__':
    # log_reader('access.log')
    # read and print line by line
    # read_datetime_line_by_line('access.log')

    # convert log to sql insert
    # create_sql_line_by_line('access.log')

    # create connection
    dbname = '/Users/worajedt/PycharmProjects/pycharmskill/log.sqlite'
    conn = create_connection_db(dbname)
    with conn:
        print('Current records BEFORE insert = ' + show_total_records(conn))

        # insert records
        # insert_log_to_table(conn)

        print('Current records AFTER insert = ' + show_total_records(conn))
