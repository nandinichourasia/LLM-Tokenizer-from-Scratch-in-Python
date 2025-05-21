# What if the token is not present in the vocab? then it will throw an error , to handle
# this we ADD SPECIAL CONTEXT TOKENS:
# <|endoftext|>  and <|unk|> (unknown token)

# Adding 2 extra tokens to vocabulary
all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>" , "<|unk|>"])

vocab = {token:integer for integer,token in enumerate(all_tokens)}
print(len(vocab.items()))


class SimpleTokenizerV2:
    def __init__(self , vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encode(self , text):
        preprocessed = re.split(r'([,.:;?!\']|--|\s)' ,text )
        preprocessed = [item for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int
                        else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    
    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # The effect is that any whitespace directly before the specified punctuation marks is removed.
        text = re.sub(r'\s+([,.:;?!\'"()\[\]])', r'\1', text)
        return text
    
tokenizer = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1,text2))
print(text)
print(tokenizer.decode(tokenizer.encode(text)))
