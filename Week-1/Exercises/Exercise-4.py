 ################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print(sum(dct.values()))


print("Exercise 4.1")

pass

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""
print(max(dct, key=dct.get))

print("Exercise 4.2")

pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""
new_dct = {k: v**2 for k, v in dct.items()}
print(new_dct)

print("Exercise 4.3")

pass

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""
even = [k for k, v in dct.items() if v % 2 == 0]
print(even)

print("Exercise 4.4")

pass

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""
swap = {v: k for k, v in dct.items()}
print(swap)

print("Exercise 4.5")

pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

print("Exercise 4.6")

pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

words = [responses_mapping[ch] for ch in responses]
print(words)

print("Exercise 4.7")

pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""
dct1 = {'a': 1, 'b': 2}
dct2 = {'c': 3, 'd': 4}
print({**dct1, **dct2})

print("Exercise 4.8")

pass

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""
biggarden = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
print(dict(sorted(biggarden.items())))

print("Exercise 4.9")

pass

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""
print(dict(sorted(biggarden.items(), key = lambda item: item[1])))

print("Exercise 4.10")

pass

print("---")