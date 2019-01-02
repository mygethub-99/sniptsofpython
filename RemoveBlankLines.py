# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:59:00 2019
Remove unwanted blank lines in a text file
@author: ow4253
"""

from path import Path

data=Path(r'C:\Users\ow4253\Documents\Emailscript\batch1.txt')

catch=[]
with open(data) as f:
    for line in f:
        if not line.isspace():
            catch.append(line)
            
with open('clean.txt','w') as fs:
    for i in catch:
        fs.write("{}".format(i))
    fs.close()
