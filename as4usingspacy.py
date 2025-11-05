from nltk.util import ngrams  

# Unigram model
n = 1
sentence = ("My best friend and I study computer science together at college. "
           "Our friendship has grown stronger through teamwork and learning.")
unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAM    ************************")
for item in unigrams:
    print(item)

# Bigram model
n = 2
sentence = ("The professor explained the assignment clearly during the lecture. "
            "The professor encouraged collaboration and creativity.")
bigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAM    ************************")
for item in bigrams:
    print(item)

# Trigram model
n = 3
sentence = ("Our college library is full of useful resources for research. "
            "Spending time in the library has improved my learning habits.")
trigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAM    ************************")
for item in trigrams:
    print(item)
