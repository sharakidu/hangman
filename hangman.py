import random


def main():
    #load the words
    words = load_words()
    #start
    new_game = start_game()
    
    while new_game:
        #choose a noun
        word = get_noun(words) 
        #play
        play_game(word)      
        #start again? 
        new_game = start_game()
    
    
def start_game():
    start_game = input("Начать новую игру: 1 \nВыйти:             0\nВведите ваш выбор: ")
    if start_game == "1":
        return True
   
   
def load_words():
    with open ("hangman_words.txt", "r", encoding="utf-8") as input_file:
        return input_file.readlines()
            
            
def get_noun(words):
    return random.choice(words).strip("\n").strip()
      
      
def play_game(word):
    hidden_word = ["*"] * len(word)
    mistakes = 0
    draw_hangman(mistakes)
    display_hidden_word(hidden_word)
    wrong_letters = []

    while mistakes < 6:
        letter = get_letter()
        if letter not in word:
                mistakes += 1
                wrong_letters.append(letter)
        elif letter in hidden_word or letter in wrong_letters:
                print("буква уже введена")
        else:
            hidden_word = open_letter(letter, hidden_word, word)
        draw_hangman(mistakes)
        display_hidden_word(hidden_word)
        display_wrong_letters(wrong_letters)
        
        
        if "*" not in hidden_word:
            print("Поздравляю, вы отгадали слово!")
            break
    if mistakes >= 6:
        print("Вы проиграли.")
        print(f"Слово: {word}")
        print()
                

def get_letter():
    allowed_letters =['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                      'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
                      'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    letter = input("Введите букву: ").lower().strip()
    while letter not in allowed_letters or len(letter) > 1:
        print("Вы ввели недопустимый символ")
        letter = input("Введите букву: ").lower().strip()
    return letter
    
    
def open_letter(letter, hidden_word, word):
    for index in range(len(word)):
        if letter == word[index]:
            hidden_word[index] = letter
            return hidden_word
                    
      
      
def draw_hangman(mistakes):
    hangman_draw = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print(hangman_draw[mistakes])
    
    
def display_hidden_word(hidden_word):
    for letter in hidden_word:
        print(letter, end="")
    print()    
    
def display_wrong_letters(wrong_letters):
    print("Выбывшие буквы: ", end="")
    for letter in wrong_letters:
        print(letter, end=" ")
    print()
        
        
if __name__ == "__main__":
    main()