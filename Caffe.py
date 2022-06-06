import pyttsx3


engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 5)


pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

engine.say('Какой торт Вы хотели бы приобрести? ')
engine.runAndWait()
    buy = input('Какой торт Вы хотели бы приобрести: ').lower()
engine.say('Что Вы хотели бы уточнить? ')
engine.runAndWait()
look = input('Что Вы хотели бы уточнить: ').lower()

for k,v in pastry.items():
     if k == buy:
         if look == "описание":
             engine.say(f"торт {k} состоит из {v[0]}")
             engine.runAndWait()
             print(f"торт {k} состоит из {v[0]}")
         elif look == "цена":
             engine.say(f"торт {k} стоит рублей {v[1]}")
             engine.runAndWait()
             print(f"торт {k} стоит рублей {v[1]}")
         elif look == "количество":
             engine.say(f"торта {k} осталось грамм {v[-1]}")
             engine.runAndWait()
             print(f"торта {k} осталось грамм {v[-1]}")
         elif look == "купить":
            engine.say("Сколько торта Вам положить? ")
            engine.runAndWait()
            gr = int(input("Сколько торта Вам положить: "))
            engine.say(f"к оплате {v[1] * gr / 100}")
            engine.runAndWait()
            print(f"к оплате {v[1] * gr / 100}")
            engine.say(f"торта {k} осталось грамм {v[-1] - gr}")
            engine.runAndWait()
            print(f"торта {k} осталось грамм {v[-1] - gr}")