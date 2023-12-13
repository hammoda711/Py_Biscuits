# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word=str(input("kol haga\n"))
user_word = user_word.upper()
for i in range(0, len(user_word)):
    
    if user_word[i] == "I" or user_word[i] == "A" or user_word[i] == "U" :
       continue
    print(user_word[i])