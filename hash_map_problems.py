#Word Counting

def word_counts(words):
    """
    counts number of occurences of a word in a list.
    Args:words list: contains a list of words
    Returns: dictionary that contains number of occurrences of words
    """
    return {word: words.count(word) for word in words}

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_counts(words))
print(word_counts.__doc__)

#character frequency

s = "Hello, world!"

def character_frequency(string):
    return {letter: string.count(letter) for letter in string}

print(character_frequency(s))

#Map words to length

words = ["Tree", "House", "Sun"]

def map_words_to_length(words_list):
    return {word: len(word) for word in words_list}

print(map_words_to_length(words))

#character position mapping

word = "Hello"

def character_position_mapping(word):
    my_dict = {}
    for index, letter in enumerate(word):
        if letter in my_dict:
            my_dict[letter].append(index)
        else:
            my_dict[letter] = [index]
    return my_dict

print(character_position_mapping(word))

#unique elements

def unique_elements(elements):
    return list(set(elements))

nums = [1,2,2,3,4,4,4,5]

print(unique_elements(nums))

#find duplicates

def find_duplicates(elements):
    return list({element for element in elements if elements.count(element) > 1})

nums = [1,2,2,3,4,5,5]

print(find_duplicates(nums))

#Sum of Pairs

nums = [2,3,4,5,7]
target = 7

def sum_of_pairs(nums, target):
    my_lst = list()
    for num in nums:
        for number in nums:
            if num + number == target:
                if [num, number] not in my_lst and [number, num] not in my_lst:
                    my_lst.append([num, number])
    return my_lst

print(sum_of_pairs(nums, target))

#find common elements in three lists

list1 = [1, 2, 3, 4, 5] 
list2 = [3, 4, 5, 6, 7] 
list3 = [5, 6, 7, 8, 9]
            
answer = set(list1).intersection(set(list2)).intersection(set(list3))
print(answer)

#second most frequent element
a_list = [1,2,2,4,5,5,5,5,3]

def second_most_frequent(elements):
    results = sorted({i:elements.count(i) for i in elements}.items(), key = lambda x: x[1], reverse=True)
    return f"{results[1][1]} # Since '{results[0][0]}' appears {results[0][1]} times and '{results[1][0]}' appears {results[1][1]} times"

print(second_most_frequent(a_list))

#index mapping
elements = ["a", "b", "a", "c"]

def index_mapping(elements):
    return {i: elements.index(i) for i in elements}

print(index_mapping(elements))

#check anagram
str1 = "crow"
str2 = "work"

def anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))
        
print(anagram(str1, str2))

#commom elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

def common_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))

print(common_elements(list1, list2))

#group words by length
words = ["cat", "dog", "elephant", "tiger", "lion"]

def group_words(elements):
    dictionary = {}
    for element in elements:
        list1 = []
        