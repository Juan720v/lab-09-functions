def pluralize(word):
    if word == "moose":
        return "moose"
    elif word == "automaton":
         return "automata"
    elif word == "mouse":
        return "mice"
    else:
        word = word + "s"
        return word

userinput = str(input("Word please.. "))
userinput = pluralize(userinput)
print(userinput)
    
