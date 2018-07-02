# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 2018

@author: Rio Kunn
"""

import re
from bs4 import BeautifulSoup

f1 = open("comment-ori.txt",'r')             # read the original file
f2 = open("comment.txt",'w')            	 # write a new file

soup = BeautifulSoup(f1, "html.parser")		 # Remove html tags with beautiful soup
text = soup.get_text().encode('utf-8')		 # Parsing to 'utf-8' format
f2.write(text)								 # write into "comment.txt"

# close the file
f1.close()
f2.close()