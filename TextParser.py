# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 12:16:32 2019
Opens emails in form of a .txt file, pulls specific lines of text, stores data in new .txt file
@author: ow4253
"""
from path import Path

#Declare function to catch wanted lines of text
def catch_lines(lines,i):
    for increment in range(0,7):
        catch.append(lines[i+increment])
    catch.append('\n')  
    
data=Path(r'C:\Users\ow4253\Documents\Python Scripts\clean.txt')
catch=[]

with open(data) as f:
    lines=f.readlines()
    for i, line in enumerate(lines):
        line=line.lower()
        if 'we have' in line:
            catch_lines(lines,i)

with open('parse.txt','w') as fs:
    for i in catch:
        fs.write("{}".format(i))
    fs.close()
