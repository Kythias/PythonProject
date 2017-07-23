import enchant

correct_word = "Hello World!"
incorrect_word = "Hallo World!"
d = enchant.Dict("en_GB")

if d.check(correct_word) == True:
    print (correct_word)

if d.check(incorrect_word) == False:
    print ("All has gone according to plan")
