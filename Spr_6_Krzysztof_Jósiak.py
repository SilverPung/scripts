import random as r
import datetime as dt

# Sprawozdanie 6 Krzysztof Jósiak 122349 zad 8-10 oraz zad 1-4
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# funkcje do zadania są odrazu pod właściwym zadaniem

class Scripts:
    def zad_8(self):
        """ Weź z Lab.1 swój kod, który kalkuluje Basal Metabolic Rate (BMR) - podstawowa przemianę
            materii. (lab 1 zad 2). Kod używał równania Harrisa-Benedicta. Pobierał od użytkownika
            wysokość (w cm), wagę (w kg), wiek i płeć.
            Dla mężczyzn: BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            Dla kobiet: BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            Przerób go na funkcję calculate_BMR(wysokosc,waga,wiek,plec).

            Stwórz 10-elementową listę słowników (klucze: wysokosc,waga,wiek,plec), zapełnij je
            wartościami wygenerowanymi przy pomocy random.
            Napisz pętle która oblicza BMR dla każdego z tych elementów i drukuje wartości ze słownika
            oraz obliczone BMR. """
        data=[]
        for n in range (10):# pętla tworzaca 10 elementową liste słowników
            data.append({"height":r.randint(150,210),"weight":r.randint(50,150),"age":r.randint(13,120),"sex":r.choice(["M","K"])})
        for person in data:# pętla obliczająca BMR dla każdego elementu listy
            print(f"Wzrost: {person['height']} Waga: {person['weight']} Wiek: {person['age']} Płeć: {person['sex']}")
            bmr = self.calculate_BMR(person['weight'],person['height'],person['age'],person['sex'])
            print(f"BMR: {bmr:.2f}")
    
    def calculate_BMR(self,weight:int,height:int,age:int,sex:str)->float:
        if sex.lower() == 'k':
            return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        elif sex.lower() == 'm':
            return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        
    def zad_9(self):
        """ Napisz program, który znajdzie pary produktów spożywczych z podanego słownika, gdzie
            całkowita wartość kaloryczna pary nie przekracza docelowego zapotrzebowania kalorycznego.
            Ustaw docelową wartość kalorii losowo w zakresie 150-400. """
        produkty = {
        "Jabłko": 95,
        "Banan": 105,
        "Marchewka": 25,
        "Kanapka": 350,
        "Sałatka": 150,
        "Jogurt": 100
        }
        calories_goal = r.randint(150,400)
        print(f"Docelowe kalorie: {calories_goal}")
        product_list =[]
        # pętla tworząca listę par produktów
        for key, value in produkty.items():
            for key2, value2 in produkty.items():
                if value + value2 <= calories_goal and key != key2:
                    product_list.append((key,key2))
        # usunięcie duplikatów z listy sortując elementy w krotkach i zamieniając je na zbiór, który nam automatycznie usunie duplikaty
        product_list = set(tuple(sorted(product)) for product in product_list)
        for product in product_list:
            print(f"{product[0]} + {product[1]} = {produkty[product[0]]+produkty[product[1]]}")

    def zad_10(self):
        """ Wykorzystaj instrukcje match i case i stwórz spersonalizowany planer aktywności, który
            sugeruje codzienne aktywności na podstawie danych o obecnej pogodzie. Funkcja
            planerAktywności() realizująca to zadanie powinna przyjmować tylko stan pogody i
            zwracać rekomendacje.
            Przechwyć wynik funkcji w zmiennej i wydrukuj ją na ekran. """
        
        choices = ['słonecznie', 'deszczowo', 'wieje', 'śnieg']
        wheather = r.choice(choices)# losowanie pogody
        print(f"Pogoda: {wheather}")
        activity = self.activity_planer(wheather.lower())
        print(f"Zalecana aktywność: {activity}")

    def activity_planer(self,wheather:str)->str:
        if wheather.lower() == "słonecznie":
            return "Rower"
        elif wheather.lower() == "deszczowo":
            return "Basen"
        elif wheather.lower() == "wieje":
            return "Kitesurfing"
        elif wheather.lower() == "śnieg":
            return "Warhammer 40k"# ;)
        
    def zad_1(self):
        """ Napisz funkcję validate_age(age), która sprawdza, czy podany wiek jest liczbą całkowitą
            dodatnią w zakresie od 13 do 120. Jeśli wiek jest niepoprawny, funkcja powinna podnieść
            wyjątek ValueError z odpowiednim komunikatem. Następnie napisz program, który:
            Pobiera od użytkownika wiek.
            Używa funkcji validate_age(age) do walidacji danych.
            Obsługuje wyjątek i wyświetla komunikat błędu, jeśli wiek jest niepoprawny
            Przykład: Użytkownik wpisuje 10.
            Program wyświetla: "Błąd: Wiek musi być liczbą całkowitą od 13 do 120." """
        age = input("Podaj wiek: ")
        error = self.validate_age(age)
        if error:
            print(error)
        else:
            print("Wiek poprawny")

    def  validate_age(self,age:str)->ValueError:
        try:
            age = int(age)# próba zamiany na liczbę
        except:
            return ValueError("Błąd: Wiek musi być LICZBĄ całkowitą od 13 do 120.")
        if age < 13 or age > 120:
            return ValueError("Błąd: Wiek musi być liczbą całkowitą od 13 do 120.")
        
    def zad_2(self):
        """ Napisz program, który:
            Prosi użytkownika o podanie dwóch liczb.
            Próbuje wykonać dzielenie pierwszej liczby przez drugą.
            Obsługuje następujące wyjątki:
            ValueError – jeśli użytkownik nie poda liczby.
            ZeroDivisionError – jeśli druga liczba (dzielnik) wynosi zero.
            Wyświetla odpowiednie komunikaty w zależności od rodzaju błędu. """
        number1 = input("Podaj pierwszą liczbę: ")
        number2 = input("Podaj drugą liczbę: ")

        try:
            number1 = int(number1)
            number2 = int(number2)
            divide = number1/number2
        except ValueError:
            print("Błąd: Podane wartości nie są liczbami")
        except ZeroDivisionError:
            print("Błąd: Nie można dzielić przez zero")
        else:
            print(f"Wynik dzielenia: {divide:.2f}")
    
    def zad_3(self):
        """ Napisz program, który:
            - Wygeneruje listę 30 losowych liczb całkowitych z zakresu od 1500 do 2500.
            - Dodaj do listy string ‘duzo’ na początku listy
            - Dodaj do listy string ‘nic’ na końcu listy
            - Zapisze listę do pliku kcal_month.txt, iterując po każdym elemencie i zapisując go od
            nowej linijki """
        to_file = []
        for _ in range(30):
            number = r.randint(1500,2500)
            to_file.append(number)
        to_file.insert(0,"duzo")
        to_file.append("nic")
        with open("kcal_month.txt","w") as file:
            for line in to_file:
                file.write(str(line)+"\n")
            print("Zapisano do pliku")

    def zad_4(self):
        """ Otwórz plik kcal_month.txt, w którym każda linia zawiera liczbę całkowitą. Napisz program,
            który:
            Odczytuje liczby z pliku i zapisuje je w liście
            Waliduje, czy każda linia faktycznie zawiera liczbę całkowitą.
            Przechowuje w liście errors napotkane błędy.
            Sumuje wszystkie poprawne liczby.
            Wyświetla sumę na ekranie.
            Wyświetla średnią na ekranie.
            Wyświetla na ekranie napotkane błędy. """
        with open("kcal_month.txt","r") as file:
            data = file.readlines()
        numbers=[]
        errors = []
        for line in data:
            try:
                line = line.strip()# usuwa znaki białe takie jak 
                number = int(line)
                numbers.append(number)
            except ValueError:
                errors.append(f"Nieprawidłowa wartość: {line}")
        sum_numbers = sum(numbers)
        print(f"Suma liczb: {sum_numbers}")
        print(f"Średnia: {(sum_numbers/len(numbers)): .2f}")
        print("Błędy:")
        for error in errors:
            print(error)
    

if  __name__ == "__main__":
    s = Scripts()
    #s.zad_4()