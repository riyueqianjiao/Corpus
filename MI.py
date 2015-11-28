#coding=utf-8
"""

"""
import math
def twoMi(dic,n):
    with open('2gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('2mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm1 = (gram[0].split(' '))[0]
        pgm2 = (gram[0].split(' '))[1]
        pgm1_freq = (float(dic[pgm1]))/n
        pgm2_freq = (float(dic[pgm2]))/n
        pmg_freq =(pgm1_freq*pgm2_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()
def threeMi(dic,n):
    with open('3gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('3mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2)/(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()

def fourMi(dic,n):
    with open('4gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('4mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的频率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pgm31_freq = (float(dic[pgm31]))/n
        pgm32_freq = (float(dic[pgm32]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2+(pgm31_freq*pgm32_freq)**2)\
                   /(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq+pgm31_freq*pgm32_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()

def fiveMi(dic,n):
    with open('5gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('5mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm41 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm42 = (gram[0].split(' '))[4]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pgm31_freq = (float(dic[pgm31]))/n
        pgm32_freq = (float(dic[pgm32]))/n
        pgm41_freq = (float(dic[pgm41]))/n
        pgm42_freq = (float(dic[pgm42]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2+(pgm31_freq*pgm32_freq)**2+(pgm41_freq*pgm42_freq)**2)\
                   /(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq+pgm31_freq*pgm32_freq+pgm41_freq*pgm42_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()

def sixMi(dic,n):
    with open('6gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('6mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm41 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm42 = (gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm51 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm52 = (gram[0].split(' '))[5]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pgm31_freq = (float(dic[pgm31]))/n
        pgm32_freq = (float(dic[pgm32]))/n
        pgm41_freq = (float(dic[pgm41]))/n
        pgm42_freq = (float(dic[pgm42]))/n
        pgm51_freq = (float(dic[pgm51]))/n
        pgm52_freq = (float(dic[pgm52]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2+(pgm31_freq*pgm32_freq)**2+(pgm41_freq*pgm42_freq)**2+(pgm51_freq*pgm52_freq)**2)\
                   /(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq+pgm31_freq*pgm32_freq\
                     +pgm41_freq*pgm42_freq+pgm51_freq*pgm52_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()

def sevenMi(dic,n):
    with open('7gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('7mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm41 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm42 = (gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm51 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm52 = (gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm61 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm62 = (gram[0].split(' '))[6]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pgm31_freq = (float(dic[pgm31]))/n
        pgm32_freq = (float(dic[pgm32]))/n
        pgm41_freq = (float(dic[pgm41]))/n
        pgm42_freq = (float(dic[pgm42]))/n
        pgm51_freq = (float(dic[pgm51]))/n
        pgm52_freq = (float(dic[pgm52]))/n
        pgm61_freq = (float(dic[pgm61]))/n
        pgm62_freq = (float(dic[pgm62]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2+(pgm31_freq*pgm32_freq)**2+
                   (pgm41_freq*pgm42_freq)**2+(pgm51_freq*pgm52_freq)**2+(pgm61_freq*pgm62_freq)**2)\
                   /(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq+pgm31_freq*pgm32_freq\
                     +pgm41_freq*pgm42_freq+pgm51_freq*pgm52_freq+pgm61_freq*pgm62_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))
        output.write('\n')
    output.close()

def eightMi(dic,n):
    with open('8gramindexed.txt', 'r') as f:
        gram_content =  f.readlines()
    output = open('8mi.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_freq = (float(gram[1]))/((n)-1)  #三词的皮率
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '\
                +(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '\
                +(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm41 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm42 = (gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm51 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '\
                +(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm52 = (gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm61 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '\
                +(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]
        pgm62 = (gram[0].split(' '))[6]+' '+(gram[0].split(' '))[7]
        pgm71 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '\
                +(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]+' '+(gram[0].split(' '))[5]+' '+(gram[0].split(' '))[6]
        pgm72 = (gram[0].split(' '))[7]
        pgm11_freq = (float(dic[pgm11]))/n
        pgm12_freq = (float(dic[pgm12]))/n
        pgm21_freq = (float(dic[pgm21]))/n
        pgm22_freq = (float(dic[pgm22]))/n
        pgm31_freq = (float(dic[pgm31]))/n
        pgm32_freq = (float(dic[pgm32]))/n
        pgm41_freq = (float(dic[pgm41]))/n
        pgm42_freq = (float(dic[pgm42]))/n  
        pgm51_freq = (float(dic[pgm51]))/n
        pgm52_freq = (float(dic[pgm52]))/n     
        pgm61_freq = (float(dic[pgm61]))/n
        pgm62_freq = (float(dic[pgm62]))/n
        pgm71_freq = (float(dic[pgm71]))/n
        pgm72_freq = (float(dic[pgm72]))/n
        pmg_freq =((pgm11_freq*pgm12_freq)**2+(pgm21_freq*pgm22_freq)**2+(pgm31_freq*pgm32_freq)**2+
                   (pgm41_freq*pgm42_freq)**2+(pgm51_freq*pgm52_freq)**2+(pgm61_freq*pgm62_freq)**2+(pgm71_freq*pgm72_freq)**2)\
                   /(pgm11_freq*pgm12_freq+pgm21_freq*pgm22_freq+pgm31_freq*pgm32_freq\
                     +pgm41_freq*pgm42_freq+pgm51_freq*pgm52_freq+pgm61_freq*pgm62_freq+pgm71_freq*pgm72_freq)
        mi = math.log(gram_freq/pmg_freq,10)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(mi))      
        output.write('\n')
    output.close()

def mi(dic,n):
    twoMi(dic,n)
    threeMi(dic,n)
    fourMi(dic,n)
    fiveMi(dic,n)
    sixMi(dic,n)
    sevenMi(dic,n)
    eightMi(dic,n)