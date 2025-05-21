# ✅STEP2:
# ✅Converting tokens into token IDs : 

with open("the-verdict.txt" , "r" , encoding = "utf-8") as f:
    raw_text = f.read()
import re
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)' , raw_text)
preprocessed = [item for item in preprocessed if item.strip()]

# preprocessed is the list of tokens now,

all_words = sorted(set(preprocessed))
print(len(all_words))

# Creating a vocabulary of all tokens and associating unique ID with it
vocab = {token:integer for integer,token in enumerate(all_words)}
for i,item in enumerate(vocab.items()):
    print(item)
    if i>=50:
        break
