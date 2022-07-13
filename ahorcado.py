import random
import os


def run():
    HANGMANPICS = ['''
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
    DB = [
        'Aatrox',
'Ahri',
'Akali',
'Akshan',
'Alistar',
'Amumu',
'Anivia',
'Annie',
'Aphelios',
'Ashe',
'AurelionSol',
'Azir',
'Bardo',
'Blitzcrank',
'Brand',
'Braum',
'Caitlyn',
'Camille',
'Cassiopeia',
'ChoGath',
'Corki',
'Darius',
'Diana',
'DrMundo',
'Draven',
'Ekko',
'Elise',
'Evelynn',
'Ezreal',
'Fiddlesticks',
'Fiora',
'Fizz',
'Galio',
'Gangplank',
'Garen',
'Gnar',
'Gragas',
'Graves',
'Gwen',
'Hecarim',
'Heimerdinger',
'Illaoi',
'Irelia',
'Ivern',
'Janna',
'JarvanIV',
'Jax',
'Jayce',
'Jhin',
'Jinx',
'KaiSa',
'Kalista',
'Karma',
'Karthus',
'Kassadin',
'Katarina',
'Kayle',
'Kayn',
'Kennen',
'KhaZix',
'Kindred',
'Kled',
'KogMaw',
'LeBlanc',
'LeeSin',
'Leona',
'Lillia',
'Lissandra',
'Lucian',
'Lulu',
'Lux',
'MaestroYi',
'Malphite',
'Malzahar',
'Maokai',
'MissFortune',
'Mordekaiser',
'Morgana',
'Nami',
'Nasus',
'Nautilus',
'Neeko',
'Nidalee',
'Nocturne',
'NunuyWillump',
'Olaf',
'Orianna',
'Ornn',
'Pantheon',
'Poppy',
'Pyke',
'Qiyana',
'Quinn',
'Rakan',
'Rammus'
'RekSai',
'Rell',
'RenataGlasc',
'Renekton',
'Rengar',
'Riven',
'Rumble',
'Ryze',
'Samira',
'Sejuani',
'Senna',
'Seraphine',
'Sett',
'Shaco',
'Shen',
'Shyvana',
'Singed',
'Sion',
'Sivir',
'Skarner',
'Sona',
'Soraka',
'Swain',
'Sylas',
'Syndra',
'TahmKench',
'Taliyah',
'Talon',
'Taric',
'Teemo',
'Thresh',
'Tristana',
'Trundle',
'Tryndamere',
'TwistedFate',
'Twitch',
'Udyr',
'Urgot',
'Varus',
'Vayne',
'Veigar',
'VelKoz',
'Vex',
'Vi',
'Viego',
'Viktor',
'Vladimir',
'Volibear',
'Warwick',
'Wukong',
'Xayah',
'Xerath',
'XinZhao',
'Yasuo',
'Yone',
'Yorick',
'Yuumi',
'Zac',
'Zed',
'Zeri',
'Ziggs',
'Zilean',
'Zoe', 
'Zyra'
]
    

    word = random.choice(DB)
    spaces = ['_'] * len(word)
    attemps = 6

    while True:
        os.system('clear')
        for character in spaces:
            print(character, end=' ')
        print(HANGMANPICS[attemps])
        letter = input('Elige una letra: ')

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        if not found:
            attemps -= 1

        if '_' not in spaces:
            os.system('clear')
            print('Ganaste. Alto lolero')
            break
            input()

        if attemps == 0:
            os.system('clear')
            print('Perdiste. Te falta grieta')
            break
            input()


if __name__ == '__main__':
    run()