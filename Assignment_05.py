### Assignment No 5 ###
"""
Assignment Title:
Implement regular expression function to find URL, IP address, Date,
PAN number in textual data using python libraries
"""

import re
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Regex patterns
url_pattern = re.compile(r'https?://\S+|www\.\S+')
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
date_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
pan_pattern = re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b')

def extract_entities(text):
    doc = nlp(text)
    urls = re.findall(url_pattern, text)
    ips = re.findall(ip_pattern, text)
    dates = re.findall(date_pattern, text)
    pans = re.findall(pan_pattern, text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return {'URLs': urls, 'IPs': ips, 'Dates': dates, 'PANs': pans, 'spaCy_Entities': entities}

# Example text
text = """
Visit our website at https://www.example.com.
Server IP is 192.168.1.1.
The event date is 2025-10-08.
Employee PAN: ABCDE1234F.
"""

# Run extraction
result = extract_entities(text)

# Display results
for key, value in result.items():
    print(f"{key}: {value}")

    '''
    output:-PS D:\nlpl>  d:; cd 'd:\nlpl'; & 'c:\Program Files\Python312\python.exe' 'c:\Users\acer\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '50445' '--' 'd:\nlpl\Assignment_05.py' 
URLs: ['https://www.example.com.']
IPs: ['192.168.1.1']
Dates: ['2025-10-08']
PANs: ['ABCDE1234F']
spaCy_Entities: [('Server IP', 'ORG'), ('192.168.1.1', 'DATE'), ('2025-10-08', 'DATE'), ('PAN', 'ORG')]
PS D:\nlpl>

    '''
