#!/usr/bin/env python
# coding: utf-8

# In[14]:


class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        CountVectorizer.token_index = {}

    def fit(self, corpus):
        self.corpus = corpus
        self.token_index = {}
        for part in self.corpus:
            index = 0
            while index <= len(part) - self.ngram_size:
                token = str(part[index : (index + self.ngram_size)])
                self.token_index.setdefault(token)
                index += 1
        self.token_index = dict(sorted(self.token_index.items()))
        value = 0
        for tokens in self.token_index:
            self.token_index[tokens] = value
            value += 1
        CountVectorizer.token_index = self.token_index
        return CountVectorizer.token_index
            
                
            

    def transform(self, corpus):
        self.corpus = corpus
        self.tokenized_corpus = []
        self.final_list = []
        for part in self.corpus:
            index = 0
            tokenized_string = []
            while index <= len(part) - self.ngram_size:
                token = str(part[index : (index + self.ngram_size)])
                tokenized_string.append(token)
                index += 1
            self.tokenized_corpus.append(tokenized_string)
        for part in self.tokenized_corpus:
            count_in_string = []
            for token in CountVectorizer.token_index:
                count = part.count(token)
                count_in_string.append(count)
            self.final_list.append(count_in_string)
        return self.final_list
            
            
        
            
                
    def fit_transform(self, corpus):
        self.corpus = corpus
        self.fit(corpus)
        return self.transform(corpus)


# In[15]:


import json


CORPUS = [
    'TTTCTGCCAATTCAGCGTGTCTCTAGAGGGTAGTCCACTTCTGAGCGCCCTCTGCAGGGCACCGCCTCATGTTACAGTGGAAACTGGCTCTGCTTTGAGGA',
    'CTTCTGGAGTGAGCTAAGCAGTTGGAGCCGTGGGTCTTCATGGCACACAGAGGTCTCGTGGAATGGGTAGTTAGGGAGGGCACCTGAGGGGAGGTGACTTT',
    'TCACCCATGCTGGAGTGCAGTGGCATGATCTCGGCTCACTGCAAGCTCCACCTCCCGGGTTCATGCCATTCTCCTGCCTCAGCCTCCCGAGTAGCTGGGAC',
    'GTCCCAGCTACGCGGCAGGCTGAGGCAGGAGAAAGGAGTGAACCCAGGAGGTGGAGCTTGCAGTGAGCGGACATCGCGCCACTGCACTCCCTCAGTCTCAA',
    'TCGCTCCCTGGGCTCCTGTGCGGCTCAAGCCTCCCGGACGAGCGCCGCCCCCTGCTCCACTGCGCCCAGTCCCATCTACCACCCAAGGGCTGGGGAGTGCG',
    'GCACCCCCTTGCCACAGTCTCATGAGTGCCCTTTGGTGTCCTGAGCGCCCCCTGGTGCTTCTGAGCACCCTCTGGTGTTCTGAGCACCCCCTGCTTCTTCT',
    'TCAGCATGAAGCCTGACGCCCAAACACCGTTTCCGGCCACAGAGGCGCCCTTTGGTTCTTAGTTTGCTAAGAACCTTTAAAAATCATAAATGAGGCCAGGC',
    'CGGCGCTCGCGCAGTTTTGAGAGAGGGTCCCGAAAACCGCCGGAGGCCAGGTGTCGCGGACGGGCCCCGGGCTAAACTCTCGTCTGGCGAAGTGAAGAGCG',
    'CCTGCCCAGCTCCTTGGCCTCAGACAATCTGGTTAACCGGAGGCCACAAGGTGGCACTGGTCCTTGCGTTGCTGGTCAGTGCGCACTGCAGCCTCATCCTG',
    'AGAGCTGGTGGACTTGGAACAGGAACAGTCTGCATGGCGTGACAGCGCCCTCTGCTGTCCAGGCTGGGCTGGCATCGATGGTACAGGAGGAGGGTGATCCT',
    'ACTGGCTCTTTCCAATAATGCTAATTATCTTATGACACTCTCCCACACCCTCTTTTTATTCCAGCCACCTATCCATTTTTATACTCATTGAACATGTTCAA',
]



def check():
    # test case #1
    try:
        for ngram_size in range(1, 10):
            vectorizer_1 = CountVectorizer(ngram_size=ngram_size)
            vectorizer_2 = CountVectorizer(ngram_size=ngram_size)

            vectorizer_1.fit(CORPUS)
            if vectorizer_1.transform(CORPUS) != vectorizer_2.fit_transform(CORPUS):
                return f'0\tFailed test #1.{ngram_size}. fit + transform should be equal to fit_transform. Please try again!'
    except Exception as e:
        return f'0\tFailed test #2. Please try again! {e}'

    # test case #2
    try:
        test_case_idx = 0
        for ngram_size in range(1, 20):
            vectorizer = CountVectorizer(ngram_size=ngram_size)

            for i in range(len(CORPUS) - 1):
                test_dataset = CORPUS[i:]
                if vectorizer.fit_transform(test_dataset) != test_2_answers[test_case_idx]:
                    return f'0\tFailed test #3.{ngram_size}.{i}. Incorrect answer. Please try again!'
                test_case_idx += 1

    except Exception as e:
        return f'0\tFailed test #4. Please try again! {e}'

    # test case #3
    try:
        test_case_idx = 0
        for ngram_size in range(1, 20):
            vectorizer = CountVectorizer(ngram_size=ngram_size)

            for i in range(1, len(CORPUS) - 1):
                train_dataset = CORPUS[:i]
                test_dataset = CORPUS[i:]

                vectorizer.fit(train_dataset)
                if vectorizer.transform(test_dataset) != test_3_answers[test_case_idx]:
                    return f'0\tFailed test #5.{ngram_size}.{i}. Incorrect answer. Please try again!'
                test_case_idx += 1

    except Exception as e:
        return f'0\tFailed test #6. Please try again! {e}'

    return '1\tGreat job! You passed all test cases.'


result, message = check().split('\t')
assert result == '1', message
print(message)


# In[ ]:




