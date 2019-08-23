def log_reader(logfile):
    with open(logfile) as f:
        log = f.read()
    print(log)


if __name__ == '__main__':
    log_reader('access.log')
