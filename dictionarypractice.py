my_dict = {
  "name": "Richard",
  "age": 25
}

# my_dict2 = dict(
#   "name": "Richard",
#   "age": 25
#   )

# Accessing elements
# print(my_dict["name"])
# print(my_dict.get("name"))

# Adding new key-value pairs
my_dict["city"] = "San Jose"

# Modify 
my_dict["age"] = 26

# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# # iterate over keys
# for key in my_dict:
#   print(key)

# # Iterate over values
# for value in my_dict.values():
#   print(value)

# # Iterate over key-value pairs
# for key,value in my_dict.items():
#   print(key, value)

# word = "abracadabra"

# word_count = {i: word.count(i) for i in word}

# eg = {}

# for n in word:
#     if n in eg:
#         eg[n] += 1
#     else:
#         eg[n] = 1
        
# print(eg)

my_dict2 = {
  "Alice": 25,
  "Bob": 26,
  "Richard": 26
}

target_value = 26

# for key, value in my_dict2.items():
#   if value == target_value:
    # print(f"Key for value {target_value}: {key}")
new_tup = ()
n = tuple()
new_t = 1,
print(new_t.count(1))
print(n)

nested_tuple = ((1,2),(3,4),(5,6))
print(nested_tuple[0]) # output -> (1,2)
print(nested_tuple[0][1]) # output -> 2

my_list = [1,2,3]
my_tuple = tuple(my_list)
print(my_tuple)

#Sets
