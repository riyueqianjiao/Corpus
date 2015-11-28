#coding=utf-8
"""
将制定文件夹内所有文件切成一词并合并在一个文件中，同时对数据进行预处理（比如只保留单词和数字，去掉各种标点，将数字统一为#符号）
合并的文件中，每行为一个词，数据格式为[一词   1(频数)  一词所在位置]
"""

import os
import re


#生成名为"onegram.txt"的合并文件，并返回一个一词list
def generate(inputDir):
    fileNameList = os.listdir(inputDir)
    list_1 = []
    if os.path.exists("onegram.txt"):
        os.remove('onegram.txt')
    for fileName in fileNameList:  # 遍历文件
        txtRead = open(inputDir + "/" + fileName, "r")
        content = txtRead.read()
        txtRead.close()
        sentences = content.split("\n")
        sentences = [e for e in sentences if len(e) > 4]

        f = file("onegram.txt", "a")
        for i in xrange(len(sentences)):
            words = sentences[i].split()
            for ii in xrange(len(words)):
                if re.search("[A-Za-z0-9]", words[ii][0]) != None:  # 去掉符号，只保留单词和数字
                    if re.search("[0-9]",words[ii].split("_")[0]) != None:
                       words[ii] ="#" + "_" + words[ii].split("_")[1]
                    # for num in "0123456789":
                    #     words[ii] = words[ii].split("_")[0].replace(num, "#") + "_" + words[ii].split("_")[1]
                    if words[ii].startswith("#"):
                        words[ii] = list(words[ii])
                        while words[ii].count("#") > 1:
                            words[ii].remove("#")
                        words[ii] = "".join(words[ii])
                    words[ii] = words[ii].upper()#将单词大写
                    list_1.append(
                        (words[ii] + '\t' + '1' + '\t' + fileName + ': s' + str(i + 1) + '_1').split("\t"))
                    f.write(words[ii])
                    f.write('\t' + '1' + '\t')
                    f.write(fileName + ': s' + str(i + 1) + '_1')
                    f.write('\n')
        f.close()
    return list_1