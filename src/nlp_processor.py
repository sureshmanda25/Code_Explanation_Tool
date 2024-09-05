import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def process_text(text: str) -> str:
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    
    # Simple rule to capitalize the first letter of sentences
    processed_tokens = []
    capitalize_next = True
    for word, tag in tagged:
        if capitalize_next:
            word = word.capitalize()
            capitalize_next = False
        if word in '.!?':
            capitalize_next = True
        processed_tokens.append(word)
    
    return ' '.join(processed_tokens)