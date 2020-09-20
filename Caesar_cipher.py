
print("Введите текст:")
Text = input().lower()

print("Введите кодовое слово:")
K_word = input()
K_word = K_word.lower()

print("Введите нужный алфавит (Rus/Eng):")
TypeAlphabet = input().lower()
if TypeAlphabet == 'rus':
    Alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
else:
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'

print("Введите индекс:")
index = int(input())
if TypeAlphabet == 'rus':
    while index > 32 or index < 0:
        print("Введен неккоректный индекс попробуйте еще раз")
        index = int(input())
else:
    while index > 25 or index < 0:
        print("Введен неккоректный индекс попробуйте еще раз")
        index = int(input())


def removeDuplicate(str):
    if (len(str)) < 2:
        return str

    result = []
    for i in str:
        if i not in result:
            result.append(i)

    return ''.join(result)


def removeDuplicateAlphabet(str,alphabet):
    result = []
    for i in alphabet:
        for j in str:
            if i == j:
                alphabet = alphabet.replace(i,'')

    return alphabet


def decipher(NewAlphabet,Alphabet,text):
    Text = []
    for character in text:
        try:
            index = NewAlphabet.index(character)
            character = Alphabet[index]
            Text.append(character)
        except ValueError:
            Text.append(character)
    return ''.join(Text)

def encrypt(NewAlphabet,Alphabet,text):
    Text = []
    for character in text:
        try:
            index = Alphabet.index(character)
            character = NewAlphabet[index]
            Text.append(character)
        except ValueError:
            Text.append(character)
    return ''.join(Text)


K_word = removeDuplicate(K_word)
print('\nНормализованное слово:' + K_word)

NewAlphabet = removeDuplicateAlphabet(K_word,Alphabet)
NewAlphabet = NewAlphabet[:index]+K_word+NewAlphabet[index:]
print('\nАлфавит с зашифрованным словом:' + NewAlphabet)

print("Зашифрованный текст: "+ encrypt(NewAlphabet,Alphabet,Text))
print("Расшифрованный текст: "+ decipher(NewAlphabet,Alphabet,encrypt(NewAlphabet,Alphabet,Text)))


