#a = 0XFF how can i do and operation to 4 bit variable.

def reverse(sentence):
    if len(sentence.split() == 1):
        return sentence

    else:
        words = sentence.split()
        return ''.joint([words[-1]] + reverse(''.join(words[:-1])).split())

    sentence = "hello my name is tanisha"
    reverse_sentence = reverse(sentence)
    print(reverse_sentence)
