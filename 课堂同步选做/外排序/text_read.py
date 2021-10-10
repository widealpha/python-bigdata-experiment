import textract


def main():
    text = textract.process("../QQ群2012使用教程.docx", extension='docx', encoding='UTF-8')
    print(text.decode('UTF-8'))
    text = textract.process(r'../p4-test1.jpg', language='cn')
    print(text.decode('UTF-8'))
    return


if __name__ == '__main__':
    main()
