#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import re
from urllib.parse import urlencode
import requests
from alphabet_detector import AlphabetDetector

ad = AlphabetDetector()

babelnet_key=''

#log for english words done
done_english_words=open("done_english","w")

#log for arabic words done
done_arabic_words=open("done_arabic","w")

#log for french words done
done_french_words=open("done_french","w")

#open the list of words to process with babelnet api
file_of_words=open("test_dict","r")
list_of_words = file_of_words.read().splitlines()

for word in list_of_words :
    print("I am processing the word "+word)
    #encoding the word for url processing
    word1=urlencode({'params': word})
    word2=re.sub(r"params=", '', word1)
    url='http://babelnet.io/v5/getSynsetIds?lemma='+word2+'&searchLang=FR&&pos=NOUN&key='+babelnet_key

    #writing english words
    outfile_eng=open("out_eng_"+word,"w")
    
    #writing arabic words
    outfile_arabic=open("out_ara_"+word,"w")

    #writing french words
    outfile_french=open("out_fre_"+word,"w")
    
    #launch the query for getting synsetIds
    requests.get(url)
    #getting the responses of the query
    response = requests.get(url)
    responseObject=response.json()

    eng_words_list=[] #list to save the respons of each query for a word
    for e in responseObject:
        #get english synsets
        res_eng=requests.get('https://babelnet.io/v5/getSynset?id='+e['id']+'&targetLang=EN&key='+babelnet_key)
        #getting responses in json
        responseObject_eng = res_eng.json()
        #getting fullLamma for each word                      
        for element in responseObject_eng.get('senses'):
            k=element.get("properties")
            w=k.get("fullLemma").lower()             
            if w not in eng_words_list:
                eng_words_list.append(w)            
    
    fr_words_list=[]#list to save the respons of each query for a word
    for e in responseObject:
        #get french synsets
        res_fr=requests.get('https://babelnet.io/v5/getSynset?id='+e['id']+'&targetLang=FR&key='+babelnet_key)
        #getting responses in json
        responseObject_fr = res_fr.json()
        #getting fullLamma for each word                     
        for element in responseObject_fr.get('senses'):
            k=element.get("properties")
            w=k.get("fullLemma").lower()             
            if w not in fr_words_list:
                fr_words_list.append(w)        
    
    arabic_words_list=[]#list to save the respons of each query for a word
    for e in responseObject:
        #get arabic synsets
        res_ara=requests.get('https://babelnet.io/v5/getSynset?id='+e['id']+'&targetLang=AR&key='+babelnet_key)
        #print('https://babelnet.io/v5/getSynset?id='+e['id']+'&targetLang=AR&key='+babelnet_key)
        #getting responses in json
        responseObject_arabic = res_ara.json() 
        #getting fullLamma for each word                   
        for element in responseObject_arabic.get('senses'):
            latin_check = re.compile(r'[a-z]')
            k=element.get("properties")
            w=k.get("fullLemma").lower()
            if ad.is_latin(w) is False:                     
                if w not in arabic_words_list:
                    arabic_words_list.append(w)
    
    #writing words treated for english
    for e in eng_words_list:
        outfile_eng.write(e+"\n")   
    done_english_words.write(word+"\n")

    #writing words treated for arabic
    for e in arabic_words_list:
        outfile_arabic.write(e+"\n")   
    done_arabic_words.write(word+"\n")
 
    #writing words treated for french
    for e in fr_words_list:
        outfile_french.write(e+"\n")
    done_french_words.write(word+"\n") 

    

        




