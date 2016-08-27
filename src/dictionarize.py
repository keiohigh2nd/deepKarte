# -*- coding: utf-8 -*-

def vec(arr):
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(min_df=1)
        X = vectorizer.fit_transform(arr)
        index = vectorizer.get_feature_names()
        return X.toarray(), index

def vec_oneword(arr):
        #vectorizer.transform(['Something completely new.']).toarray()
        #入ってきたカルテをvector化する
        from sklearn.feature_extraction.text import CountVectorizer
        #vectorizer = CountVectorizer(analyzer = 'char_wb', ngram_range=(0, 1))
        vectorizer = CountVectorizer(analyzer = 'word', ngram_range=(0, 1), token_pattern=u'(?u)\\b\\w+\\b', stop_words=["."] )
        X = vectorizer.fit_transform(arr)
        index = vectorizer.get_feature_names()
        return X.toarray(), index
