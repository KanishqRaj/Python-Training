def word_frequency(sentence):
    words = sentence.split()
    freq_dictionary = {}
    for word in words:
        freq_dictionary[word] = freq_dictionary.get(word, 0) + 1
    return freq_dictionary

sentence = "The elephant was chasing a tiger which was chasing an elephant"
print(word_frequency(sentence))