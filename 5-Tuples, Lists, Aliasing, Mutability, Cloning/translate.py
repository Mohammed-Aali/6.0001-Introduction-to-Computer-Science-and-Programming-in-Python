EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
'eat':'mange', 'drink':'bois', 'John':'Jean',
'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
'mange':'eat', 'bois':'drink', 'Jean':'John',
'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translate_word(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word