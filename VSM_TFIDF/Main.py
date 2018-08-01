#import library pandas dan inisialisasikan menjadi pd
import pandas as pd
#import library numpy dan inisialisasikan menjadi np
import numpy as np
#dari library math import function log
from math import log


#hapus seluruh tanda baca dan angka
def removeNonWord(doc):
    #hapus seluruh kata yang mengandung angka, contoh: perempuan2
    result = doc.replace({'\w*\d\w*': ''}, regex=True)
    #hapus seluruh karakter yang tidak termasuk alphabet
    result = result.replace({'[\W_]+': ' '}, regex=True)
    #remove null dari hasil final
    return result[result.notnull()]

def idf(doc, wordBank):
    #hitung jumlah doc
    N = len(doc.index)
    #buat dataframe dengan header word dan idf
    result = pd.DataFrame(columns=['word', 'idf'])
    #untuk setiap kata pada wordBank lakukan.....
    for index, word in wordBank.iterrows():
        #hitung jumlah doc yang mengandung kata word['words']
        dft = np.sum(doc.str.contains(word['words']))
        #hitung inverse document frequency smooth
        idft = log(N / (dft + 1), 10)
        #tambahkan idf untuk setiap kata pada data frame
        result = result.append(pd.Series([word['words'],  idft], index=['word', 'idf']), ignore_index=True)
    #return variable result
    return result


#funtion to calculate tf
def tf(doc, wordBank):
    #split kata berdasarkan spasi
    wordList = doc.str.split(' ')
    #hitung jumlah kata pada setiap doc
    maxFt = [len(s)  for s in wordList]
    #buat DataFrame kosong untuk menyimpan hasil perhitungan Tf
    result = pd.DataFrame()
    #untuk setiap word dalam wordbank lakukan ....
    for index, word in wordBank.iterrows():
        #hitung frekuensi kata untuk setiap doc
        ft = np.add([s.count(word['words']) for s in wordList], 0)
        #tf log normalization
        ftd = 1 + np.log10(ft)
        #tambahkan hasil perhitungan tf kedalam DataFrame
        result = result.append(pd.Series(ftd), ignore_index=True)
    #replace -inf with zero
    result = result.replace(-np.inf, 0)
    #return variable result
    return result

def tfIdf(tf, idf):
    #buat DataFrame kosong untuk menyimpan hasil perhitungan Tf-Idf
    result = pd.DataFrame()
    #untuk setiap tf
    for i in tf:
        #tf idf untuk document term weighting tf * idf
        tfIdf = tf[i] * idf['idf']
        #tambahkan hasil perhitungan tf idf kedalam DataFrame
        result = result.append(pd.Series(tfIdf), ignore_index=True)
    #return variable result
    return result



# membaca file doc.csv menggunakan pandas
# doc.csv berisi 10 kalimat
doc = pd.read_csv('data/doc.csv', encoding='utf-8')

# membaca file wordBank.csv
# wordBank.csv berisi kata-kata penting atau keywords yang dianggap relevan dengan topik dalam sebuah kasus
vocabulary = pd.read_csv('data/wordBank.csv', encoding='utf-8')


#ubah seluruh huruf menjadi huruf kecil
doc = doc['sentences'].str.lower()

#panggil fungsi removeNonWord
doc = removeNonWord(doc)

#hitung nilai IDF
resultIDF = idf(doc, vocabulary)

#hitung nilai TF
resultTF = tf(doc, vocabulary)

#hitung nilai Tf-Idf
resultTfIdf = tfIdf(resultTF, resultIDF)

print(resultTfIdf)
