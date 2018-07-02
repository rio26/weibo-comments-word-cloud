# - * - coding: utf - 8 -*-
#
# Author: Rio Kunn
# Date: Jun 30, 2018 
# 
# This file genereates a simple Chinese word cloud

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import jieba

# open the file with "read" attribute
with open('comment.txt', 'r') as f:
    f_text = f.read()							#read file
    res = jieba.cut(f_text)						#split chinese characters using jieba package
    res_text = ' '.join(res)					
    background_img = plt.imread('back.jpeg')
    STOPWORDS.add('via')						 #add stop words

    #generate the word cloud
    wc = WordCloud(background_color="white",mask=background_img,stopwords=STOPWORDS, font_path='SourceHanSans-Bold.ttf').generate(res_text)

    #show the image
    plt.imshow(wc)
    plt.axis('off')
    plt.show()