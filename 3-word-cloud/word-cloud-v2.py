# - * - coding: utf - 8 -*-
#
# Author: Rio Kunn
# Date: Jun 30, 2018 
#
# This file genereates a Chinese word cloud in the shape you wish.


from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image

# open the file with "read" attribute
with open('comment.txt', 'r') as f:
    f_text = f.read()           #read file
    res = jieba.cut(f_text)     #split chinese characters using jieba package
    res_text = ' '.join(res)
    background_img = plt.imread('J.jpeg')           #read image that you wish to input in the word cloud
    j_coloring = np.array(Image.open("j2.png"))     #handle the image you just read
    STOPWORDS.add('via')                            #add stop words

    #generate the word cloud
    wc = WordCloud(background_color="white", mask=j_coloring,stopwords=STOPWORDS, font_path='SourceHanSans-Bold.ttf').generate(res_text)
    image_colors = ImageColorGenerator(j_coloring)

    #show the image
    plt.imshow(wc)
    plt.axis('off')
    plt.show()