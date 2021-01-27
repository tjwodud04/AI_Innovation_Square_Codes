from konlpy.tag import Kkma

ma = Kkma()
#print(ma.pos('오늘은 금요일입니다'))

from konlpy.corpus import kolaw

#kolaw.fileids()
#c = kolaw.open(kolaw.fileids()[0]).read()

#print(len(c.split()))
#print(len(c.splitlines()))
#print(c.splitlines()[:3])

import nltk

#nltk.download('brown')
#nltk.download('gutenberg')

from nltk.corpus import brown, gutenberg

'''
corpus = brown.open(brown.fileids()[0]).read()
len(brown.fileids())
print(len(corpus))
print(corpus.split())
print(len(corpus.splitlines()))
print(corpus.splitlines()[:3])
'''
corpus = gutenberg.open(gutenberg.fileids()[0]).read()
#print(len(gutenberg.fileids()))
#print(len(corpus))
#print(corpus.split())
#print(len(corpus.splitlines()))
#print(corpus.splitlines()[:3])

#nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize
'''
sentence = sent_tokenize(corpus)
print(len(corpus.splitlines()))
print(len(sentence))
print(sentence[:3])
print(corpus.splitlines()[:3])
'''
morphemes = list()
for sentence in sent_tokenize(corpus):
    morphemes.extend(ma.morphs(sentence))

corpus = '''
(서울=뉴스1) 이기림 기자 = 성리학을 발전시키고, 후학을 양성한 조선시대 교육기관 '한국의 서원'이 유네스코 세계유산 등재를 눈앞에 두게 됐다. '한국의 서원'은 16세기부터 17세기에 건립된 '소수, 도산, 병산, 옥산, 도동, 남계, 필암, 무성, 돈암' 등 전국 9곳으로 구성된 연속유산으로, 모두 2009년 이전에 국가지정문화재 사적으로 지정됐고 비교적 원형이 잘 보존됐다는 평가를 받는다.

오는 6월 열리는 제43차 유네스코 세계유산위원회에서의 최종결정을 앞둔 가운데 세계유산에 등재될 경우 우리 유교 문화의 우수성을 과시하는 것은 물론 지역경제 활성화에도 적잖이 기여할 것으로 관측된다.

◇ 8년의 기다림…세계유산 등재될까

14일 문화재청에 따르면 '한국의 서원'은 지난 2011년 세계유산 잠정목록에 등재된 이후 8년 만에 세계유산 목록에 등재될 기회를 잡았다.

문화재청은 이런 한국 서원들에 대한 가치를 인정받기 위해 지난 2015년 처음 유네스코 세계유산센터에 등재신청을 했다. 그러나 유네스코 자문‧심사기구인 국제기념물유적협의회(ICOMOS, 이하 이코모스)는 한국의 서원이 '탁월한 보편적 가치'(OUV)에 충족하는 잠재적 가치를 갖췄다고는 판단하지만, '반려' 의견을 냈다.

여러 곳을 묶어 세계문화유산으로 신청할 경우 각 유산 간에 연결고리가 있어야 하는데, 서원 9곳이 어떻게 연결돼있는지에 관한 근거 설명이 약하다는 지적이었다. 이는 2012년 '한국의 서원 세계유산 등재추진단'이 결성됐을 때부터 제기된 문제이기도 했다. 결국 문화재청은 2016년 등재신청을 자진철회하고 관련단체들과 함께 보완작업에 들어갔다.

이코모스의 자문을 통해 OUV 서술을 다시 작성했고, 비교연구의 보완, 연속유산으로서의 논리 강화 등을 거쳤다. 그러면서 Δ동아시아에서 성리학이 가장 발달한 사회였던 조선시대에 각 지역에서 활성화된 서원들이 성리학의 사회적 전파를 이끌었다는 점 Δ서원의 건축이 높은 정형성을 갖췄다는 점을 세계유산 등재에 필요한 OUV로 제시하며 지난해 1월 등재를 재신청했다.

심사결과 이코모스는 OUV를 인정했다. 전체유산과 각 구성유산의 진정성과 완전성, 보존관리계획 등도 요건을 갖춘 것으로 봤다. 다만 이코모스는 추가적 이행과제로 등재 이후 9개 서원에 대한 통합 보존 관리방안을 마련할 것을 권고했다.

◇ '한국의 서원' 세계유산 등재 시 이점은

문화재청에 따르면 한국의 서원들이 세계유산에 등재될 경우 각 보전관리 및 활용홍보 지원을 위한 예산을 지원받을 수 있다. 현재는 각 지방자치단체가 서원을 보존관리하고 있지만 등재 이후에는 관련 예산을 문화재청으로부터 지원받아 더 나은 보전관리가 가능해진다. 또한 교육이나 관광 차원에서도 홍보예산 등을 받아 세계적인 문화유산을 널리 알릴 수 있는 기회가 생긴다.

이경동 '한국의 서원' 통합보존관리단 간사는 "국내에서 유교가 대중적으로는 부정적으로 알려지거나 잘 알려지지 않았다"며 "세계유산에 등재될 경우 국내뿐만 아니라 세계로까지 한국의 유교에 대해 잘 알릴 수 있고, 국내 문화브랜드를 한층 높일 수 있다는 가치가 있다"고 말했다.

그러면서 "각 지방자치단체에서는 서원을 중심으로 관광 및 활용사업을 통해 관련 부가사업을 활성화시킬 수 있다는 장점도 있다"고 덧붙였다.

서원의 세계유산 등재 여부는 오는 6월30일부터 아제르바이잔 바쿠에서 열리는 제43차 유네스코 세계유산위원회에서 최종결정된다. 등재로 최종결정이 날 경우 우리나라는 총 14건의 세계유산을 보유하게 된다.
'''

#print(len(word_tokenize(corpus)))
#print(len(corpus.split(corpus)))

from matplotlib import rc, font_manager

'''
path = 'C:/Users/J/Anaconda3/envs/FollowingTensorflowTutorial/Lib/site-packages/matplotlib/mpl-data/fonts/ttf'
font = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font)
'''

#print(sent_tokenize('오늘은. "화"요일입니다.! :)'))
#print(word_tokenize('오늘은. "화"요일입니다.! :)'))

#print(word_tokenize('오늘은. "화"요일입니다.! :)', preserve_line=False))
#print(word_tokenize('오늘은. "화"요일입니다.! :)', preserve_line=True))
'''
from nltk.tokenize import TweetTokenizer
print(TweetTokenizer().tokenize('오늘은. "화" :)요일입니다.! :) :( ;( ㅠㅠ'))

from nltk.tokenize import regexp_tokenize
corpus = gutenberg.open(gutenberg.fileids()[0]).read()
pattern = '([A-Za-z]+)'
print(regexp_tokenize(corpus[1], pattern))

pattern = '([가-힣]+)'
print(regexp_tokenize('오늘은. "화" :)요일입니다.! :) :( ;( ㅠㅠ', pattern))
'''
#nltk.download('stopwords')

from nltk import Text

textObj = Text(word_tokenize(corpus))
print(textObj.vocab())

import os

base = 'C:/Users/J/Desktop/바탕화면 파일들/CodePractice/Python/AI 이노베이션 스퀘어 자연어처리 과정/news/'
corpus = ''
for _ in os.listdir(base):
    with open(base + _, encoding='utf-8') as fp:
        corpus += fp.read()

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

#plt.rcParams["font.family"] = 'NanumPen'

from matplotlib import rc, font_manager

#path = 'C:/Windows/Fonts/NanumPen'
#font = font_manager. FontProperties(fname=path).get_name()
#rc('font', family=font)

# textObj = Text(word_tokenize(corpus))
# textObj.vocab().most_common()
# print(len(textObj))
# print(set(textObj))
# print(textObj.plot(30))
#
# print(textObj.dispersion_plot(['중국', '미국']))
# print(textObj.collocations())

corpus = kolaw.open(kolaw.fileids()[0]).read()
kolaw = Text(word_tokenize(corpus))
print(kolaw.similar('국민은'))

k = 50
b = 0.5

base = 'C:/Users/J/Desktop/바탕화면 파일들/CodePractice/Python/AI 이노베이션 스퀘어 자연어처리 과정/news/'
corpus = list()
for _ in os.listdir(base):
    with open(base + _, encoding='utf-8') as fp:
        corpus.append(fp.read())

import matplotlib.pyplot as plt

x = list()
y = list()
_text = ''
for _ in corpus:
    _text += _
    obj = Text(word_tokenize(_text))
    x.append(k * len(obj) ** b)
    y.append(len(set(obj)))

#plt.plot(x, y, 'r-')

kolawText = Text(morphemes)
# print(kolawText.vocab().most_common(30))
# print(kolawText.vocab())
# print(kolawText.plot(20))
#
# print(kolawText.similar('국민'))
# print(kolawText.similar('국회'))
# print(kolawText.similar('대통령'))

# print(kolawText.dispersion_plot(['국민', '국회', '대통령']))
# print(kolawText.collocations())

import os
import matplotlib.pyplot as plt
from math import log

base = 'C:/Users/J/Desktop/바탕화면 파일들/CodePractice/Python/AI 이노베이션 스퀘어 자연어처리 과정/news/'
# for _ in os.listdir(base):
#     morphemes = list()
#     with open(base + _, encoding='utf-8') as fp:
#         text = fp.read()
#     for sentence in sent_tokenize(text):
#         morphemes.extend(ma.morphs(sentence))
#     obj = Text(morphemes)
#     x = [_[0] for _ in obj.vocab().most_common()]
#     y = [_[1] for _ in obj.vocab().most_common()]
#     yy = [log(_) for _ in y]
#     plt.plot(x, y, '-r')
#     plt.show()
#     plt.plot(x, yy, 'b-')
#     plt.show()
#     break
#
# from konlpy.tag import Okt
#
# ma = Okt()

# from konlpy.tag import Okt
#
# ma = Okt()
#
# for _ in os.listdir(base):
#     morphemes = list()
#     with open(base + _, encoding='utf-8') as fp:
#         text = fp.read()
#     for sentence in sent_tokenize(text):
#         morphemes.extend(ma.morphs(sentence))
#
# obj = Text(morphemes)
# x = range(len(obj.vocab().most_common()))
# y = [_[1] for _ in obj.vocab().most_common()]
# yy = [log(_) for _ in y]
# plt.plot(x, y, '-r')
# plt.show()
# plt.plot(x, yy, 'b-')
# plt.show()

from konlpy.corpus import kolaw

corpus = kolaw.open(kolaw.fileids()[0]).read()

# def eojeol(text, n =2):
#     tokens = text.split()
#     ngram = list()
#
#     for i in range(len(tokens)-(n-1)):
#         ngram.append(' '.join(tokens[i:i+n]))
#     return ngram
#
# for _ in sent_tokenize(corpus):
#     print(eojeol(_))
#     break
#
# def umjeol(text, n =2):
#     ngram = list()
#
#     for i in range(len(text)-(n-1)):
#         ngram.append(''.join(text[i:i+n]))
#     return ngram
#
# for _ in sent_tokenize(corpus):
#     print(umjeol(_))
#     break
#
# print(kolawText.vocab())
# bigramText = eojeol(corpus)
# print(bigramText.vocab())

# Byte Pair Encoding
# ('어절':빈도), ('어절':빈도), ('어절':빈도)
# low:5, lowest:2
# l o w </w>
# l o w e s t </w>

def splitTerm(term):
    result = list()
    for token in term.split():
        result.append(' '.join(list(term) + ['</w>']))
    return '_'.join(result)

from collections import defaultdict

def ngram(data, n=2):
    result = defaultdict(int)

    for term, freq in data.items():
        tokens = term.split()
        for i in range(len(tokens) - (n-1)):
            result[' '.join(tokens[i:i+n])] += freq
    return result

import re

def mergerNgram(maxKey, data):
    newData = dict()

    for term, freq in data.items():
        newKey = re.sub(maxKey, maxKey.replace(' ', ''), term)
        newData[newKey] = freq

    return newData

data = {
    splitTerm('low'):5,
    splitTerm('lowest'):2,
    splitTerm('newer'):6,
    splitTerm('wider'):3
}
for _ in range(5):
    bigram = ngram(data)
    maxKey = max(bigram, key=bigram.get)
    data = mergerNgram(maxKey, data)
print(data)