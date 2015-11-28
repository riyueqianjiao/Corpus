#coding=utf-8
"""
将一词分别切成2-8词语，并统计好词频并排序
判断是否是2-8词原理为看相连一词的位置是否在同一句中
"""

import CountFreq
import gc
#list格式为[一词   1(频数)  一词所在位置]
""""" 1词 """""
def oneGram(list):
    dic = CountFreq.count(list) #返回词的dic
    f = open('1gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 2词 """""
def twoGram(list):
    list_2 = []
    for i in xrange(len(list) - 1):
        if list[i][2] == list[i+1][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]
            item1 = 1
            list_2.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_2) #回词的dic
    ff = open('2gram.txt','w')
    for i in xrange(len(list_2)):
        ff.write(list_2[i][0] + '\t' + '1' + '\t' + list_2[i][2])
        ff.write('\n')
    ff.close()
    f = open('2gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 3词 """""
def threeGram(list):
    list_3 = []
    for i in xrange(len(list) - 2):
        if list[i][2] == list[i+2][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]
            item1 = 1
            list_3.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_3)
    f = open('3gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 4词 """""
def fourGram(list):
    list_4 = []
    for i in xrange(len(list) - 3):
        if list[i][2] == list[i+3][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]+ ' ' + list[i+3][0]
            item1 = 1
            list_4.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_4)
    f = open('4gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 5词 """""
def fiveGram(list):
    list_5 = []
    for i in xrange(len(list) - 4):
        if list[i][2] == list[i+4][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]+ ' ' + list[i+3][0]+ ' ' + list[i+4][0]
            item1 = 1
            list_5.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_5)
    f = open('5gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 6词 """""
def sixGram(list):
    list_6 = []
    for i in xrange(len(list) - 5):
        if list[i][2] == list[i+5][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]+ ' ' + list[i+3][0]+ ' ' + list[i+4][0]+ ' ' + list[i+5][0]
            item1 = 1
            list_6.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_6)
    f = open('6gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 7词 """""
def sevenGram(list):
    list_7 = []
    for i in xrange(len(list) - 6):
        if list[i][2] == list[i+6][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]+ ' ' + list[i+3][0]+ ' ' + list[i+4][0]+ ' ' + list[i+5][0]+ ' ' + list[i+6][0]
            item1 = 1
            list_7.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_7)
    f = open('7gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


""""" 8词 """""
def eightGram(list):
    list_8 = []
    for i in xrange(len(list) - 7):
        if list[i][2] == list[i+7][2]:
            item0 = list[i][0] + ' ' + list[i+1][0]+ ' ' + list[i+2][0]+ ' ' + list[i+3][0]+ ' ' + list[i+4][0]+ ' ' + list[i+5][0]+ ' ' + list[i+6][0]+ ' ' + list[i+7][0]
            item1 = 1
            list_8.append([item0, item1, list[i][2]])
    dic = CountFreq.count(list_8)
    f = open('8gramindexed.txt', 'w')
    CountFreq.write(dic,f) #将统计好的词频写到f文件中


def cutGram(list):
    oneGram(list)
    twoGram(list)
    threeGram(list)
    fourGram(list)
    fiveGram(list)
    sixGram(list)
    sevenGram(list)
    eightGram(list)