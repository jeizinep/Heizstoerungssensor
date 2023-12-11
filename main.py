from yaml import safe_load
from func2 import *

def fehlertext(digits=list):
    zustand = ()
    temp = None
    with open("Status.yml", "r") as file:
        fehler_bibliothek = safe_load(file)

    if type(digits[0]) == int:
        zustand = fehler_bibliothek['STATUSauto'][digits[0]]
        temp_list = digits[1:]
        temp = int(''.join(map(str, temp_list)))
    elif type(digits[0]) == str:
        if digits[0] == "H":
            zustand = fehler_bibliothek['H'][digits[1]]
            temp_list = digits[2:]
            temp = int(''.join(map(str, temp_list)))
        else:
            code_art_list = digits[0:2]
            code_art = ''.join(map(str, code_art_list))
            fehler_code_list = digits[2:]
            fehler_code = int(''.join(map(str, fehler_code_list)))
            zustand = fehler_bibliothek[code_art][fehler_code]

    return zustand, temp






def main():
    while True:
        anzeige = get_status("http://192.168.1.62:8080/?action=stream")

        print(anzeige)
        print(fehlertext(anzeige))



if __name__ == "__main__":
    main()