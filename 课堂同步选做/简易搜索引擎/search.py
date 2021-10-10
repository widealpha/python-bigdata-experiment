"""词语搜索程序"""


def main():
    word_map = {}
    init(word_map)
    search(word_map)
    return


def init(word_map):
    filename = './a.txt'
    in_file = open(filename)
    line = in_file.readline()
    line_count = 1
    while len(line) != 0:
        words = line.split(' ')
        place_count = 0
        for word in words:
            if word not in word_map:
                word_map[word] = []
            place_list = word_map[word]
            place_list.append(filename + ':' + str(line_count) + ':' + str(place_count))
            place_count += (len(word) + 1)
            line_count += 1
        line = in_file.readline()
    in_file.close()


def search(word_map):
    key = input('请输入关键字:')
    if key in word_map:
        print('位置在:' + str(word_map[key]))
    else:
        print('词语不存在\n')


if __name__ == '__main__':
    main()
