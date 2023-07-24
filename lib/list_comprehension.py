#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    if not even_numbers:
        return[]
    return even_numbers 
    pass

def make_exclamation(sentence_list):
    list_of_sentences = [sentences + '!' for sentences in sentence_list]
    if not list_of_sentences:
        return []
    return list_of_sentences
    pass