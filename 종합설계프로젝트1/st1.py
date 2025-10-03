# 1. 데이터 전처리
from konlpy.tag import Okt
from collections import Counter
import re

text = "오늘은 좀 불안하고 긴장되네요. 하지만 기대도 됩니다."
okt = Okt()
tokens = [t for t in okt.nouns(text) if len(t) > 1]  # 명사 추출
print(tokens)

# 2. 감정 분류 (HuggingFace KLUE-BERT)
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=8)  
# num_labels = 감정 카테고리 개수

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
print(classifier("오늘은 좀 불안하고 긴장되네요."))

# 3. 토픽 모델링 (LDA 예시)
from gensim import corpora, models

dictionary = corpora.Dictionary([tokens])
corpus = [dictionary.doc2bow(tokens)]
lda = models.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=10)
print(lda.print_topics())

# 4. 네트워크 분석 (공출현 네트워크)
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
window_size = 3
for i in range(len(tokens) - window_size + 1):
    window = tokens[i:i+window_size]
    for w1 in window:
        for w2 in window:
            if w1 != w2:
                G.add_edge(w1, w2)

nx.draw(G, with_labels=True, node_color="lightblue")
plt.show()

# 5. 시각화 - WordCloud
from wordcloud import WordCloud

word_freq = Counter(tokens)
wc = WordCloud(font_path="/System/Library/Fonts/Supplemental/AppleGothic.ttf", background_color="white")
wc.generate_from_frequencies(word_freq)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
