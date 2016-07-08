#coding=utf-8
'''
Created on 2016-1-23

@author: kwsy
'''
import re
import math

minLen = 1
maxLen = 4

def getAllChineseCharacters(content):
    regex = u'[\u4e00-\u9fa5]+'
    res=re.findall(regex, content)
    return res


def getLatentword2(txt,length,width,index):
    lst = []
    for i in range(length):
        if i+width<=length:
            word = txt[i:i+width]
            left = None
            right = None
            if i>0:
                left = txt[i-1:i]
            if i<length-1:
                right = txt[i+width:i+width+1]
            wordindex = index+i
            item = {'word':word,'left':left,'right':right,'wordindex':wordindex}
            lst.append(item)
    return lst
def getLatentword(txt,index):
    LatentLst = []
    length = len(txt)
    for i in range(minLen,maxLen+1):
        lst = getLatentword2(txt,length,i,index)
        LatentLst.extend(lst)
    '''
    for item in LatentLst:
        print item['word'],' ',item['left'],' ',item['right'],' ',item['wordindex']
    '''
    return LatentLst


def splitWord(word):
    lst = []
    length = len(word)
    for i in range(1,length):
        lst.append((word[0:i],word[i:length]))
    return lst

def calculateFreedom(wordLst):
    wordDic = {}
    for word in wordLst:
        if not word in wordDic:
            wordDic[word] = 0
        wordDic[word] = wordDic[word]+1
    
    count = len(wordLst)
    freedom = 0
    for word,wordcount in wordDic.items():
        freedom = freedom - float(wordcount)/float(count)*math.log(float(wordcount)/float(count))
    return freedom
	
if __name__ == '__main__':
   lst = [ u'不', u'皮', u'倒', u'皮']
   print (calculateFreedom(lst))