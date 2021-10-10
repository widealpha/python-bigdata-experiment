def main():
    test_process_string('This is is a dark')
    return


def test_process_string(s):
    words = s.split(" ")
    result = []
    for word in words:
        if not result.__contains__(word):
            result.append(word)
    for word in result:
        print(word + ' ')


def test_function():
    print('这个程序在ex_1.py里已经有所体现了')
    return


if __name__ == '__main__':
    main()
