import random as r


# Sprawozdanie 4 z Zad. 7-11 Krzysztof Jósiak 122349
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# całość zrobiłem jako klasę, gdyż chciałem je sobie jeszcze przećwiczyć
# funkcje do zadania są odrazu pod właściwym zadaniem


class Scripts:

    def __init__(self):
        pass

    def zad_7(self):
        """ Użyj slicingu lub metod string do wyciągnięcia wartości liczbowych ze zmiennej nutrition_facts.
            Te wartości to protein, fat, carbohydrates oraz calories. Umieść te wartości w słowniku z
            kluczami o tych samych nazwach: "calories", "fat", "carbohydrates", "protein". Funkcja powinna
            zwracać taki słownik. """
        nutrition_facts = """Nutrition facts
                            Sources include: USDA
                            Steak
                            271 Calories
                            - 100 grams
                            Nutrient Amount(g) DV(%)
                            Total Fat 19 g 29%
                            Cholesterol 78 mg 26%
                            Sodium 58 mg 2%
                            Potassium 279 mg 7%
                            Total Carbohydrate 0 g 0%
                            Protein 25 g 50%"""
        
        nutrition = self.extract_nutrition(nutrition_facts)
        for key, value in nutrition.items(): #wypisywanie wartości
            print(f"{key}: {value}") 

    def extract_nutrition(self,nutrition_facts:str)->dict:
        nutrition_facts =nutrition_facts.split("\n")
        for line in nutrition_facts: # iteracja po liniach sprawdza czy w linii jest interesująca nas informacja i ją wyciąga
            if "Protein" in line: 
                protein = int(line.split()[1]) 
            if "Total Fat" in line:
                fat = int(line.split()[2])
            if "Total Carbohydrate" in line:
                carbohydrates = int(line.split()[2])
            if "Calories" in line:
                calories = int(line.split()[0])

        return {"calories":calories,"fat":fat,"carbohydrates":carbohydrates,"protein":protein}
            
    def zad_8(self):
        """ Utwórz losową listę składającą się z 10 liczb w zakresie od 1500 do 2500 korzystając z
        biblioteki random. Napisz funkcję, która przyjmie tę listę jako argument i zwróci nową listę
        zawierającą tylko te liczby, które przekraczają 2200. Zwróć również ich indeksy. """
        random_numbers = self.check_list()

        for index, number in enumerate(random_numbers):# wypisywanie indeksów i wartości z wykorzystaniem enumerate czyli indeksowanie
            print(f"{index} : {number}")
        
    def random_ten(self)->list:# generowanie 10 liczb losowych
        number_list=[]
        for n in range(10):
            number_list.append(r.randint(1500,2500))

        return number_list
    
    def check_list(self)->list:
        new_list = []
        random_numbers = self.random_ten()
        for number in random_numbers:# sprawdzanie czy liczba jest większa od 2200 i zwracanie listy
            if number > 2200:
                new_list.append(number)
        return new_list

    def zad_9(self):
        """ Biorąc pod uwagę listę dystansów przebiegniętych w ciągu tygodnia (lista zaczyna się od
            poniedziałku, lista ma dokładnie 7 elementów, po jednym na każdy dzień), napisz funkcję, która
            zwraca łączny dystans przebiegnięty w dni robocze (od poniedziałku do piątku), oraz drugą
            funkcję, która zwraca łączny dystans przebiegnięty w weekend (sobota i niedziela). Obie funkcje
            powinny przyjmować listę dystansów jako argument i zwracać tylko wynik. """
        weekly_distances = [5.2, 8.4, 7.0, 3.5, 6.0, 12.3, 14.0]
        weekday_distance = self.weekday_distance(weekly_distances)# wywołanie funkcji zwracającej dystans w dni robocze
        weekend_distance = self.weekend_distance(weekly_distances)# wywołanie funkcji zwracającej dystans w weekend
        print(f"Dystans przebiegnięty w dni robocze: {weekday_distance}km")
        print(f"Dystans przebiegnięty w weekend: {weekend_distance}km")

    def weekday_distance(self,distances:list)->int:
        sum_distance = sum(distances[:5])# sumowanie dystansów od poniedziałku do piątku (0:5]
        return sum_distance
    
    def weekend_distance(self,distances:list)->int:
        sum_distance = sum(distances[5:])# sumowanie dystansów w weekend (5:7]
        return sum_distance

    def zad_10(self):
        """ Stwórz listę ulubionych ćwiczeń z Twojego planu treningowego (lista może początkowo być
            pusta lub wypełniona). Dodaj dwa dowolne ćwiczenia na początku listy oraz dwa na jej końcu.
            Oblicz liczbę ćwiczeń na liście. Jeśli jest parzysta, dodaj jeszcze jedno ćwiczenie. Usuń
            ćwiczenie znajdujące się w środku listy. Posortuj pozostałe ćwiczenia w kolejności
            alfabetycznej. """
        activities = ["bieganie", "rower", "siłownia", "pływanie"]
        
        activities.append("joga")# dodanie na koniec listy
        activities.append("spacer")

        activities.insert(0,"fitness")# dodanie na początek listy
        activities.insert(0,"trójbój siłowy")

        if len(activities) % 2 == 0:# sprawdzenie czy liczba elementów jest parzysta i dodanie elementu w środku
            activities.append("rower stacjonarny")
        activities.pop((len(activities) // 2))

        activities.sort()# sortowanie listy
        print(activities)    

    def zad_11(self):
        """ Korzystając z funkcji sorted() (znajdź jak działa w dokumentacji) przygotuj listę treningów
            posortowaną od palącego najwięcej kcal w dół. Wydrukuj wynik na ekran. sorted() może przyjąć
            argument key, aby określić, na podstawie czego sortować - będzie mu potrzebna funkcja
            pomocnicza. """
        workouts = {
            "Bieganie (8 km/h)": 500,
            "Jazda na rowerze (średnia intensywność)": 400,
            "Pływanie": 550,
            "Skakanie na skakance": 600,
            "Marsz (5 km/h)": 250,
            "Trening siłowy": 300,
            "Joga": 200
            }
        sorted_workouts = self.sort_workouts(workouts)# wywołanie funkcji sortującej treningi
        print(sorted_workouts)

    def sort_workouts(self,workouts:dict)->dict:
        # sortowanie po wartościach x[1] z wykorzystaniem funkcji pomocniczej lambda 
        return dict(sorted(workouts.items(), key=lambda x: x[1], reverse=True))

        


if __name__ == "__main__":
    s = Scripts()
    s.zad_11()
   