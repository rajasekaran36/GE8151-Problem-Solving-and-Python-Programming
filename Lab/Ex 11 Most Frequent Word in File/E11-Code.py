in_file = open("input_file.txt","r")
data = in_file.read()
print(data)
word_list = data.split(" ")

word_dictionary = {}

for word in word_list:
    if(word in word_dictionary):
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1
        
max_frequency = max(word_dictionary.values())
print(max_frequency)

print("Maximum Repeated Words")
print("----------------------")
for word in word_dictionary:
    if(word_dictionary[word]==max_frequency):
        print (word)
