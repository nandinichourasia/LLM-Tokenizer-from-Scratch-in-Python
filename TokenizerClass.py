 class SimpleTokenizerV1:
    def __init__(self , vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encode(self , text):
        preprocessed = re.split(r'([,.:;?!\']|--|\s)' ,text )
        preprocessed = [item for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # The effect is that any whitespace directly before the specified punctuation marks is removed.
        text = re.sub(r'\s+([,.:;?!\'"()\[\]])', r'\1', text)
        return text
    
tokenizer = SimpleTokenizerV1(vocab)
text = """" It's the last he painted, you know," Mrs.Gisburn said with pardonable pride."""
print(tokenizer.encode(text))
print(tokenizer.decode(ids))

# But if the token is not present in the vocabulary it will throw an error for handling that we eill create Version2 class
