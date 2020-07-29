from random_word import RandomWords
import os
def cleaing():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def length_of_word():
    while True:
        try:
            length_of_word = int(input("Enter maximum length of word [5-11]: "))
            if 4 < length_of_word <20:
                return length_of_word
            else:
                print ("Enter number [5-11 ")
        except ValueError as ve:
            print ("Enter valid number", ve)

def generating_random_word():
    x = length_of_word()
    r = RandomWords()
    word = r.get_random_word(maxLength=x)
    return word 


def play():
    word = generating_random_word().lower()
    r = [i for i in "*"*len(word)]
    life = 10
    while True:
        if word == ''.join(r):
            cleaing()
            print (word)
            print ("Hurray you  are winner")
            print ("you guess correct word")
            break
        else:
            if life == 0:
                cleaing()
                print (f"correct word is {word}")
                print ("hey You lose!!")
                print ("Please try next time")
                break
            else:
                cleaing()
                #print (word)
                print (f"**Length of your word is {len(word)}")
                print ("**You have left {}".format(life))
                list_of_word = [i for i in word]
                my_word = ''.join(r)
                print ("your word is {}".format(my_word))
                guess = input("Guess a alphabet: ")
                if guess in word:
                    a = []
                    for i in range(0,word.count(guess)):
                        y = list_of_word.index(guess)
                        a.append(y)
                        list_of_word.insert(y,"0")
                    for i in a:
                        r.pop(i)
                        r.insert(i,guess)
                else:
                    print ("wrong!! guess")
                    life -= 1  






if __name__ == "__main__":
    play()