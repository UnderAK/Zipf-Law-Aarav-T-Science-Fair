#import libraries
import random
import unidecode
import time
import math

#start time
start_time = time.time()

#pre-made variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
incrementer_random_text = 0
number_of_charecters = 10

#generation of random text
with open("random_text_generated.txt","a") as random_text_writer:
    while incrementer_random_text < number_of_charecters:
        random_text_writer.write(random.choice(letters))
        incrementer_random_text += 1

def random_text_doer(language):
    start_time = time.time()
    dictionary_split_to_list_with_accents = []
    dictionary_split_to_list_refined = []
    length_of_word_to_count = {}
    dictionary_analyzed = f"all-words-in-all-languages/{language}/{language}.txt"
    #seperating the dictionary and fixing
    with open(dictionary_analyzed,"r") as dictionary_string:
        dictionary_to_string = dictionary_string.read()
        dictionary_split_to_list_with_accent = dictionary_to_string.split(',')
        for element in dictionary_split_to_list_with_accent:
            element_removed = unidecode.unidecode(element)
            dictionary_split_to_list_refined.append(element_removed)

    #finding frequency of each word + sort by length 
    with open("random_text_generated.txt","r") as random_text_reader:
        random_text_read = random_text_reader.read()
        random_text_length = len(random_text_read)
        for word in dictionary_split_to_list_refined:
            if len(word) in length_of_word_to_count:
                length_of_word_to_count[len(word)] += random_text_read.count(word)
            else:
                length_of_word_to_count[len(word)] = 0 
                length_of_word_to_count[len(word)] += random_text_read.count(word)

    #sort output
    length_of_word_to_count = dict(sorted(length_of_word_to_count.items()))
    #time
    end_time = time.time()

    elapsed_time = end_time - start_time    
    #print all output values
    with open("results.txt","a") as results_writer:
        results_writer.write(f"Language: {language} \n Length of Random Text: {random_text_length} \n {length_of_word_to_count} \n Elapsed time: {elapsed_time} seconds \n")
        for element in length_of_word_to_count:
            element_log = length_of_word_to_count[element]
            if element_log > 0:
                results_writer.write(" ")
                results_writer.write(str(math.log10(element_log)))
                results_writer.write("\n")
        results_writer.write("------------------------------ \n")

with open("languages.txt","r") as languages_reader:
    languages_read = languages_reader.read()
    for line in languages_read.splitlines():
        random_text_doer(line)






