## 核心程序

### 1、word-cloud-simple-version.py
这个文件会直接生成传统词云。

- 例子：


![image](http://github.com//rio26/weibo-comments-word-cloud/tree/master/source/result-from-simple-version.png)

### 2、word-cloud-v2.py
这个文件可以根据指定图像形状，生成新的词云。


- 例子：


根据这张图:

![image](http://github.com//rio26/weibo-comments-word-cloud/tree/master/source/j2.png)

![基础模板1 (2).png](http://ata2-img.cn-hangzhou.img-pub.aliyun-inc.com/82bb195ac62532963b2364d2e4da23e5.png)

生成了这样子的词云：

![image](http://github.com//rio26/weibo-comments-word-cloud/tree/master/source/result-from-v2.png)


## 运行所需文件

- 请将需要生成词云的清洗过的文本数据储存于“comment.txt”文件中。
- font_path='xxx.ttf' 是中文字体文件，此目录下提供'SourceHanSans-Bold.ttf'和'SourceHanSans-normal.ttf'两个选择，可以自由更换成其它的中文字体样式。
