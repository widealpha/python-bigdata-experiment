"""python去除文件中空字符"""
import win32ui
import io


def main():
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir('.')  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    filename = dlg.GetPathName()  # 获取选择的文件名称
    if filename == '':
        print('没选择任何文件')
        return
    with open(filename) as in_file:
        # 防止内存溢出建立缓冲区
        x = in_file.read(10000)
        while True:
            if not x:
                return
            x = x.replace('\0', '')
            out_file = open('./result/no_blank_' + in_file.name.split('\\')[-1], mode='w')
            out_file.write(x)
            print(x)
            x = in_file.read(10000)


if __name__ == '__main__':
    main()
