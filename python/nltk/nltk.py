import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize.punkt import PunktWordTokenizer

def demo():
    # split paragraph into sentences using punct
    sent_tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(paragraphs)
    
    # split sentence into tokens (wrods + puncts)
    s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\n\nThanks."
    WordPunctTokenizer().tokenize(s)
    #['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
    PunktWordTokenizer().tokenize(s)
    #['Good', 'muffins', 'cost', '$3.88', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks.']
    PunktWordTokenizer().span_tokenize(s)
    #[(0, 4), (5, 12), (13, 17), (18, 23), (24, 26), (27, 30), (31, 36), (38, 44),  (45, 48), (49, 51), (52, 55), (56, 58), (59, 64), (66, 73)]
    
    #split the paragraph into sentence
    nltk.sent_tokenize(s)
    #split sentence into word and punct
    nltk.word_tokenize(s)
    
    # pos tagging
    nltk.pos_tag(nltk.word_tokenize(s))



    
    
    
    