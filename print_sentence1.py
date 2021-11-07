def print_sentence(input, sentence, word):
    print(input[sentence][word])

my_sentences = [
    {1: 'I love python'},
    {2: 'Now go and code some python'},
    {3: 'Python rocks!'},
]

print_sentence(my_sentences, 1, 2)
print_sentence(my_sentences, 0, 1)