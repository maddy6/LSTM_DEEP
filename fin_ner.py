# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:57:07 2019

@author: mayur.v
"""

import nltk
import re
import numpy as np
import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.tree import Tree
from nltk import everygrams
from fuzzywuzzy import fuzz
from fuzzywuzzy import process 
import sys

## Read Input data files
df = pd.read_csv(sys.argv[1], delimiter = ',',encoding = 'latin1',error_bad_lines=False)
#df = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/Issue Trending/Issue Trending/EBS_PGT25.csv",delimiter = ',',encoding = 'latin1')

df1 = pd.read_csv(sys.argv[2], delimiter = ',',encoding = 'latin1',error_bad_lines=False)
#df1 = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/Issue Trending/Issue Trending/Instrument List.csv",delimiter = ',',encoding = 'latin1')

df2 = pd.read_csv(sys.argv[3], delimiter = ',',encoding = 'latin1',error_bad_lines=False)
#df2 = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/Issue Trending/Issue Trending/Equipment List.csv",delimiter = ',',encoding = 'latin1')


## Unique list function

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        return(x)

##### Processing on EBS Input Data file to extract dump of unique keywords
   
iob_tagged = []
for i in range(0,len(df['PMHD_TA004_SYS_T_DES'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df['PMHD_TA004_SYS_T_DES'][i])))
    iob_tagged.append(tree2conlltags(ne_tree))
    

s1 = []
for i in range(0,len(iob_tagged)):
    s1.append([i[0] for i in iob_tagged[i]])
  
s2 = []
for i in range(0,len(iob_tagged)):
    s2.append([i[1] for i in iob_tagged[i]])
  
s3 = []
for i in range(0,len(iob_tagged)):
    s3.append([i[2] for i in iob_tagged[i]])

s01 = []
for i in range(0,len(s1)):
    s01.append(set(s1[i]))
    
s11 = []
for i in range(0,len(s2)):
    s11.append(set(s2[i]))

s22 = []
for i in range(0,len(s3)):
    s22.append(set(s3[i]))

s_l01 = unique(s01)
s_l1 = unique(s11)
s_l2 = unique(s22)


fin_pos = []
for i in range(0,len(iob_tagged)):     
        #print(i)
        if len(iob_tagged[i])==0:
            fin_pos.append('')
        else:
            fin_pos.append(list(zip(*iob_tagged[i]))[0])
  
unique_data = [list(x) for x in set(tuple(x) for x in fin_pos)]
                  
sa = ' '.join(str(r) for v in unique_data for r in v)
sa = set(sa.split(' '))

#### Processing on EBS Input Data file to extract dump of unique keywords

iob_tagged1 = []
for i in range(0,len(df['PMHD_TA005_GRP_T_DES'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df['PMHD_TA005_GRP_T_DES'][i])))
    iob_tagged1.append(tree2conlltags(ne_tree))
    

r1 = []
for i in range(0,len(iob_tagged1)):
    r1.append([i[0] for i in iob_tagged1[i]])
  
r2 = []
for i in range(0,len(iob_tagged1)):
    r2.append([i[1] for i in iob_tagged1[i]])
  
r3 = []
for i in range(0,len(iob_tagged1)):
    r3.append([i[2] for i in iob_tagged1[i]])

r01 = []
for i in range(0,len(r1)):
    r01.append(set(r1[i]))
    
r11 = []
for i in range(0,len(r2)):
    r11.append(set(r2[i]))

r22 = []
for i in range(0,len(r3)):
    r22.append(set(r3[i]))

r_l01 = unique(r01)    
r_l1 = unique(r11)
r_l2 = unique(r22)

fin_pos1 = []
for i in range(0,len(iob_tagged1)):     
        #print(i)
        if len(iob_tagged1[i])==0:
            fin_pos1.append('')
        else:
            fin_pos1.append(list(zip(*iob_tagged1[i]))[0])
            

unique_data1 = [list(x) for x in set(tuple(x) for x in fin_pos1)]

sa1 = ' '.join(str(r) for v in unique_data1 for r in v)
sa1 = set(sa1.split(' '))          

##### Processing on Instrument list Input Data file to extract dump of unique keywords

iob_tagged2 = []
for i in range(0,len(df1['System code'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df1['System code'][i])))
    iob_tagged2.append(tree2conlltags(ne_tree))

    
t1 = []
for i in range(0,len(iob_tagged2)):
    t1.append([i[0] for i in iob_tagged2[i]])
  
t2 = []
for i in range(0,len(iob_tagged2)):
    t2.append([i[1] for i in iob_tagged2[i]])
  
t3 = []
for i in range(0,len(iob_tagged2)):
    t3.append([i[2] for i in iob_tagged2[i]])
 
t01 = []
for i in range(0,len(t1)):
    t01.append(set(t1[i]))
    
t11 = []
for i in range(0,len(t2)):
    t11.append(set(t2[i]))

t22 = []
for i in range(0,len(t3)):
    t22.append(set(t3[i]))

t_l01 = unique(t01)   
t_l1 = unique(t11)
t_l2 = unique(t22)

fin_pos2 = []
for i in range(0,len(iob_tagged2)):     
        #print(i)
        if len(iob_tagged2[i])==0:
            fin_pos2.append('')
        else:
            fin_pos2.append(list(zip(*iob_tagged2[i]))[0])
    
unique_data2 = [list(x) for x in set(tuple(x) for x in fin_pos2)]

sa2 = ' '.join(str(r) for v in unique_data2 for r in v)
sa2 = set(sa2.split(' ')) 

#### Processing on Instrument list Input Data file to extract dump of unique keywords

iob_tagged3 = []
for i in range(0,len(df1['Type desc.'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df1['Type desc.'][i])))
    iob_tagged3.append(tree2conlltags(ne_tree))

    
u1 = []
for i in range(0,len(iob_tagged3)):
    u1.append([i[0] for i in iob_tagged3[i]])
  
u2 = []
for i in range(0,len(iob_tagged3)):
    u2.append([i[1] for i in iob_tagged3[i]])
  
u3 = []
for i in range(0,len(iob_tagged3)):
    u3.append([i[2] for i in iob_tagged3[i]])
 
u01 = []
for i in range(0,len(u1)):
    u01.append(set(u1[i]))
    
u11 = []
for i in range(0,len(u2)):
    u11.append(set(u2[i]))

u22 = []
for i in range(0,len(u3)):
    u22.append(set(u3[i]))

u_l01 = unique(u01)   
u_l1 = unique(u11)
u_l2 = unique(u22)

fin_pos3 = []
for i in range(0,len(iob_tagged3)):     
        #print(i)
        if len(iob_tagged3[i])==0:
            fin_pos3.append('')
        else:
            fin_pos3.append(list(zip(*iob_tagged3[i]))[0])
            
unique_data3 = [list(x) for x in set(tuple(x) for x in fin_pos3)]

sa3 = ' '.join(str(r) for v in unique_data3 for r in v)
sa3 = set(sa3.split(' ')) 
        
#### Processing on Instrument list Input Data file to extract dump of unique keywords

iob_tagged4 = []
for i in range(0,len(df1['Service'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df1['Service'][i])))
    iob_tagged4.append(tree2conlltags(ne_tree))

    
v1 = []
for i in range(0,len(iob_tagged4)):
    v1.append([i[0] for i in iob_tagged4[i]])
  
v2 = []
for i in range(0,len(iob_tagged4)):
    v2.append([i[1] for i in iob_tagged4[i]])
  
v3 = []
for i in range(0,len(iob_tagged4)):
    v3.append([i[2] for i in iob_tagged4[i]])
 
v01 = []
for i in range(0,len(v1)):
    v01.append(set(v1[i]))
    
v11 = []
for i in range(0,len(v2)):
    v11.append(set(v2[i]))

v22 = []
for i in range(0,len(v3)):
    v22.append(set(v3[i]))

v_l01 = unique(v01) 
v_l1 = unique(v11)
v_l2 = unique(v22)

fin_pos4 = []
for i in range(0,len(iob_tagged4)):     
        #print(i)
        if len(iob_tagged4[i])==0:
            fin_pos4.append('')
        else:
            fin_pos4.append(list(zip(*iob_tagged4[i]))[0])
            
unique_data4 = [list(x) for x in set(tuple(x) for x in fin_pos4)]

sa4 = ' '.join(str(r) for v in unique_data4 for r in v)
sa4 = set(sa4.split(' ')) 
           
#### Processing on Equipment list Input Data file to extract dump of unique keywords


df2['Description'] = df2['Description'].replace(np.nan, 'NA', regex=True)
iob_tagged5 = []
for i in range(0,len(df2['Description'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df2['Description'][i])))
    iob_tagged5.append(tree2conlltags(ne_tree))

    
a1 = []
for i in range(0,len(iob_tagged5)):
    a1.append([i[0] for i in iob_tagged5[i]])
  
a2 = []
for i in range(0,len(iob_tagged5)):
    a2.append([i[1] for i in iob_tagged5[i]])
  
a3 = []
for i in range(0,len(iob_tagged5)):
    a3.append([i[2] for i in iob_tagged5[i]])
 
a01 = []
for i in range(0,len(a1)):
    a01.append(set(a1[i]))
    
a11 = []
for i in range(0,len(a2)):
    a11.append(set(a2[i]))

a22 = []
for i in range(0,len(a3)):
    a22.append(set(a3[i]))

a_l01 = unique(a01) 
a_l1 = unique(a11)
a_l2 = unique(a22)

fin_pos5 = []
for i in range(0,len(iob_tagged5)):     
        #print(i)
        if len(iob_tagged5[i])==0:
            fin_pos5.append('')
        else:
            fin_pos5.append(list(zip(*iob_tagged5[i]))[0])

unique_data5 = [list(x) for x in set(tuple(x) for x in fin_pos5)]

sa5 = ' '.join(str(r) for v in unique_data5 for r in v)
sa5 = set(sa5.split(' ')) 

#### Processing on Eqipment list Input Data file to extract dump of unique keywords

df2['Type'] = df2['Type'].replace(np.nan, 'NA', regex=True)
iob_tagged6 = []
for i in range(0,len(df2['Type'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df2['Type'][i])))
    iob_tagged6.append(tree2conlltags(ne_tree))

    
b1 = []
for i in range(0,len(iob_tagged6)):
    b1.append([i[0] for i in iob_tagged6[i]])
  
b2 = []
for i in range(0,len(iob_tagged6)):
    b2.append([i[1] for i in iob_tagged6[i]])
  
b3 = []
for i in range(0,len(iob_tagged6)):
    b3.append([i[2] for i in iob_tagged6[i]])
 
b01 = []
for i in range(0,len(b1)):
    b01.append(set(b1[i]))
    
b11 = []
for i in range(0,len(b2)):
    b11.append(set(b2[i]))

b22 = []
for i in range(0,len(b3)):
    b22.append(set(b3[i]))

b_l01 = unique(b01) 
b_l1 = unique(b11)
b_l2 = unique(b22)


fin_pos6 = []
for i in range(0,len(iob_tagged6)):     
        #print(i)
        if len(iob_tagged6[i])==0:
            fin_pos6.append('')
        else:
            fin_pos6.append(list(zip(*iob_tagged6[i]))[0])

unique_data6 = [list(x) for x in set(tuple(x) for x in fin_pos6)]

sa6 = ' '.join(str(r) for v in unique_data6 for r in v)
sa6 = set(sa6.split(' '))             

#### Processing on Eqipment list Input Data file to extract dump of unique keywords

df2['Sys. Name'] = df2['Sys. Name'].replace(np.nan, 'NA', regex=True)
iob_tagged7 = []
for i in range(0,len(df2['Sys. Name'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df2['Sys. Name'][i])))
    iob_tagged7.append(tree2conlltags(ne_tree))

    
c1 = []
for i in range(0,len(iob_tagged7)):
    c1.append([i[0] for i in iob_tagged7[i]])
  
c2 = []
for i in range(0,len(iob_tagged7)):
    c2.append([i[1] for i in iob_tagged7[i]])
  
c3 = []
for i in range(0,len(iob_tagged7)):
    c3.append([i[2] for i in iob_tagged7[i]])
 
c01 = []
for i in range(0,len(c1)):
    c01.append(set(c1[i]))
    
c11 = []
for i in range(0,len(c2)):
    c11.append(set(c2[i]))

c22 = []
for i in range(0,len(c3)):
    c22.append(set(c3[i]))

c_l01 = unique(c01) 
c_l1 = unique(c11)
c_l2 = unique(c22)

fin_pos7 = []
for i in range(0,len(iob_tagged7)):     
        #print(i)
        if len(iob_tagged7[i])==0:
            fin_pos7.append('')
        else:
            fin_pos7.append(list(zip(*iob_tagged7[i]))[0])

unique_data7 = [list(x) for x in set(tuple(x) for x in fin_pos7)]

sa7 = ' '.join(str(r) for v in unique_data7 for r in v)
sa7 = set(sa7.split(' '))   
sa7 = tuple(sa7)

### keywords extracted from from all input files.

from itertools import chain
key_dump = set(chain(sa,sa1,sa2,sa3,sa4,sa5,sa6,sa7))
key_dump = tuple(key_dump)
key_dump = [w.lower() for w in key_dump]

##### Processing on BHGE main Input Data file to extract Named Entities

#df_fin = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/BHGE_Dataset.csv",delimiter = ',',encoding = 'latin1')
df_fin = pd.read_csv(sys.argv[4],delimiter = ',',encoding = 'latin1')


def pre_process(text):
    
    #remove tags
    text=re.sub("(\\d|\\W)+"," ",text)
    
    #text = re.sub(r'\b[A-Z]+\b', '', text)

    text = ' '.join( [w for w in text.split() if len(w)>2] )
    # remove special characters and digits
    
    return text
    
df_fin['Problem Description'] = df_fin['Problem Description'].apply(lambda x:pre_process(x))

list_pos = []
for i in range(0,len(df_fin['Problem Description'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df_fin['Problem Description'][i])))
    list_pos.append(tree2conlltags(ne_tree))


pos_1 = []
for i in range(0,len(list_pos)):
    #print(i)
    pos_1.append(list(filter(lambda x: (x[1] == 'NNP' or x[1] == 'VBG' or x[1] == 'NNS') and (x[2] == 'O' or x[2] == 'I-PERSON' or x[2] == 'B-PERSON'), list_pos[i])))

    
pos = []
for i in range(0,len(list_pos)):
    #print(i)
    pos.append(list(filter(lambda x: (x[1] == 'NNP' or x[1] == 'NN' or x[1] == 'VBP' or x[1] == 'CC' or x[1] == 'NNS' or x[1] == 'VBG' or x[1] == 'VBP' or x[1] == 'DT' or x[1] == 'JJ' or x[1] == 'IN') and
                                     (x[2] == 'O' or x[2] == 'B-ORGANIZATION' or x[2] == 'B-GPE' or x[2] == 'B-GSP' or x[2] == 'B-GPE' or x[2] == 'I-PERSON' or x[2] == 'B-PERSON'),
                                      list_pos[i])))
    
fin_pos_df = []
for i in range(0,len(pos)):
        #print(i)
        if len(pos[i])==0:
            fin_pos_df.append('')
        else:
            fin_pos_df.append(list(zip(*pos[i]))[0])
            

ds = [[x.lower()  for x in element] for element in fin_pos_df]

fin_key_pos = []
for i in range(0,len(ds)):
    #print(i)
    fin_key_pos.append(list(set(ds[i])&set(key_dump)))


fin_key_pos_f1 = []
for i in range(0,len(ds)):
    #print(i)
    fin_key_pos_f1.append(list(set(fin_key_pos[i]+ds[i])))


Fin_Named_Entity_list_11 = [] 
for i in range(0,len(fin_key_pos_f1)):
    #print(i)
    Fin_Named_Entity_list_11.append(' '.join(fin_key_pos_f1[i]))
    
# Remove Stopword 
stop_words = set(stopwords.words('english')) 

word_tok = [] 
for i in range(0,len(Fin_Named_Entity_list_11)):
    #print(i)
    word_tok.append(word_tokenize(Fin_Named_Entity_list_11[i]))
  
# Domain specific stopwords
stop = ['and','number','all','look','note','like','attache','consist','once','suitable','enclosure','some','request','kindly','kind','please','are','eps','from','with',
        'uld','used','additional','iecx','upon','able','oct','order','pgt','details','bhge','while','both','ptg','furthermore','current','gtg','fuond','allowing','tomorrow','observations','iecex','doesnt','does','cpy','list','attach','reach','withouts','fact','expected',
        'or','the','for','have','way','due','therefore','true','matching','between','equal','valid','validity','arrangement','proven','sep','aplng','further',
        'cant','running','form','types','site','found','other','attempts','several','despite','believe','above','into','hence','kindly','this','name','sac','dear',
        'providing','need','pre','that','after','but','provide','ready','days','per','reply','From','Considering','considering','allow',
        'approval','confirm','otherwise','around','differences','among','view','information','customer','total','desired','against','according','present','your','house','anything','following','requriment','taken',
        'april','about','regards','actual','regarding','today','year','inhibit','similar','different','updated','first','attachment','next','some',
        'need','during','mkvie','purpose','putting', 'bring','thanks','such','various','able','reference','readings','permited','using','call','could','required','neither','mismatch','comparing','require','every','projects','documents','possible','particular','section','thing','improve','because','top','items','item','detail','since','any','advise','want','info','email','som','below','further','see','new','use','page','same','each','attached','refer','check','without','pictures','feedback',
        'ourselves', 'hers', 'between', 'yourself','followings', 'but', 'again', 'there', 'about', 'once', 'during','understand',
        'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
        'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
        'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
        'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their',
        'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 
        'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then',
        'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you',
        'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
        'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further',
        'was', 'here', 'than']


ner_sentence = []
for i in range(0,len(word_tok)): 
    ner_sentence.append([i for i in word_tok[i] if i not in stop])

ner_sentence1 = [] 
for i in range(0,len(ner_sentence)):
    #print(i)
    ner_sentence1.append(' '.join(ner_sentence[i]))

         
DF_NER = pd.DataFrame(ner_sentence1)
df_fin['Named_Entity'] = DF_NER

##### Processing on BHGE main Input Data file to extract dump of unique keywords

#df_fin = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/BHGE_Dataset.csv",delimiter = ',',encoding = 'latin1')
#df_fin = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/BHGE_Dataset.csv",delimiter = ',',encoding = 'latin1')

df_fin['Expected Deliverable and proposed solution'] = df_fin['Expected Deliverable and proposed solution'].replace(np.nan, 'NA', regex=True)

df_fin['Expected Deliverable and proposed solution'] = df_fin['Expected Deliverable and proposed solution'].apply(lambda x:pre_process(x))


### extarct named entities

list_pos_e1 = []
for i in range(0,len(df_fin['Expected Deliverable and proposed solution'])):
    #print(i)
    ne_tree = ne_chunk(pos_tag(word_tokenize(df_fin['Expected Deliverable and proposed solution'][i])))
    list_pos_e1.append(tree2conlltags(ne_tree))


pos_e1 = []
for i in range(0,len(list_pos_e1)):
    #print(i)
    pos_e1.append(list(filter(lambda x: (x[1] == 'NNP' or x[1] == 'NN' or x[1] == 'VBP' or x[1] == 'CC' or x[1] == 'NNS' or x[1] == 'VBG' or x[1] == 'VBP' or x[1] == 'DT' or x[1] == 'JJ' or x[1] == 'IN') and
                                     (x[2] == 'O' or x[2] == 'B-ORGANIZATION' or x[2] == 'B-GPE' or x[2] == 'B-GSP' or x[2] == 'B-GPE' or x[2] == 'I-PERSON' or x[2] == 'B-PERSON'),
                                      list_pos_e1[i])))

   
fin_pos_df_e1 = []
for i in range(0,len(pos_e1)):
        #print(i)
        if len(pos_e1[i])==0:
            fin_pos_df_e1.append('')
        else:
            fin_pos_df_e1.append(list(zip(*pos_e1[i]))[0])
            

ds = [[x.lower()  for x in element] for element in fin_pos_df_e1]

fin_key_pos = []
for i in range(0,len(ds)):
    #print(i)
    fin_key_pos.append(list(set(ds[i])&set(key_dump)))


fin_key_pos_ee1 = []
for i in range(0,len(ds)):
    #print(i)
    #fin_key_pos_f1.append(list(set(fin_key_pos[i]+ds[1])))
    fin_key_pos_ee1.append(list(set(fin_key_pos[i]+ds[i])))

Fin_Named_Entity_list_e1 = [] 
for i in range(0,len(fin_key_pos_ee1)):
    #print(i)
    Fin_Named_Entity_list_e1.append(' '.join(fin_key_pos_ee1[i]))
    
word_tok_e1 = [] 
for i in range(0,len(Fin_Named_Entity_list_e1)):
    #print(i)
    word_tok_e1.append(word_tokenize(Fin_Named_Entity_list_e1[i]))
    

ner_sentence_e1 = []
for i in range(0,len(word_tok_e1)): 
    ner_sentence_e1.append([i for i in word_tok_e1[i] if i not in stop])

    
ner_sentence1_e1 = [] 
for i in range(0,len(ner_sentence_e1)):
    #print(i)
    ner_sentence1_e1.append(','.join(ner_sentence_e1[i]))

         
DF_NER1 = pd.DataFrame(ner_sentence1_e1)
df_fin['Named_Entity_Expected Deliverable_and proposed solution'] = DF_NER1
#df_fin.to_csv('C:/Users/mayur.v/Desktop/BHGE/Named_Entity_Model_New_v3.2.csv')

## Maaping of extracted entities with EBS list
#sys.argv[0]
#df3 = pd.read_csv("C:/Users/mayur.v/Desktop/BHGE/Issue Trending/Issue Trending/EBS_PGT25.csv",delimiter = ',',encoding = 'latin1')

## pre-processing function
def pre_process1(text):
    
    #remove tags
    text=re.sub("(\\d|\\W)+"," ",text)
    
    text = re.sub(r'(|)', '', text)

    #text = ' '.join( [w for w in text.split() if len(w)>2] )

    return text
    
df['PMHD_TA005_GRP_T_DES'] = df['PMHD_TA005_GRP_T_DES'].apply(lambda x:pre_process(x))

        
compo_list = []
for i in range(0,len(df['PMHD_TA005_GRP_T_DES'])):
    #print(i)
    compo_list.append(df['PMHD_TA005_GRP_T_DES'][i])
    
compo_list = [x.lower() for x in compo_list]

mapped_entities = []       
for i in range(0,len(df_fin['Named_Entity'])):
    #print(i)
    mapped_entities.append(set(process.extract(df_fin['Named_Entity'][i], compo_list, limit=5)))

mapped_entities_list = list(mapped_entities)

extracted_ner_entities = []
for i in range(0,len(mapped_entities_list)):
    #print(i)
    extracted_ner_entities.append(''.join(str(mapped_entities_list[i])))

    
extracted_ner = pd.DataFrame(extracted_ner_entities)
df_fin['Named_Entity_EBS_Mapping'] = extracted_ner
df_fin.to_csv(sys.argv[4])
