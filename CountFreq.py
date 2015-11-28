#coding=utf-8
"""
统计词频
dic用来记载词频及位置 格式为
            {'gram_1'：{'num':1,
                        'position':{'position_1':1
                                    ,'position_2':1
                                    },
                       },
             'gram_2'：{'num':1,
                        'position':{},
                        },
             ,……}
"""

def count(list):
    dic = {}
    for line in list:
        if line[0] in dic:
            dic[line[0]]['num'] = dic[line[0]].get('num',0) + 1
            dic[line[0]]['position'][line[2]] = 1
        else:
            dic[line[0]] = {}
            dic[line[0]]['num'] = 1
            dic[line[0]]['position'] = {}
            dic[line[0]]['position'][line[2]] = 1
    return dic

#将统计好的词频写入到f中
def write(dic,f):
    for key in sorted(dic.keys()):
        f.write(key)
        f.write('\t')
        f.write(str(dic[key]['num']))
        f.write('\t')
        position = []
        for k in sorted(dic[key]['position'].keys()):
            position.append(k)
        f.write(','.join(position))
        f.write('\n')
    f.close()