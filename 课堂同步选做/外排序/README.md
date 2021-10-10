# Python 第三次作业 2021.3.23

## 准备工作

1. 安装所需要的库

   ```shell
   pip install pywin32
   ```

2. 一个windows 7以上的windows系统(有些程序用到了windows api)

3. 所有的样例输入放在./example下，输出对应在./result下





## Python 去除文件中的‘\0’字符

### 介绍

free_space.py的main允许选择文件(filename)并去除其中的‘\0’字符(0x00)，生成文件写入./result/no_blank_filename

用python文件输入流，O(n)复杂度，设置10000缓冲字符

### 运行

调用free_space.py的main函数

## python归并排序

### 介绍

merge_sort.py的main函数用以操作归并排序文件，文件必须以按行形式给出并且不能有不合规范的行

按照字母升序排列，输入文件放在./example/a.txt，结果输出至./result/sorted.txt

### 分析

首先以main()函数开始

接着调用split_file()方法进行文件的拆分，并在拆分过程中进行一次排序，这次排序的时间复杂度为nlogn

接着调用merge()及进行归并，归并过程中时间复杂度为nlogn

最终时间复杂度为O(nlogn)

实测速度很慢，100000的文件要将近1分钟，问题原因一部分是频繁的文件读写，另一部分是python自身较慢，优化起来都很困难，python应该并不适合做大数据量的排序工作，更适合做一个胶水语言

## TextAct使用

### 安装

```shell
pip install textract
```

我在安装之后尝试使用的时候报错

> AttributeError: module 'textract' has no attribute 'process'

然后发现了，我的文件名起成的textract.py与它本身的文件夹冲突

### 使用

按照官网的教程直接使用尝试

```python
 text = textract.process("../QQ群2012使用教程.docx", extension='docx')
 print(text)
```

发现输出的是一行似乎有什么规律的16进制串，里面夹杂着英文

```
b'\xe4\xbd\xbf\xe7\x94\xa8DataGrip\xe5\x9b\xbe....'
```

经过一番摸索发现，类似UTF-8的编码，所以用UTF-8解码字符串

```python
text = textract.process("../QQ群2012使用教程.docx", extension='docx')
print(text.decode('UTF-8'))
```

解码之后显示出了正常的结果

![image-20210405235346047](https://gitee.com/widealpha/pic/raw/master/image-20210405235346047.png)

jpg等图像格式类似，不过需要指明language

```
text = textract.process(r'../p4-test1.jpg', language='cn')
print(text.decode('UTF-8'))
```

> 如果文件名有后缀是可以省略extension选项的

> 如果尝试使用图像识别，需要额外安装tesseract