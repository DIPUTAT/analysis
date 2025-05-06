import ru_core_news_md
from spacy.lang.ru.stop_words import STOP_WORDS

model = ru_core_news_md.load()
text = model("Ставки на спор, большые выйграши, быстрые выплаты, надежный букмекер")
text_list = [word.lemma_ for word in text]
print(text_list)

filter_text_list = [elem for elem in text_list if not elem in STOP_WORDS]
print(filter_text_list)

