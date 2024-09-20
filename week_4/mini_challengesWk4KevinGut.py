# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper()) #prints the senntence in uppercase 
sentence2 = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence2.lower())#prints the sentence in lowercase

print(sentence.find("communications")) 
print(sentence[25:39].upper())
print(sentence.replace("communications", "COMMUNICATIONS")) #prints the sentence word communications in uppercase 
print(sentence.replace("communications", "communications".upper())) #prints the sentence word communications in uppercase 

newsentence = "if the implementation is hard to explain, it might be a bad idea."
print(newsentence.replace("hard", "easy").replace("bad", "good"))
modfiedsentence=newsentence.replace("hard", "easy").replace("bad", "good")
print(modfiedsentence)


#join method 
wordlist=["simple","is","better","than","complex."]
print(wordlist)
joinsentence=" ".join(wordlist)
print(joinsentence)
newwordlist=["apple","banna","mango","cherry","watermelon"]
newjoinsentence="💀 ".join(newwordlist)
print(newjoinsentence)
#split method
sentence4= "I am a python programmer"
print(sentence4.split())#splits sentence into a list of words 
#this prints out as ['I', 'am', 'a', 'python', 'programmer']
#by default, this method splits the sentence by commas 
print(sentence4.split(","))#splits the sentence into a lost if words using a separator
#this prints out as ['I am a python programmer']
print(sentence4.split("a")) #splits the snetence into a list of words using a separator 
#this takes out all the as in the sentence 
#it prints something like this ['I ', 'm ', ' python progr', 'mmer']

#concatination words inpython repetition 15 times 
result= "Repetition" * 15
print(result)


firstparagraph="The unanimous Declaration of the thirteen united States of America, When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
print(firstparagraph.replace("people", "citizens").replace(" ","").replace(",", "🤡"))



# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple","is","better","than","complex."]
sentencejoin = " ".join(word_list)
print(sentencejoin)


# String Methods Practice #3
# Replace in the following sentence:
practice3="If the implementation is hard to explain, it might be a bad idea."
print(practice3.replace("hard", "easy").replace("bad", "good"))
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

resul= "Repetition" * 15
print(resul)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
haiku="Whitecaps on the bay: A broken signboard banging In the April wind."
print(haiku.replace("bay", "beach"))
# — Richard Wright, collected in Haiku: This Other World, 1998

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
color = ['blue', 'green', 'red', 'orange', 'yellow']
    
len(color)
print(len)