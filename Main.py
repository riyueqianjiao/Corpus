#coding=utf-8
"""
运行主程序
"""

import os
import time
import CutOneGram
import CutMultiGram
import Entropy
import MaxEntropy
import MI
import MaxMi
import FaiSquare


timeclock=time.clock() #设定时间基数，之后的time.clock()即输出从此时开始的时间
print "begin"

#定义存放和输出目录
inputDir = "C:\\0721"  # 文件存放目录，已附码的各文件存放在此目录下
outputDir = "C:\\0913"  # 文件输出目录

os.chdir(outputDir)

#调用CutOneGram.py的generate,返回值为一词的list,list_1的格式为[一词   1(频数)  一词所在位置]，在outputDir生成"onegram.txt"的文件
list_1 = CutOneGram.generate(inputDir)  #调用Onegram.py的generate,返回值为一词的list
n = len(list_1)#总词数

print "onegram generated,at "+str(time.clock())+"s"


#将1-8次序列写入gramindexed.txt文件中
CutMultiGram.cutGram(list_1)
print "2-8gram generated,at "+str(time.clock())+"s"

#求左右边界熵
Entropy.entropy(list_1)
print "2-8gram entropy generated,at "+str(time.clock())+"s"

#不同长度词块熵值的对比
MaxEntropy.maxEntropy()
print "2-8gram maxEntropy generated,at "+str(time.clock())+"s"


word_dic={}
for j in xrange(1,9): #循环将1-n词的频率存到word_dic字典中,供MI/FAI/LL用
    with open('%dgramindexed.txt'%j, 'r') as f:
        gram_content = f.readlines()
    for i in xrange(len(gram_content)):
        word_dic[(gram_content[i].split('\t'))[0]]=(gram_content[i].split('\t'))[1]
print "word_dic generated,at "+str(time.clock())+"s"

#求Mi
MI.mi(word_dic,n)
print "2-8gram mi generated,at "+str(time.clock())+"s"
#不同长度词块Mi的对比
MaxMi.maxMi()
print "2-8gram maxMi generated,at "+str(time.clock())+"s"

#求Fai
FaiSquare.fai(word_dic,n)
print "2-8gram Fai generated,at "+str(time.clock())+"s"




print "total time is "+str(time.clock())+"s"