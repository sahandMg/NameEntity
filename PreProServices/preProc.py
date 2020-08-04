import re
import os
def Arman_Corp():
    with open('./arman_main_corp.txt', mode='a', encoding='utf8') as mainTxt:
        for i in range(1,3):
            with open('../Files/1_ArmanPersoNERCorpus/test_fold'+str(i)+'.txt',mode='r',encoding='utf-8') as txt:
                line = txt.readline()
                while line:
                    if line.rstrip():
                        if len(line.split()) > 2:
                            line = (line.split()[0]).replace('-','_').upper() + ' ' + line[1:]

                        else:
                            line = line.split()[0] + ' ' + line.split()[1].replace('-','_').upper()
                        mainTxt.write(line+'\n')
                    line = txt.readline()
            txt.close()
    mainTxt.close()

def Feili_Corp():
    with open('./feili_main_corp.txt', mode='a', encoding='utf8') as mainTxt:
        for t in range(1, 710):
            with open('../Files/2_feili/300K/'+str(t)+'.txt' , mode='r' , encoding='utf8') as ftxt:
                line = ftxt.readline()
                while line:
                    if line.rstrip():
                        if len(line.split()) > 2:
                            line = line.split()[-1] + ' '+line[:-2]

                        else:
                            line = line.split()[1]+' '+line.split()[0]
                        mainTxt.write(line+'\n')
                    line = ftxt.readline()
            ftxt.close()
    mainTxt.close()

def Feili_Corp2():
    files = os.listdir('../Files/2_feili/600K')
    with open('./feili600_main_corp.txt', mode='a', encoding='utf8') as mainTxt:
        for (index,file) in enumerate(files):
            for t in range(1, 710):
                with open('../Files/2_feili/600K/'+file , mode='r' , encoding='utf8') as ftxt:
                    line = ftxt.readline()
                    while line:
                        if line.rstrip():
                            try:
                                if len(line.split()) > 2:
                                    line = line.split()[-1] + ' '+(line.split()[:-2]).replace('-','_').upper()
                                else:
                                    line = line.split()[1]+' '+(line.split()[0]).replace('-','_').upper()
                            except(IndexError):
                                print(line+file)
                            mainTxt.write(line+'\n')
                        line = ftxt.readline()
                ftxt.close()
    mainTxt.close()

Feili_Corp2()
print(os.listdir('../Files/2_feili/600K'))