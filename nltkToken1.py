import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Sample text
text = "I am learning Natural Language Processing using Python!"

# 1. Tokenization
tokens = word_tokenize(text)

# 2. Remove punctuation
tokens = [w for w in tokens if w not in string.punctuation]

# 3. Remove stop words
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words]

# 4. Stemming
ps = PorterStemmer()
stems = [ps.stem(w) for w in filtered]

# 5. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(w) for w in filtered]

print("Tokens:", tokens)
print("After Stopword Removal:", filtered)
print("Stemming:", stems)
print("Lemmatization:", lemmas)
