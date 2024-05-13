#30 min
import re

def declination (userInput):

    endingForNumber = {
        "0": "ов",
        "2": "а",
        "3": "а",
        "4": "а",
        "5": "ов",
        "6": "ов",
        "7": "ов",
        "8": "ов",
        "9": "ов"
    }

    #ending initizlization valid for 1, 21, 31, etc..
    ending = ""

    #exception cases for endings (111, 123214, 1512, etc)
    if re.match(r".*(11|12|13|14)$", userInput):
        ending = "ов"
    #standart cases for ending
    else:
        for k, v in endingForNumber.items():
            if userInput[-1] == k:
                ending = v
    print (f'{userInput} копмьютер{ending}')

while True:
    t = input('Введите число и я просклоняю слово \'компьютер\': ')
    #key phrase to end the dialog
    if t.lower() == 'стоп':
        print('Пока')
        break
    else:
        #check if user input is a number
        if t.isdigit() == False:
            print('С нечисленными символами и отрицательными числами я не смогу работать :(')
        else:
            declination(t)
