
def remove_duplicates(input_string, is_sentence=True, case_sensitive=True):
    if is_sentence:
        words = input_string.split()
        unique_words = []

        for word in words:
            if not case_sensitive:
                word = word.lower()
            if word not in unique_words:
                unique_words.append(word)

        return ' '.join(unique_words)
    else:
        if not case_sensitive:
            input_string = input_string.lower()
        output_string = ""
        seen_chars = set()
        
        for char in input_string:
            if char not in seen_chars:
                output_string += char
                seen_chars.add(char)
        
        return output_string

input_string = input("Enter a sentence or a word: ")
if len(input_string.split()) > 1:  # Check if it's a sentence by counting the number of words
    is_sentence = True
else:
    is_sentence = False

case_sensitive = input_string.lower().strip() == 'yes'
  
result = remove_duplicates(input_string, is_sentence, case_sensitive)
if is_sentence:
    print("Sentence with duplicate words removed:", result)
else:
    print("Word with duplicates removed:", result)

