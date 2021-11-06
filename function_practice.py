#   function exercises 
#   practice



#  RETURN EVENS - Given a list of numbers, write a function which returns even numbers omly
def return_evens(num):        
    mylist = []
    for i in num:
        if i % 2 == 0:
            mylist.append(i)
    return mylist

print(return_evens([8,7,5,6]))



#  NEW ZINGER - write a function that returns second and fifth letter capitalized
def new_zinger(word):
    if len(word) > 4:
        return word[1].upper() +  word[4].upper()     #        you could also use .capitalize()
print(new_zinger('Vincent'))



#  EVEN MAKER - Given a word, return only even letters of the string
def even_maker(string):                  
    mylist = []                          
    for i in range(len(string)):
        if i % 2 == 0:
            mylist.append(string[i])     
    return mylist
print(even_maker('Hello'))



#  OLD TRAFFORD - Create a function that reverses words in a sentence
def old_trafford(sen):
    split_word = sen.split()
    split_word_r = split_word[::-1]

    return ' '.join(split_word_r)  #   ''.join(), if you dont do it it will put the words in a list

result = old_trafford('Hello my name is')   
print(result)





