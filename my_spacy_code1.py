# Import SpaCy library
import spacy

# Load English language model
nlp = spacy.load('en_core_web_sm')

# Input sample text
example_string = """
Sagar (PRN: UIT22M1019) is pursuing B.Tech in Information Technology at Sanjivani College of Engineering.
He is passionate about AI and machine learning.
Recently, he started learning Natural Language Processing (NLP).
He enjoys working on Python projects in his free time.
His favorite subjects are Data Structures, Algorithms, and Cloud Computing.
"""

# Process text with SpaCy
doc = nlp(example_string)

# ----- Perform all NLP Operations -----

# 1️⃣ Sentence Tokenization
sentences = [sent.text for sent in doc.sents]

# 2️⃣ Word Tokenization (without punctuation)
words = [token.text for token in doc if not token.is_punct]

# 3️⃣ Stop Word Removal (no punctuation + no stop words)
filtered_words = [token.text for token in doc if not token.is_stop and not token.is_punct]

# 4️⃣ Lemmatization (root form of words)
lemmatized_words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

# ----- Print all Results -----
print("\n===== NLP TEXT PRE-PROCESSING RESULTS =====")
print("\n1️⃣ Sentences:\n", sentences)
print("\n2️⃣ Words (excluding punctuation):\n", words)
print("\n3️⃣ Filtered Words (no stop words, no punctuation):\n", filtered_words)
print("\n4️⃣ Lemmatized Words:\n", lemmatized_words)
