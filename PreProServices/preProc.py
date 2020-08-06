import re
import pandas as pd
import numpy as np
import csv
import codecs

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
    # with open('./feili_main_corp.txt', mode='a', encoding='utf8') as mainTxt:

        with open('feili300.csv', 'w+', encoding='utf-8-sig', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Sentence #', 'Word', 'Tag'))
            flag = 0
            sentCounter = 1
            k = 100
            for t in range(1, 710):
                with open('../Files/2_feili/300K/'+str(t)+'.txt' , mode='r' , encoding='utf8') as ftxt:
                    line = ftxt.readline()
                    while line:
                        try:
                            if len(line) != 1:
                                w = ' '.join(line.split()[0:-1])
                                t = line.split()[-1]

                                if k == 100:
                                    s = 'Sentence: ' + str(1)
                                    print(s)
                                    writer.writerow((s, w, t))
                                else:
                                    if flag == 1:
                                        sentCounter += 1
                                        s = 'Sentence: ' + str(sentCounter)
                                        writer.writerow((s, w, t))
                                        flag = 0
                                    else:
                                        writer.writerow(('', w, t))
                                    if w == '!' or w == '?':
                                        flag = 1
                            else:
                                flag = 1
                        except(IndexError):
                            print(len(line))
                        k = 101
                        line = ftxt.readline()

def Feili_Corp2():
    files = os.listdir('../Files/2_feili/600K')
    with open('feili600.csv', 'w+', encoding='utf-8-sig', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Sentence #', 'Word', 'Tag'))
        flag = 0
        sentCounter = 10021
        for (index,file) in enumerate(files):
            with open('../Files/2_feili/600K/'+file , mode='r' , encoding='utf8') as ftxt:
                line = ftxt.readline()
                while line:
                    try:
                        if len(line) != 1:
                            w = ' '.join(line.split()[0:-1])
                            t = line.split()[-1].replace('-','_')

                            if flag == 1:
                                sentCounter += 1
                                s = 'Sentence: ' + str(sentCounter)
                                writer.writerow((s, w, t))
                                flag = 0
                            else:
                                writer.writerow(('', w, t))
                            if w == '!' or w == '?':
                                flag = 1
                        else:
                            flag = 1
                    except(IndexError):
                        print(len(line))
                    line = ftxt.readline()


def create_main_file():
    with open('main_corp2.txt',mode='w+',encoding='utf-8')as main:
        with open('arman_main_corp.txt', mode='r', encoding='utf-8')as armin:
            line1 = armin.readline()
            while line1:
                line10 = line1.split()[0]
                line12 = ' '.join(line1.split()[1:])
                main.write(line12+' '+line10+'\n')
                line1 = armin.readline()
        with open('feili_main_corp.txt', mode='r', encoding='utf-8')as feili1:
            line2 = feili1.readline()
            while line2:
                line20 = line2.split()[0]
                line22 = ' '.join(line2.split()[1:])

                main.write(line20 + ' ' + line22 + '\n')
                line2 = feili1.readline()
        with open('feili600_main_corp.txt', mode='r', encoding='utf-8')as feili2:
            line3 = feili2.readline()
            while line3:
                line30 = line3.split()[0]
                line32 = ' '.join(line3.split()[1:])
                main.write(line30 + ' ' + line32 + '\n')
                line3 = feili2.readline()

def create_csv():
    with open('main_corp2.txt', 'r',encoding='utf-8') as in_file:

        line = in_file.readline().replace('\n','')
        with open('main_corp.csv', 'w+',encoding='utf-8-sig',newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Word', 'Tag'))
            while line:
                w = ' '.join(line.split()[1:])
                t = line.split()[0]
                writer.writerow((w,t))

                # if len(line.split()) > 2:
                #     writer.writerow((line.split()[-1], line[:-1]))
                # else:
                #     try:
                #         writer.writerow(((line.split()[1]),(line.split()[0])))
                #     except(UnicodeEncodeError):
                #         print(line)
                line = in_file.readline().replace('\n','')



# create_main_file()
Feili_Corp()
