#coding=utf-8
"""
不同长度词块熵值的对比，是最大的则保留，如三词，跟其对应的二词与四词对比，如果三词的熵值最大则保留
"""
def twoMaxMi():
    dic2={}
    dic3_1={}  #用于存放ABC三词的XBC
    dic3_2={}  #用于存放ABC三词的ABX
    f = open('3mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic3_1['X '+gram[1]+' '+gram[2]]=dic3_1.get('X '+gram[1]+' '+gram[2],{})
        dic3_1['X '+gram[1]+' '+gram[2]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic3_2[gram[0]+' '+gram[1]+' X']=dic3_1.get(gram[0]+' '+gram[1]+' X',{})
        dic3_2[gram[0]+' '+gram[1]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()
    f = open('2mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        dic2[gram]={}
        dic2[gram]['2gram'] = {}
        dic2[gram]['2gram'][gram] = content[i].split('\t')[1]
        dic2[gram]['3gram'] = {}
        dic2[gram]['3gram']['X '+gram] = dic3_1.get('X '+gram,{})
        dic2[gram]['3gram'][gram+' X'] = dic3_2.get(gram+' X',{})
    f.close()
    def compare(k,dic2):
        twoMI = dic2[k]['2gram'][k]
        for key in sorted(dic2[k]['3gram']['X '+k].keys()):
            if dic2[k]['3gram']['X '+k][key] > twoMI:
                return False
        for key in sorted(dic2[k]['3gram'][k+' X'].keys()):
            if dic2[k]['3gram'][k+' X'][key] > twoMI:
                return False
        return True
    f = open('2maxMi.txt', 'w')
    for k in sorted(dic2.keys()):
        boolean = compare(k,dic2)
        if boolean == True:
            f.write(k+'\t'+str(dic2[k]['2gram'][k]))
            f.write('\n')
    f.close()

def threeMaxMi():
    dic2={}
    dic3={}
    dic4_1={}  #用于存放ABCD的XBCD
    dic4_2={}  #用于存放ABCD的ABCX
    f = open('2mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic2[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    f = open('4mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic4_1['X '+gram[1]+' '+gram[2]+' '+gram[3]]=dic4_1.get('X '+gram[1]+' '+gram[2]+' '+gram[3],{})
        dic4_1['X '+gram[1]+' '+gram[2]+' '+gram[3]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic4_2[gram[0]+' '+gram[1]+' '+gram[2]+' X']=dic4_1.get(gram[0]+' '+gram[1]+' '+gram[2]+' X',{})
        dic4_2[gram[0]+' '+gram[1]+' '+gram[2]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()


    def compare(k,dic): #参数为gram,dic3[gram] dic=dic3[k]
        onegram = k.split(' ')
        threeMI = dic['3gram'][k]
        if dic['2gram'][onegram[0]+' '+onegram[1]] > threeMI:
            return False
        if dic['2gram'][onegram[1]+' '+onegram[2]] > threeMI:
            return False
        for key in sorted(dic['4gram']['X '+k].keys()):
            if dic['4gram']['X '+k][key] > threeMI:
                return False
        for key in sorted(dic['4gram'][k+' X'].keys()):
            if dic['4gram'][k+' X'][key] > threeMI:
                return False
        return True

    f = open('3mi.txt', 'r')
    fout = open('3maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic3[gram]={}
        dic3[gram]['2gram'] = {}
        dic3[gram]['2gram'][onegram[0]+' '+onegram[1]] = dic2[onegram[0]+' '+onegram[1]]
        dic3[gram]['2gram'][onegram[1]+' '+onegram[2]] = dic2[onegram[1]+' '+onegram[2]]
        dic3[gram]['3gram'] = {}
        dic3[gram]['3gram'][gram] = content[i].split('\t')[1]
        dic3[gram]['4gram'] = {}
        dic3[gram]['4gram']['X '+gram] = dic4_1.get('X '+gram,{})
        dic3[gram]['4gram'][gram+' X'] = dic4_2.get(gram+' X',{})
        boolean = compare(gram,dic3[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic3[gram]
    f.close()
    fout.close()

def fourMaxMi():
    dic3={}
    dic4={}
    dic5_1={}  #用于存放ABCDE的XBCDE
    dic5_2={}  #用于存放ABCDE的ABCDX

    f = open('3mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic3[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    f = open('5mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic5_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]]=dic5_1.get('X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4],{})
        dic5_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic5_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' X']=dic5_1.get(gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' X',{})
        dic5_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    def compare(k,dic): #参数为gram,dic4[gram] dic=dic4[k]
        onegram = k.split(' ')
        fourMI = dic['4gram'][k]
        if dic['3gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]] > fourMI:
            return False
        if dic['3gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]] > fourMI:
            return False
        for key in sorted(dic['5gram']['X '+k].keys()):
            if dic['5gram']['X '+k][key] > fourMI:
                return False
        for key in sorted(dic['5gram'][k+' X'].keys()):
            if dic['5gram'][k+' X'][key] > fourMI:
                return False
        return True

    f = open('4mi.txt', 'r')
    fout = open('4maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic4[gram]={}
        dic4[gram]['3gram'] = {}
        dic4[gram]['3gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]] = dic3[onegram[0]+' '+onegram[1]+' '+onegram[2]]
        dic4[gram]['3gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]] = dic3[onegram[1]+' '+onegram[2]+' '+onegram[3]]
        dic4[gram]['4gram'] = {}
        dic4[gram]['4gram'][gram] = content[i].split('\t')[1]
        dic4[gram]['5gram'] = {}
        dic4[gram]['5gram']['X '+gram] = dic5_1.get('X '+gram,{})
        dic4[gram]['5gram'][gram+' X'] = dic5_2.get(gram+' X',{})
        boolean = compare(gram,dic4[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic4[gram]
    f.close()
    fout.close()

def fiveMaxMi():
    dic4={}
    dic5={}
    dic6_1={}  #用于存放ABCDE的XBCDE
    dic6_2={}  #用于存放ABCDE的ABCDX

    f = open('4mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic4[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    f = open('6mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic6_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]]=dic6_1.get('X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5],{})
        dic6_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic6_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' X']=dic6_1.get(gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' X',{})
        dic6_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    def compare(k,dic): #参数为gram,dic5[gram] dic=dic5[k]
        onegram = k.split(' ')
        fiveMI = dic['5gram'][k]
        if dic['4gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]] > fiveMI:
            return False
        if dic['4gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]] > fiveMI:
            return False
        for key in sorted(dic['6gram']['X '+k].keys()):
            if dic['6gram']['X '+k][key] > fiveMI:
                return False
        for key in sorted(dic['6gram'][k+' X'].keys()):
            if dic['6gram'][k+' X'][key] > fiveMI:
                return False
        return True

    f = open('5mi.txt', 'r')
    fout = open('5maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic5[gram]={}
        dic5[gram]['4gram'] = {}
        dic5[gram]['4gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]] = dic4[onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]]
        dic5[gram]['4gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]] = dic4[onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]]
        dic5[gram]['5gram'] = {}
        dic5[gram]['5gram'][gram] = content[i].split('\t')[1]
        dic5[gram]['6gram'] = {}
        dic5[gram]['6gram']['X '+gram] = dic6_1.get('X '+gram,{})
        dic5[gram]['6gram'][gram+' X'] = dic6_2.get(gram+' X',{})
        boolean = compare(gram,dic5[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic5[gram]
    f.close()
    fout.close()

def sixMaxMi():
    dic5={}
    dic6={}
    dic7_1={}  #用于存放ABCDE的XBCDE
    dic7_2={}  #用于存放ABCDE的ABCDX


    f = open('5mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic5[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()


    f = open('7mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic7_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]]=dic7_1.get('X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6],{})
        dic7_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic7_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' X']=dic7_2.get(gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' X',{})
        dic7_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    def compare(k,dic): #参数为gram,dic6[gram] dic=dic6[k]
        onegram = k.split(' ')
        sixMI = dic['6gram'][k]
        if dic['5gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]] > sixMI:
            return False
        if dic['5gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]] > sixMI:
            return False
        for key in sorted(dic['7gram']['X '+k].keys()):
            if dic['7gram']['X '+k][key] > sixMI:
                return False
        for key in sorted(dic['7gram'][k+' X'].keys()):
            if dic['7gram'][k+' X'][key] > sixMI:
                return False
        return True

    f = open('6mi.txt', 'r')
    fout = open('6maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic6[gram]={}
        dic6[gram]['5gram'] = {}
        dic6[gram]['5gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]] = dic5[onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]]
        dic6[gram]['5gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]] = dic5[onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]]
        dic6[gram]['6gram'] = {}
        dic6[gram]['6gram'][gram] = content[i].split('\t')[1]
        dic6[gram]['7gram'] = {}
        dic6[gram]['7gram']['X '+gram] = dic7_1.get('X '+gram,{})
        dic6[gram]['7gram'][gram+' X'] = dic7_2.get(gram+' X',{})
        boolean = compare(gram,dic6[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic6[gram]
    f.close()
    fout.close()

def sevenMaxMi():
    dic6={}
    dic7={}
    dic8_1={}  #用于存放ABCDE的XBCDE
    dic8_2={}  #用于存放ABCDE的ABCDX

    f = open('6mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic6[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    f = open('8mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0].split(' ')
        dic8_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' '+gram[7]]\
            = dic8_1.get('X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' '+gram[7],{})
        dic8_1['X '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' '+gram[7]][content[i].split('\t')[0]] = content[i].split('\t')[1]
        dic8_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' X']\
            =dic8_2.get(gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' X',{})
        dic8_2[gram[0]+' '+gram[1]+' '+gram[2]+' '+gram[3]+' '+gram[4]+' '+gram[5]+' '+gram[6]+' X'][content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    def compare(k,dic): #参数为gram,dic6[gram] dic=dic6[k]
        onegram = k.split(' ')
        sevenMI = dic['7gram'][k]
        if dic['6gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]] > sevenMI:
            return False
        if dic['6gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]] > sevenMI:
            return False
        for key in sorted(dic['8gram']['X '+k].keys()):
            if dic['8gram']['X '+k][key] > sevenMI:
                return False
        for key in sorted(dic['8gram'][k+' X'].keys()):
            if dic['8gram'][k+' X'][key] > sevenMI:
                return False
        return True

    f = open('7mi.txt', 'r')
    fout = open('7maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic7[gram]={}
        dic7[gram]['6gram'] = {}
        dic7[gram]['6gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]] \
            = dic6[onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]]
        dic7[gram]['6gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]] \
            = dic6[onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]]
        dic7[gram]['7gram'] = {}
        dic7[gram]['7gram'][gram] = content[i].split('\t')[1]
        dic7[gram]['8gram'] = {}
        dic7[gram]['8gram']['X '+gram] = dic8_1.get('X '+gram,{})
        dic7[gram]['8gram'][gram+' X'] = dic8_2.get(gram+' X',{})
        boolean = compare(gram,dic7[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic7[gram]
    f.close()
    fout.close()

def eightMaxMi():
    dic7 = {}
    dic8 = {}

    f = open('7mi.txt', 'r')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        dic7[content[i].split('\t')[0]] = content[i].split('\t')[1]
    f.close()

    def compare(k,dic): #参数为gram,dic6[gram] dic=dic6[k]
        onegram = k.split(' ')
        eightMI = dic['8gram'][k]
        if dic['7gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]] > eightMI:
            return False
        if dic['7gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]+' '+onegram[7]] > eightMI:
            return False
        return True

    f = open('8mi.txt', 'r')
    fout = open('8maxMi.txt', 'w')
    content = f.read().split('\n')
    content = [e for e in content if len(e) > 0]
    for i in xrange(len(content)):
        gram = content[i].split('\t')[0]
        onegram = gram.split(' ')
        dic8[gram]={}
        dic8[gram]['7gram'] = {}
        dic8[gram]['7gram'][onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]] \
            = dic7[onegram[0]+' '+onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]]
        dic8[gram]['7gram'][onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]+' '+onegram[7]] \
            = dic7[onegram[1]+' '+onegram[2]+' '+onegram[3]+' '+onegram[4]+' '+onegram[5]+' '+onegram[6]+' '+onegram[7]]
        dic8[gram]['8gram'] = {}
        dic8[gram]['8gram'][gram] = content[i].split('\t')[1]
        boolean = compare(gram,dic8[gram])
        if boolean is True:
                fout.write(gram+'\t'+content[i].split('\t')[1])
                fout.write('\n')
        del dic8[gram]
    f.close()
    fout.close()

def maxMi():
    twoMaxMi()
    threeMaxMi()
    fourMaxMi()
    fiveMaxMi()
    sixMaxMi()
    sevenMaxMi()
    eightMaxMi()