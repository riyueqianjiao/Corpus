#coding=utf-8
"""

"""
def twoFai(dic,n):
    with open('2gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('2fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
        pgm1 = (gram[0].split(' '))[0]
        pgm2 = (gram[0].split(' '))[1]
        pgm1_num = float(dic[pgm1])
        pgm2_num = float(dic[pgm2])
        pai = (gram_num*n-pgm1_num*pgm2_num)**2/(pgm1_num*pgm2_num*(n-pgm1_num)*(n-pgm2_num))
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def threeFai(dic,n):
    with open('3gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('3fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai = (pai1**2+pai2**2)/(pai1+pai2)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))   
        output.write('\n')
    output.close()

def fourFai(dic,n):
    with open('4gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('4fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pgm31_num = float(dic[pgm31])
        pgm32_num = float(dic[pgm32])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai3 = (gram_num*n-pgm31_num*pgm32_num)**2/(pgm31_num*pgm32_num*(n-pgm31_num)*(n-pgm32_num))
        pai = (pai1**2+pai2**2+pai3**2)/(pai1+pai2+pai3)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def fiveFai(dic,n):
    with open('5gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('5fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
        pgm11 = (gram[0].split(' '))[0]
        pgm12 = (gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm21 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]
        pgm22 = (gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm31 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]
        pgm32 = (gram[0].split(' '))[3]+' '+(gram[0].split(' '))[4]
        pgm41 = (gram[0].split(' '))[0]+' '+(gram[0].split(' '))[1]+' '+(gram[0].split(' '))[2]+' '+(gram[0].split(' '))[3]
        pgm42 = (gram[0].split(' '))[4]
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pgm31_num = float(dic[pgm31])
        pgm32_num = float(dic[pgm32])
        pgm41_num = float(dic[pgm41])
        pgm42_num = float(dic[pgm42])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai3 = (gram_num*n-pgm31_num*pgm32_num)**2/(pgm31_num*pgm32_num*(n-pgm31_num)*(n-pgm32_num))
        pai4 = (gram_num*n-pgm41_num*pgm42_num)**2/(pgm41_num*pgm42_num*(n-pgm41_num)*(n-pgm42_num))
        pai = (pai1**2+pai2**2+pai3**2+pai4**2)/(pai1+pai2+pai3+pai4)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def sixFai(dic,n):
    with open('6gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('6fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
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
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pgm31_num = float(dic[pgm31])
        pgm32_num = float(dic[pgm32])
        pgm41_num = float(dic[pgm41])
        pgm42_num = float(dic[pgm42])
        pgm51_num = float(dic[pgm51])
        pgm52_num = float(dic[pgm52])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai3 = (gram_num*n-pgm31_num*pgm32_num)**2/(pgm31_num*pgm32_num*(n-pgm31_num)*(n-pgm32_num))
        pai4 = (gram_num*n-pgm41_num*pgm42_num)**2/(pgm41_num*pgm42_num*(n-pgm41_num)*(n-pgm42_num))
        pai5 = (gram_num*n-pgm51_num*pgm52_num)**2/(pgm51_num*pgm52_num*(n-pgm51_num)*(n-pgm52_num))
        pai = (pai1**2+pai2**2+pai3**2+pai4**2+pai5**2)/(pai1+pai2+pai3+pai4+pai5)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def sevenFai(dic,n):
    with open('7gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('7fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
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
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pgm31_num = float(dic[pgm31])
        pgm32_num = float(dic[pgm32])
        pgm41_num = float(dic[pgm41])
        pgm42_num = float(dic[pgm42])
        pgm51_num = float(dic[pgm51])
        pgm52_num = float(dic[pgm52])
        pgm61_num = float(dic[pgm61])
        pgm62_num = float(dic[pgm62])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai3 = (gram_num*n-pgm31_num*pgm32_num)**2/(pgm31_num*pgm32_num*(n-pgm31_num)*(n-pgm32_num))
        pai4 = (gram_num*n-pgm41_num*pgm42_num)**2/(pgm41_num*pgm42_num*(n-pgm41_num)*(n-pgm42_num))
        pai5 = (gram_num*n-pgm51_num*pgm52_num)**2/(pgm51_num*pgm52_num*(n-pgm51_num)*(n-pgm52_num))
        pai6 = (gram_num*n-pgm61_num*pgm62_num)**2/(pgm61_num*pgm62_num*(n-pgm61_num)*(n-pgm62_num))
        pai = (pai1**2+pai2**2+pai3**2+pai4**2+pai5**2+pai6**2)/(pai1+pai2+pai3+pai4+pai5+pai6)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def eightFai(dic,n):
    with open('8gramindexed.txt', 'r') as f:
        gram_content =  f.read().split('\n')
        gram_content =  [e for e in gram_content if len(e)>0]
    output = open('8fai.txt','w')
    for i in xrange(len(gram_content)):
        gram = gram_content[i].split('\t')
        gram_num = float(gram[1])
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
        pgm11_num = float(dic[pgm11])
        pgm12_num = float(dic[pgm12])
        pgm21_num = float(dic[pgm21])
        pgm22_num = float(dic[pgm22])
        pgm31_num = float(dic[pgm31])
        pgm32_num = float(dic[pgm32])
        pgm41_num = float(dic[pgm41])
        pgm42_num = float(dic[pgm42])
        pgm51_num = float(dic[pgm51])
        pgm52_num = float(dic[pgm52])
        pgm61_num = float(dic[pgm61])
        pgm62_num = float(dic[pgm62])
        pgm71_num = float(dic[pgm71])
        pgm72_num = float(dic[pgm72])
        pai1 = (gram_num*n-pgm11_num*pgm12_num)**2/(pgm11_num*pgm12_num*(n-pgm11_num)*(n-pgm12_num))
        pai2 = (gram_num*n-pgm21_num*pgm22_num)**2/(pgm21_num*pgm22_num*(n-pgm21_num)*(n-pgm22_num))
        pai3 = (gram_num*n-pgm31_num*pgm32_num)**2/(pgm31_num*pgm32_num*(n-pgm31_num)*(n-pgm32_num))
        pai4 = (gram_num*n-pgm41_num*pgm42_num)**2/(pgm41_num*pgm42_num*(n-pgm41_num)*(n-pgm42_num))
        pai5 = (gram_num*n-pgm51_num*pgm52_num)**2/(pgm51_num*pgm52_num*(n-pgm51_num)*(n-pgm52_num))
        pai6 = (gram_num*n-pgm61_num*pgm62_num)**2/(pgm61_num*pgm62_num*(n-pgm61_num)*(n-pgm62_num))
        pai7 = (gram_num*n-pgm71_num*pgm72_num)**2/(pgm71_num*pgm72_num*(n-pgm71_num)*(n-pgm72_num))
        pai = (pai1**2+pai2**2+pai3**2+pai4**2+pai5**2+pai6**2+pai7**2)/(pai1+pai2+pai3+pai4+pai5+pai6+pai7)
        output.write(gram[0]+'\t'+gram[1]+'\t'+str(pai))
        output.write('\n')
    output.close()

def fai(dic,n):
    twoFai(dic,n)
    threeFai(dic,n)
    fourFai(dic,n)
    fiveFai(dic,n)
    sixFai(dic,n)
    sevenFai(dic,n)
    eightFai(dic,n)