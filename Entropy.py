#coding=utf-8
"""
计算左右边界熵
dic用来记载词及其左右词 格式为
            {'gram_1'：{'num':1,
                         'left':{'left_1':1,'left_2':2},
                         'right':{'right_1':1,'right_2':2}
                        },
             'gram_2'：{'num':1,
                         'left':{},
                         'right':{}
                        },
             ,……}

"""

import math


def calMME(dic,num): #计算边界熵
    mmeValue = 0
    for k in dic:
        mmeValue+=(float(dic[k])/num)*math.log(float(dic[k])/num,2)
    return -mmeValue
def calLeftAndRightMME(leftDic,rightDic,num,leftmax,rightmax):#计算左右边界熵
    leftMME = calMME(leftDic,num)/(math.floor(leftmax)+1)
    rightMME = calMME(rightDic,num)/(math.floor(rightmax)+1)
    if leftMME == 0 or rightMME ==0:  #只要有一个边界熵是0则左右边界熵为0
        leftAndRightMME = 0
    else:
        leftAndRightMME = (1-float(1)/num)*(math.sqrt((1-leftMME)*(1-rightMME)))
    return leftAndRightMME

def twoEntropy(list):
    dic={}
    if list[0][2] == list[1][2]:#单独考虑第一个二词和最后一个二词
        twogram = list[0][0]+' '+list[1][0]
        dic[twogram]={}
        dic[twogram]['num']=1
        dic[twogram]['right']={}
        dic[twogram]['left']={}
        dic[twogram]['left']['']=1    #全文第一个二词显然没有左词
        if list[2][2] == list[1][2]: #如果有右词
            dic[twogram]['right'][list[2][0]]=1
        else:    #如果没有右词
            dic[twogram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 2][2]:
        twogram1 = list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        dic[twogram1]={}
        dic[twogram1]['num']=dic[twogram1].get('num',0)+1
        dic[twogram1]['left']={}
        dic[twogram1]['right']={}
        dic[twogram1]['right']['']=dic[twogram1].get('',0)+1
        if list[len(list) - 3][2] == list[len(list) - 2][2]:       #如果有左词
            dic[twogram1]['left'][list[len(list) - 3][0]] = dic[twogram1]['left'].get(list[len(list) - 3][0],0)+1
        else:
            dic[twogram1]['left'][''] = dic[twogram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 2): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+1][2]:
            twogram2 = list[i][0]+' '+list[i+1][0]
            if dic.__contains__(twogram2):
                dic[twogram2]['num']+=1
            else:
                dic[twogram2]={}
                dic[twogram2]['left']={}
                dic[twogram2]['right']={}
                dic[twogram2]['num'] = dic[twogram2].get('num',0)+1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[twogram2]['left'][list[i-1][0]]=dic[twogram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[twogram2]['left']['']=dic[twogram2]['left'].get('',0)+1
            if list[i+2][2] ==list[i][2]: #如果有右词
                dic[twogram2]['right'][list[i+2][0]]=dic[twogram2]['right'].get(list[i+2][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[twogram2]['right']['']=dic[twogram2]['right'].get('',0)+1
    f = open('2Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def threeEntropy(list):
    dic = {}
    if list[0][2] == list[2][2]:#单独考虑第一个三词和最后一个三词
        threegram = list[0][0]+' '+list[1][0]+' '+list[2][0]
        dic[threegram]={}
        dic[threegram]['num']=1
        dic[threegram]['right']={}
        dic[threegram]['left']={}
        dic[threegram]['left']['']=1    #全文第一个三词显然没有左词
        if list[3][2] == list[1][2]: #如果有右词
            dic[threegram]['right'][list[3][0]]=1
        else:    #如果没有右词
            dic[threegram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 3][2]:
        threegram1 = list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(threegram1):
            dic[threegram1]['num']+=1
            dic[threegram1]['right']['']=dic[threegram1].get('',0)+1
        else :
            dic[threegram1]={}
            dic[threegram1]['num'] = 1
            dic[threegram1]['left'] = {}
            dic[threegram1]['right'] = {}
            dic[threegram1]['right'][''] = 1
        if list[len(list) - 4][2] == list[len(list) - 2][2]:      #如果有左词
            dic[threegram1]['left'][list[len(list) - 4][0]] = dic[threegram1]['left'].get(list[len(list) - 4][0],0)+1
        else:
            dic[threegram1]['left'][''] = dic[threegram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 3): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+2][2]:
            threegram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]
            if dic.__contains__(threegram2):
                dic[threegram2]['num']+=1
            else:
                dic[threegram2]={}
                dic[threegram2]['left']={}
                dic[threegram2]['right']={}
                dic[threegram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[threegram2]['left'][list[i-1][0]]=dic[threegram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[threegram2]['left']['']=dic[threegram2]['left'].get('',0)+1
            if list[i+3][2] ==list[i][2]: #如果有右词
                dic[threegram2]['right'][list[i+3][0]]=dic[threegram2]['right'].get(list[i+3][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[threegram2]['right']['']=dic[threegram2]['right'].get('',0)+1
    f = open('3Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def fourEntropy(list):
    dic = {}
    if list[0][2] == list[3][2]:#单独考虑第一个四词和最后一个四词
        fourgram = list[0][0]+' '+list[1][0]+' '+list[2][0]+' '+list[3][0]
        dic[fourgram]={}
        dic[fourgram]['num']=1
        dic[fourgram]['right']={}
        dic[fourgram]['left']={}
        dic[fourgram]['left']['']=1    #全文第一个四词显然没有左词
        if list[4][2] == list[1][2]: #如果有右词
            dic[fourgram]['right'][list[4][0]]=1
        else:    #如果没有右词
            dic[fourgram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 4][2]:
        fourgram1 = list[len(list) - 4][0]+' '+list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(fourgram1):
            dic[fourgram1]['num']+=1
            dic[fourgram1]['right']['']=dic[fourgram1].get('',0)+1
        else :
            dic[fourgram1]={}
            dic[fourgram1]['num'] = 1
            dic[fourgram1]['left'] = {}
            dic[fourgram1]['right'] = {}
            dic[fourgram1]['right'][''] = 1
        if list[len(list) - 5][2] == list[len(list) - 2][2]:      #如果有左词
            dic[fourgram1]['left'][list[len(list) - 5][0]] = dic[fourgram1]['left'].get(list[len(list) - 5][0],0)+1
        else:
            dic[fourgram1]['left'][''] = dic[fourgram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 4): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+3][2]:
            fourgram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]+' '+list[i+3][0]
            if dic.__contains__(fourgram2):
                dic[fourgram2]['num']+=1
            else:
                dic[fourgram2]={}
                dic[fourgram2]['left']={}
                dic[fourgram2]['right']={}
                dic[fourgram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[fourgram2]['left'][list[i-1][0]]=dic[fourgram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[fourgram2]['left']['']=dic[fourgram2]['left'].get('',0)+1
            if list[i+4][2] ==list[i][2]: #如果有右词
                dic[fourgram2]['right'][list[i+4][0]]=dic[fourgram2]['right'].get(list[i+4][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[fourgram2]['right']['']=dic[fourgram2]['right'].get('',0)+1
    f = open('4Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def fiveEntropy(list):
    dic = {}
    if list[0][2] == list[4][2]:#单独考虑第一个四词和最后一个四词
        fivegram = list[0][0]+' '+list[1][0]+' '+list[2][0]+' '+list[3][0]+' '+list[4][0]
        dic[fivegram]={}
        dic[fivegram]['num']=1
        dic[fivegram]['right']={}
        dic[fivegram]['left']={}
        dic[fivegram]['left']['']=1    #全文第一个四词显然没有左词
        if list[5][2] == list[1][2]: #如果有右词
            dic[fivegram]['right'][list[5][0]]=1
        else:    #如果没有右词
            dic[fivegram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 5][2]:
        fivegram1 = list[len(list) - 5][0]+' '+list[len(list) - 4][0]+' '+list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(fivegram1):
            dic[fivegram1]['num']+=1
            dic[fivegram1]['right']['']=dic[fivegram1].get('',0)+1
        else :
            dic[fivegram1]={}
            dic[fivegram1]['num'] = 1
            dic[fivegram1]['left'] = {}
            dic[fivegram1]['right'] = {}
            dic[fivegram1]['right'][''] = 1
        if list[len(list) - 6][2] == list[len(list) - 2][2]:      #如果有左词
            dic[fivegram1]['left'][list[len(list) - 6][0]] = dic[fivegram1]['left'].get(list[len(list) - 6][0],0)+1
        else:
            dic[fivegram1]['left'][''] = dic[fivegram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 5): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+4][2]:
            fivegram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]+' '+list[i+3][0]+' '+list[i+4][0]
            if dic.__contains__(fivegram2):
                dic[fivegram2]['num']+=1
            else:
                dic[fivegram2]={}
                dic[fivegram2]['left']={}
                dic[fivegram2]['right']={}
                dic[fivegram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[fivegram2]['left'][list[i-1][0]]=dic[fivegram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[fivegram2]['left']['']=dic[fivegram2]['left'].get('',0)+1
            if list[i+5][2] ==list[i][2]: #如果有右词
                dic[fivegram2]['right'][list[i+5][0]]=dic[fivegram2]['right'].get(list[i+5][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[fivegram2]['right']['']=dic[fivegram2]['right'].get('',0)+1
    f = open('5Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def sixEntropy(list):
    dic = {}
    if list[0][2] == list[5][2]:#单独考虑第一个四词和最后一个四词
        sixgram = list[0][0]+' '+list[1][0]+' '+list[2][0]+' '+list[3][0]+' '+list[4][0]+' '+list[5][0]
        dic[sixgram]={}
        dic[sixgram]['num']=1
        dic[sixgram]['right']={}
        dic[sixgram]['left']={}
        dic[sixgram]['left']['']=1    #全文第一个四词显然没有左词
        if list[6][2] == list[1][2]: #如果有右词
            dic[sixgram]['right'][list[6][0]]=1
        else:    #如果没有右词
            dic[sixgram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 6][2]:
        sixgram1 = list[len(list) - 6][0]+' '+list[len(list) - 5][0]+' '+list[len(list) - 4][0]+' '+list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(sixgram1):
            dic[sixgram1]['num']+=1
            dic[sixgram1]['right']['']=dic[sixgram1].get('',0)+1
        else :
            dic[sixgram1]={}
            dic[sixgram1]['num'] = 1
            dic[sixgram1]['left'] = {}
            dic[sixgram1]['right'] = {}
            dic[sixgram1]['right'][''] = 1
        if list[len(list) - 7][2] == list[len(list) - 2][2]:      #如果有左词
            dic[sixgram1]['left'][list[len(list) - 7][0]] = dic[sixgram1]['left'].get(list[len(list) - 7][0],0)+1
        else:
            dic[sixgram1]['left'][''] = dic[sixgram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 6): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+5][2]:
            sixgram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]+' '+list[i+3][0]+' '+list[i+4][0]+' '+list[i+5][0]
            if dic.__contains__(sixgram2):
                dic[sixgram2]['num']+=1
            else:
                dic[sixgram2]={}
                dic[sixgram2]['left']={}
                dic[sixgram2]['right']={}
                dic[sixgram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[sixgram2]['left'][list[i-1][0]]=dic[sixgram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[sixgram2]['left']['']=dic[sixgram2]['left'].get('',0)+1
            if list[i+6][2] ==list[i][2]: #如果有右词
                dic[sixgram2]['right'][list[i+6][0]]=dic[sixgram2]['right'].get(list[i+6][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[sixgram2]['right']['']=dic[sixgram2]['right'].get('',0)+1
    f = open('6Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def sevenEntropy(list):
    dic = {}
    if list[0][2] == list[6][2]:#单独考虑第一个七词和最后一个七词
        sevengram = list[0][0]+' '+list[1][0]+' '+list[2][0]+' '+list[3][0]+' '+list[4][0]+' '+list[5][0]+' '+list[6][0]
        dic[sevengram]={}
        dic[sevengram]['num']=1
        dic[sevengram]['right']={}
        dic[sevengram]['left']={}
        dic[sevengram]['left']['']=1    #全文第一个七词显然没有左词
        if list[7][2] == list[1][2]: #如果有右词
            dic[sevengram]['right'][list[7][0]]=1
        else:    #如果没有右词
            dic[sevengram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 7][2]:
        sevengram1 = list[len(list) - 7][0]+' '+list[len(list) - 6][0]+' '+list[len(list) - 5][0]+' '+list[len(list) - 4][0]+' '+list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(sevengram1):
            dic[sevengram1]['num']+=1
            dic[sevengram1]['right']['']=dic[sevengram1].get('',0)+1
        else :
            dic[sevengram1]={}
            dic[sevengram1]['num'] = 1
            dic[sevengram1]['left'] = {}
            dic[sevengram1]['right'] = {}
            dic[sevengram1]['right'][''] = 1
        if list[len(list) - 8][2] == list[len(list) - 2][2]:      #如果有左词
            dic[sevengram1]['left'][list[len(list) - 8][0]] = dic[sevengram1]['left'].get(list[len(list) - 8][0],0)+1
        else:
            dic[sevengram1]['left'][''] = dic[sevengram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 7): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+6][2]:
            sevengram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]+' '+list[i+3][0]+' '+list[i+4][0]+' '+list[i+5][0]+' '+list[i+6][0]
            if dic.__contains__(sevengram2):
                dic[sevengram2]['num']+=1
            else:
                dic[sevengram2]={}
                dic[sevengram2]['left']={}
                dic[sevengram2]['right']={}
                dic[sevengram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[sevengram2]['left'][list[i-1][0]]=dic[sevengram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[sevengram2]['left']['']=dic[sevengram2]['left'].get('',0)+1
            if list[i+7][2] ==list[i][2]: #如果有右词
                dic[sevengram2]['right'][list[i+7][0]]=dic[sevengram2]['right'].get(list[i+7][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[sevengram2]['right']['']=dic[sevengram2]['right'].get('',0)+1
    f = open('7Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def eightEntropy(list):
    dic = {}
    if list[0][2] == list[7][2]:#单独考虑第一个八词和最后一个八词
        eightgram = list[0][0]+' '+list[1][0]+' '+list[2][0]+' '+list[3][0]+' '+list[4][0]+' '+list[5][0]+' '+list[6][0]+' '+list[7][0]
        dic[eightgram]={}
        dic[eightgram]['num']=1
        dic[eightgram]['right']={}
        dic[eightgram]['left']={}
        dic[eightgram]['left']['']=1    #全文第一个八词显然没有左词
        if list[8][2] == list[1][2]: #如果有右词
            dic[eightgram]['right'][list[8][0]]=1
        else:    #如果没有右词
            dic[eightgram]['right']['']=1
    if list[len(list) - 1][2] == list[len(list) - 8][2]:
        eightgram1 = list[len(list) - 8][0]+' '+list[len(list) - 7][0]+' '+list[len(list) - 6][0]+' '+list[len(list) - 5][0]+' '+list[len(list) - 4][0]+' '+list[len(list) - 3][0]+' '+list[len(list) - 2][0]+' '+list[len(list) - 1][0]
        if dic.__contains__(eightgram1):
            dic[eightgram1]['num']+=1
            dic[eightgram1]['right']['']=dic[eightgram1].get('',0)+1
        else :
            dic[eightgram1]={}
            dic[eightgram1]['num'] = 1
            dic[eightgram1]['left'] = {}
            dic[eightgram1]['right'] = {}
            dic[eightgram1]['right'][''] = 1
        if list[len(list) - 9][2] == list[len(list) - 2][2]:      #如果有左词
            dic[eightgram1]['left'][list[len(list) - 9][0]] = dic[eightgram1]['left'].get(list[len(list) - 9][0],0)+1
        else:
            dic[eightgram1]['left'][''] = dic[eightgram1]['left'].get('',0)+1
    for i in xrange(1,len(list) - 8): #将第一个词和最后一个词在上方单独处理
        if list[i][2] == list[i+7][2]:
            eightgram2 = list[i][0]+' '+list[i+1][0]+' '+list[i+2][0]+' '+list[i+3][0]+' '+list[i+4][0]+' '+list[i+5][0]+' '+list[i+6][0]+' '+list[i+7][0]
            if dic.__contains__(eightgram2):
                dic[eightgram2]['num']+=1
            else:
                dic[eightgram2]={}
                dic[eightgram2]['left']={}
                dic[eightgram2]['right']={}
                dic[eightgram2]['num'] = 1
            if list[i-1][2] ==list[i][2]: #如果有左词
                dic[eightgram2]['left'][list[i-1][0]]=dic[eightgram2]['left'].get(list[i-1][0],0)+1
            else:                       #如果没有左词，将{'',1}存入
                dic[eightgram2]['left']['']=dic[eightgram2]['left'].get('',0)+1
            if list[i+8][2] ==list[i][2]: #如果有右词
                dic[eightgram2]['right'][list[i+8][0]]=dic[eightgram2]['right'].get(list[i+8][0],0)+1
            else:           #如果没有右词，将{'',1}存入
                dic[eightgram2]['right']['']=dic[eightgram2]['right'].get('',0)+1
    f = open('8Entropy.txt', 'w')
    leftmax = 0
    rightmax = 0
    for key in sorted(dic.keys()):
        leftmax = max(leftmax,calMME(dic[key]['left'],dic[key]['num'])) #取左熵最大值
    for key in sorted(dic.keys()):
        rightmax = max(rightmax,calMME(dic[key]['right'],dic[key]['num'])) #取右熵最大值
    for k in sorted(dic.keys()):
        leftAndRightMME = calLeftAndRightMME(dic[k]['left'],dic[k]['right'],dic[k]['num'],leftmax,rightmax)
        f.write(k+'\t'+str(leftAndRightMME))
        f.write('\n')
    f.close()

def entropy(list):
    twoEntropy(list)
    threeEntropy(list)
    fourEntropy(list)
    fiveEntropy(list)
    sixEntropy(list)
    sevenEntropy(list)
    eightEntropy(list)
