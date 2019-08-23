def hello(name: str, times: int) -> str:
    """
    พิมพ์ชื่อ ตามจำนวนครั้งที่กำหนด
    :param name: Name of the subject
    :param times: Times of printing
    """
    for i in range(times):
        print(name)


if __name__ == '__main__':
    hello('Worajedt', 3)
