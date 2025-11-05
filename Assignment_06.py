###  Assignment No 6 ###

"""
Assignment Title:
Implement and visualize Dependency Parsing of Textual Input
using Stanford CoreNLP and Spacy library
"""

import spacy
from spacy import displacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# --- NEW INPUT TEXT ---
multiline_text = """
Artificial Intelligence (AI) is transforming industries across the globe by enabling machines 
to perform tasks that typically require human intelligence. 
From healthcare and education to finance and transportation, 
AI systems analyze vast amounts of data to make decisions, detect patterns, and improve efficiency. 
As AI technology advances, it raises important questions about ethics, privacy, and the future of human employment.
"""

# Process the text
multiline_doc = nlp(multiline_text)

# Print token-level dependency information
for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

# Visualize dependencies
displacy.serve(multiline_doc, style="dep")
'''
 output:9676' '--' 'd:\nlpl\Assignment_06.py' 

TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'Intelligence'
token.dep_ = 'dep'

TOKEN: Artificial
=====
token.tag_ = 'NNP'
token.head.text = 'Intelligence'
token.dep_ = 'compound'

TOKEN: Intelligence
=====
token.tag_ = 'NNP'
token.head.text = 'transforming'
token.dep_ = 'nsubj'

TOKEN: (
=====
token.tag_ = '-LRB-'
token.head.text = 'Intelligence'
token.dep_ = 'punct'

TOKEN: AI
=====
token.tag_ = 'NNP'
token.head.text = 'Intelligence'
token.dep_ = 'appos'

TOKEN: )
=====
token.tag_ = '-RRB-'
token.head.text = 'Intelligence'
token.dep_ = 'punct'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'transforming'
token.dep_ = 'aux'

TOKEN: transforming
=====
token.tag_ = 'VBG'
token.head.text = 'transforming'
token.dep_ = 'ROOT'

TOKEN: industries
=====
token.tag_ = 'NNS'
token.head.text = 'transforming'
token.dep_ = 'dobj'

TOKEN: across
=====
token.tag_ = 'IN'
token.head.text = 'transforming'
token.dep_ = 'prep'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'globe'
token.dep_ = 'det'

TOKEN: globe
=====
token.tag_ = 'NN'
token.head.text = 'across'
token.dep_ = 'pobj'

TOKEN: by
=====
token.tag_ = 'IN'
token.head.text = 'transforming'
token.dep_ = 'prep'

TOKEN: enabling
=====
token.tag_ = 'VBG'
token.head.text = 'by'
token.dep_ = 'pcomp'

TOKEN: machines
=====
token.tag_ = 'NNS'
token.head.text = 'enabling'
token.dep_ = 'dobj'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'machines'
token.dep_ = 'dep'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'perform'
token.dep_ = 'aux'

TOKEN: perform
=====
token.tag_ = 'VB'
token.head.text = 'enabling'
token.dep_ = 'xcomp'

TOKEN: tasks
=====
token.tag_ = 'NNS'
token.head.text = 'perform'
token.dep_ = 'dobj'

TOKEN: that
=====
token.tag_ = 'WDT'
token.head.text = 'require'
token.dep_ = 'nsubj'

TOKEN: typically
=====
token.tag_ = 'RB'
token.head.text = 'require'
token.dep_ = 'advmod'

TOKEN: require
=====
token.tag_ = 'VBP'
token.head.text = 'tasks'
token.dep_ = 'relcl'

TOKEN: human
=====
token.tag_ = 'JJ'
token.head.text = 'intelligence'
token.dep_ = 'amod'

TOKEN: intelligence
=====
token.tag_ = 'NN'
token.head.text = 'require'
token.dep_ = 'dobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'transforming'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: From
=====
token.tag_ = 'IN'
token.head.text = 'finance'
token.dep_ = 'prep'

TOKEN: healthcare
=====
token.tag_ = 'NN'
token.head.text = 'From'
token.dep_ = 'pobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'healthcare'
token.dep_ = 'cc'

TOKEN: education
=====
token.tag_ = 'NN'
token.head.text = 'healthcare'
token.dep_ = 'conj'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'finance'
token.dep_ = 'aux'

TOKEN: finance
=====
token.tag_ = 'NN'
token.head.text = 'finance'
token.dep_ = 'ROOT'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'finance'
token.dep_ = 'cc'

TOKEN: transportation
=====
token.tag_ = 'NN'
token.head.text = 'finance'
token.dep_ = 'conj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'analyze'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: AI
=====
token.tag_ = 'NNP'
token.head.text = 'systems'
token.dep_ = 'compound'

TOKEN: systems
=====
token.tag_ = 'NNS'
token.head.text = 'analyze'
token.dep_ = 'nsubj'

TOKEN: analyze
=====
token.tag_ = 'VBP'
token.head.text = 'finance'
token.dep_ = 'conj'

TOKEN: vast
=====
token.tag_ = 'JJ'
token.head.text = 'amounts'
token.dep_ = 'amod'

TOKEN: amounts
=====
token.tag_ = 'NNS'
token.head.text = 'analyze'
token.dep_ = 'dobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'amounts'
token.dep_ = 'prep'

TOKEN: data
=====
token.tag_ = 'NNS'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'make'
token.dep_ = 'aux'

TOKEN: make
=====
token.tag_ = 'VB'
token.head.text = 'analyze'
token.dep_ = 'advcl'

TOKEN: decisions
=====
token.tag_ = 'NNS'
token.head.text = 'make'
token.dep_ = 'dobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'analyze'
token.dep_ = 'punct'

TOKEN: detect
=====
token.tag_ = 'VB'
token.head.text = 'analyze'
token.dep_ = 'conj'

TOKEN: patterns
=====
token.tag_ = 'NNS'
token.head.text = 'detect'
token.dep_ = 'dobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'detect'
token.dep_ = 'punct'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'detect'
token.dep_ = 'cc'

TOKEN: improve
=====
token.tag_ = 'VB'
token.head.text = 'detect'
token.dep_ = 'conj'

TOKEN: efficiency
=====
token.tag_ = 'NN'
token.head.text = 'improve'
token.dep_ = 'dobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'finance'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: As
=====
token.tag_ = 'IN'
token.head.text = 'advances'
token.dep_ = 'mark'

TOKEN: AI
=====
token.tag_ = 'NNP'
token.head.text = 'technology'
token.dep_ = 'compound'

TOKEN: technology
=====
token.tag_ = 'NN'
token.head.text = 'advances'
token.dep_ = 'nsubj'

TOKEN: advances
=====
token.tag_ = 'VBZ'
token.head.text = 'raises'
token.dep_ = 'advcl'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'raises'
token.dep_ = 'punct'

TOKEN: it
=====
token.tag_ = 'PRP'
token.head.text = 'raises'
token.dep_ = 'nsubj'

TOKEN: raises
=====
token.tag_ = 'VBZ'
token.head.text = 'raises'
token.dep_ = 'ROOT'

TOKEN: important
=====
token.tag_ = 'JJ'
token.head.text = 'questions'
token.dep_ = 'amod'

TOKEN: questions
=====
token.tag_ = 'NNS'
token.head.text = 'raises'
token.dep_ = 'dobj'

TOKEN: about
=====
token.tag_ = 'IN'
token.head.text = 'questions'
token.dep_ = 'prep'

TOKEN: ethics
=====
token.tag_ = 'NNS'
token.head.text = 'about'
token.dep_ = 'pobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'ethics'
token.dep_ = 'punct'

TOKEN: privacy
=====
token.tag_ = 'NN'
token.head.text = 'ethics'
token.dep_ = 'conj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'privacy'
token.dep_ = 'punct'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'privacy'
token.dep_ = 'cc'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'future'
token.dep_ = 'det'

TOKEN: future
=====
token.tag_ = 'NN'
token.head.text = 'privacy'
token.dep_ = 'conj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'future'
token.dep_ = 'prep'

TOKEN: human
=====
token.tag_ = 'JJ'
token.head.text = 'employment'
token.dep_ = 'amod'

TOKEN: employment
=====
token.tag_ = 'NN'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'raises'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...

'''