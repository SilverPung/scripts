import datetime as dt
from Krzysztof_Jósiak_calculate import calculate_bmr, calculate_daily_calories
import textwrap
import itertools
import random as r

# Sprawozdanie 7 Krzysztof Jósiak 122349 zad 5-8
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# funkcje do zadania są odrazu pod właściwym zadaniem

class Scripts:

    def __init__(self):
        pass

    def zad_5(self):
        """Utwórz moduł (podmień nazwisko i imię na swoje) nazwisko_imie_calculate.py, w którym
            umieścisz funkcje:
            - calculate_bmr(weight, height, age, gender)- oblicza BMR na podstawie
            wzorów Harrisa-Benedicta.
            - calculate_daily_calories(bmr, activity_level) - oblicza dzienne
            zapotrzebowanie kaloryczne na podstawie BMR i poziomu aktywności.
            Napisz program, który:
            - Pobiera od użytkownika dane (waga, wzrost, wiek, płeć, poziom aktywności) z walidacją
            (również zakresów) i obsługą wyjątków.
            - Używa funkcji z modułu calculate do obliczeń.
            - Zapisuje wyniki do pliku raport_kalorie.txt w czytelnym formacie, tj:
            “Raport Kalorii
            --------------
            Imię: Jan
            Płeć: Mężczyzna
            Wiek: 30 lat
            Waga: 80 kg
            Wzrost: 180 cm
            -
            -
            Twoje BMR wynosi: 1765 kcal
            Dzienne zapotrzebowanie kaloryczne (poziom aktywności: średnia aktywność): 2736
            kcal
            “
            W przypadku wystąpienia błędu, zapisuje informację o błędzie do pliku errors.log wraz z
            datą i godziną. Np.
            [2024-10-12 14:35:22] ValueError: Niepoprawna wartość wagi:"""
        
        today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        name = input("Podaj imię: ")
        
        #inputing weight
        weight = input("Podaj wagę: ")
        try:
            weight=int(weight)
        except ValueError:
            self.save_error(f"{today} ValueError: Waga niepoprawna wartość: {weight}")
            return
        

        #inputing height
        height = input("Podaj wzrost: ")
        try:
            height=int(height)
        except ValueError:
            self.save_error(f"{today} ValueError: Wzrost niepoprawna wartość: {height}")
            return
        

        #inputing age
        age = input("Podaj wiek: ")
        try:
            age=int(age)
        except ValueError:
            self.save_error(f"{today} ValueError: Wiek niepoprawna wartość: {age}")
            return

        
        activity_level=input("""Podaj swój poziom aktywności: 
    1-Siedzący tryb życia (bez treningów)
    2-Lekka aktywność (treningi 1-3 dni w tygodniu) 
    3-Średnia aktywność (treningi 3-5 w tygodniu)
    4-Wysoka aktywność (treningi 6-7 w tygodniu)
    5-Absurdalna aktywność (intensywne treningi codziennie)\n""")
        try:
            activity_level=int(activity_level)
        except ValueError:
            self.save_error(f"{today} ValueError: Poziom aktywności musi być liczbą: {activity_level}")
        
        # inputing sex
        sex = input("Podaj płeć (M/K): ").capitalize()
        if sex not in ["M","K"]:
            self.save_error(f"{today} ValueError: Płeć musi być M lub K")
            return
        #checking if activity level is in range
        if activity_level not in range(1,6):
            self.save_error(f"{today} ValueError: Poziom aktywności musi być liczbą od 1 do 5")
            return
        
        bmr = calculate_bmr(weight,height,age,sex)
        daily_calories = calculate_daily_calories(bmr,activity_level)
        self.save_template(name,weight,height,age,sex,activity_level,bmr,daily_calories)
        
    def save_template(self, name: str, weight: int, height: int, age: int, sex: str, activity_level: int, bmr: float, daily_calories: float):
        acitivity_levels = {
            1: "Siedzący tryb życia",
            2: "Lekka aktywność",
            3: "Średnia aktywność",
            4: "Wysoka aktywność",
            5: "Absurdalna aktywność"
        }
        # używam textwrap zyb było widać co jest w pliku jako  
        report = textwrap.dedent(f"""\
            Raport Kalorii
            --------------
            Imię: {name}
            Płeć: {'Mężczyzna' if sex == 'M' else 'Kobieta'}
            Wiek: {age} lat
            Waga: {weight} kg
            Wzrost: {height} cm
            -
            -
            Twoje BMR wynosi: {bmr:.2f} kcal
            Dzienne zapotrzebowanie kaloryczne (poziom aktywności: {acitivity_levels[activity_level]}): {daily_calories:.2f} kcal
        """)
        # uzywam 'w' żeby nadpisać dane w pliku ale można użyć 'a' żeby dopisywać
        with open("raport_kalorie.txt", "w") as file:
            file.write(report)

    def save_error(self,error:str):
        # uzywam 'a' żeby dopisywać do pliku
        with open("errors.log","a") as file:
            file.write(error)

    def zad_6(self):
        """ Napisz program w Pythonie, który:
            Poprosi użytkownika o wpisanie swojego imienia i nazwiska, oddzielonych spacją (np.
            „Jan Kowalski”).
            Podzieli wprowadzone dane, aby oddzielić imię i nazwisko.
            Odwróci kolejność, tak aby wyświetlić „Kowalski, Jan”.
            Przechwyć wyjątek w którym użytkownik wpisze coś innego niż dwa słowa oddzielone
            spacją
            Przechwyć wyjątek w którym użytkownik użyje ctrl+c do przerwania działania programu
            Wydrukuj na ekran odwróconą kolejność imię - nazwisko (np. Jan Kowalski, Kowalski
            Jan) """
        
        try:
            name = input("Podaj imię i nazwisko: ")
        except KeyboardInterrupt:
            print("Przerwano działanie programu")
            return
        name.strip()
        name = name.split(" ")
        if len(name) != 2:
            print("Podaj dokładnie 2 słowa")
            return
        
        name = f"{name[1]} {name[0]}"

        print(name)

    def zad_7(self,exercises:list=["Pompki", "Przysiady", "Plank"]):
        """ Napisz program, który zwraca wszystkie możliwe unikalne podzbiory (kombinacje) ćwiczeń z
            podanej listy różnych ćwiczeń. """
        grouped = []
        grouped.append([])
        for  i in range(1,len(exercises)+1):
            #korzystam z itertools żeby uzyskać wszystkie kombinacje, gdyż jest to plus python'a że ma metody do większości zastosowań
            #wynik przez to jest w postaci tuple 
            grouped.extend(itertools.combinations(exercises,i))

        print(grouped)
        return grouped
                
    def zad_8(self,bmr:int=1800):
        """  Stwórz listę 15 list zawierającą listy 30 losowych liczb całkowitych powstających w
            wyniku mnożenia dwóch losowych liczb x i y, gdzie x jest w zakresie od 0 do 10000, a y
            w zakresie od 1 do 4.
            Jest to liczba wykonanych kroków przez 15 użytkowników przez miesiąc.
            - Oblicz średnią dzienną dla każdego użytkownika
            - Napisz funkcję, która tej średniej zwraca poziom aktywności zgodnie z poniższymi
            kategoriami:
            1. Siedzący tryb życia (bez treningów): = 1.2 (0 - 7499 kroków)
            2. Lekka aktywność = 1.375 (7500 - 13999 kroków)
            3. Średnia aktywność = 1.55 (14000 - 20999 kroków)
            4. Wysoka aktywność = 1.725 (21000 - 29999 kroków)
            5. Bardzo wysoka aktywność = 1.9 (30000+ kroków)
            - Korzystając ze swojego modułu nazwisko_imie_calculate wydrukuj na ekran
            - Poziom aktywności dla każdej z 15 list
            - Zakładając BMR = 1800, dzienne zapotrzebowanie kaloryczne na podstawie
            BMR i poziomu aktywności """
        steps=[]
        steps_average=[]
        for n in range(15):
            user_steps=[]
            for i in range(30):
                x=r.randint(0,10000)
                y=r.randint(1,4)
                user_steps.append(x*y)
            steps.append(user_steps)
            steps_average.append(sum(user_steps)/len(user_steps))

        for i in range(15):
            print(f"Użytkownik {i+1} średnia ilośc kroków: {steps_average[i]:.2f}")
            print(f"Poziom aktywności: {self.calculate_activity_level(steps_average[i])}")
            print(f"Zapotrzebowanie kaloryczne: {calculate_daily_calories(bmr,self.calculate_activity_level(steps_average[i])):.2f}")
            print("\n")

    def calculate_activity_level(self,steps:int)->int:
        if steps<7500:
            return 1
        if steps<14000:
            return 2
        if steps<21000:
            return 3
        if steps<30000:
            return 4   
        return 5

        

if __name__ == "__main__":
    s = Scripts()
    #s.zad_8()