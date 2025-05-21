# ✅STEP:1 
# ✅TOKENIZING THE TEXT:

with open("the-verdict.txt" , "r" , encoding = "utf-8") as f:
    raw_text = f.read()
print("Total number of character:" , len(raw_text))
print(raw_text[:99])


# for spliting the words individually we use python library "re"
import re
text = "hello, world. This, is a test."
result = re.split(r'(\s)' , text)
print(result)

# no whitespace:
result = [item for item in result if item.strip()]
print(result)

#For creating seperate tokens for special characters:
text="hello, world. This-- is a test?"
result = re.split(r'([,.:;?_!()\']|--|\s)' , text)
result = [item for item in result if item.strip()]
print(result)

# Splitted text is stored , and if there is any space .strip() removes it:
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)' , raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print(preprocessed[:30])
print(len(preprocessed))
