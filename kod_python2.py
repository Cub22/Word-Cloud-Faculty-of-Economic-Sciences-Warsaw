import matplotlib.pyplot as pyplot
from wordcloud import WordCloud, STOPWORDS
import sys, os
from collections import Counter

os.chdir(sys.path[0])

# Wczytaj tekst
raw_text = open('WordCloud_ANG.txt', mode='r', encoding='utf-8').read()

# Rozdziel tylko po średnikach
phrases = raw_text.split(';')

# Oczyść i przekształć do wielkich liter
cleaned_phrases = [phrase.strip().upper() for phrase in phrases if phrase.strip()]

# Policz częstotliwość fraz
phrase_counts = Counter(cleaned_phrases)

# Chmura słów
wc = WordCloud(
    background_color='white',
    stopwords=STOPWORDS,
    height=600,
    width=800,
    max_words=45,
    collocations=False,
    colormap='tab20'  # paleta zróżnicowanych kolorów
)

# Generuj z częstotliwości
wc.generate_from_frequencies(phrase_counts)

# Zapisz do pliku
wc.to_file('wordcloud_output_ANG.png')
