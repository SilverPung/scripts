import datetime as dt

# Sprawozdanie 3 z Zad. 1-6 Krzysztof Jósiak 122349
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# całość zrobiłem jako klasę, gdyż chciałem je sobie jeszcze przećwiczyć
# funkcje do zadania są odrazu pod właściwym zadaniem

class Scipts:

    def __init__(self):
        pass 


    def zad_1(self):
        """ W aplikacji fitness śledzenie i wyświetlanie postępów w zorganizowany sposób jest kluczowe.
            Wyobraź sobie, że tworzysz tabelę, która pokazuje cotygodniowy postęp w utracie wagi. Aby
            tabela była łatwa do odczytania, musisz upewnić się, że zarówno tekst, jak i liczby są
            odpowiednio wyrównane, określając minimalną szerokość dla każdej kolumny. Użyj poniższego
            słownika, który śledzi utratę wagi w każdym tygodniu, i upewnij się, że kolumny danych są
            estetycznie wyrównane.
            Napisz pętlę, która iteruje przez słownik i drukuje tydzień oraz utratę wagi, sformatowane z
            minimalną szerokością 10 znaków dla tygodnia i z dwoma miejscami po przecinku dla utraty
            wagi. """
        
        progress = {'Week 1': 1.2, 'Week 2': 0.8, 'Week 3': 1.5} # utrata wagi w kg

        for week, weight in progress.items():
            print(f"{week:<10} {weight:.2f}kg")


    def zad_2(self):
        """ Lista Ćwiczeń (Listy i Metody)
            Stwórz dynamiczny plan ćwiczeń, używając list i metod.
            Napisz funkcję build_routine(), która zaczyna z pustą listą ćwiczeń i dodaje ćwiczenia przy
            pomocy append(). Użyj insert(), aby dodać rozgrzewkę na początku, oraz pop(), aby usunąć
            ćwiczenie schładzające na końcu """
        routine = self.build_routine(["Pompki", "Przysiady", "Plank"])
        print(routine)

    def build_routine(self,exercises:list)->list:
        training_routine = []
        for exercise in exercises:
            training_routine.append(exercise)
        
        training_routine.insert(0,"Rozgrzewka")
        training_routine.pop()

        return training_routine


    def zad_3(self):
        """ Cotygodniowy Raport Fitness (Listy)
            Przechowuj i uzyskuj dostęp do danych o cotygodniowym postępie za pomocą listy.
            Napisz funkcję weekly_progress_highlights(), która przyjmuje listę z dystansami przebiegniętymi
            w ciągu ostatnich 7 dni i zwraca krotkę zawierającą najdłuższy oraz najkrótszy bieg, sumę
            przebiegniętych kilometrów i średnią. Następnie wydrukuj na ekran te informacje. """
        distances = [5.0, 4.5, 6.0, 3.0, 5.5, 4.0, 6.5]
        progress = self.weekly_progress_highlights(distances)
        print(f"Największa: {progress[0]}km")
        print(f"Najmniejsza: {progress[1]}km")
        print(f"Suma: {progress[2]}km")
        print(f"Średnia: {progress[3]:.2f}km")

    def weekly_progress_highlights(self,distances:list)->tuple:
        
        sum_distance = sum(distances)
        avg_distance = sum_distance / len(distances)
        max_distance = max(distances)
        min_distance = min(distances)

        return max_distance,min_distance, sum_distance, avg_distance


    def zad_4(self,calories_number:int=None):
        """ Tracker kalori (słowniki).
            Napisz funkcję update_calories(), która przyjmuje (int) liczbę kalorii i dopisuje ją do słownika z
            dzisiejszą datą, którą funkcja uzyskuje automatycznie. Jeśli wpis już istnieje, nadpisz go.
            Funkcja powinna w argumentach przyjmować słownik calories i zwracać zaktualizowany słownik
            calories. """
        calories = {'2024-10-11': 2000, '2024-10-12': 2200}

        if calories_number is None:
            calories_number = int(input("Podaj liczbę kalorii: "))

        calories = self.update_calories(calories,calories_number)
        print(calories)

    def update_calories(self,calories:dict,calories_today:int)->dict:
        today = dt.date.today().strftime("%Y-%m-%d")
        calories[today] = calories_today
        return calories
    

    def zad_5(self):

        """ Stwórz słownik workout_log w którym numer sesji będzie unikatowym kluczem, a
            przechowywaną wartością będzie kolejny słownik, tym razem zawierający pary:
            "exercise": exercise, #string
            "duration": duration, #float
            "calories": calories #integer
            Napisz funkcję log_workout, która przyjmuje wartości exercise, duration, calories,
            workout_log. Funkcja ma dodawać wartości do słownika. Inkrementuj numer sesji. Funkcja
            powinna zwracać zaktualizowany słownik workout_log.
            Napisz kod dodający do tego słownika 3 wpisy (bez pobierania danych od uzytkownika,
            korzystając z funkcji `log_workout`). Napisz pętlę wyświetlającą te wpisy, iterując po słowniku
            workout_log. """
   
        workout_log = self.log_workout("Bieganie", 60, 500, {})
        workout_log = self.log_workout("Pływanie", 30, 300, workout_log)
        workout_log = self.log_workout("Joga", 45, 200, workout_log)
        for number, workout in workout_log.items():
            print(f"Ćwiczenie {number}: (exercise: {workout['exercise']}, duration: {workout['duration']} min, calories: {workout['calories']} kcal)")
    
    def log_workout(self,exercise:str,duraion:float,calories:int,workout_log:dict):
        workout={"exercise":exercise,"duration":duraion,"calories":calories}
        workout_log.update({len(workout_log)+1:workout})
        return workout_log


    def zad_6(self):
        """ Zarządzaj zestawem ćwiczeń, zapewniając, że nie ma duplikatów, używając zbiorów.
            Napisz funkcję unique_exercises(), która przyjmuje dwie listy ćwiczeń wykonywanych w ciągu
            tygodnia i zwraca zbiór unikalnych ćwiczeń, wykorzystując operację sumy zbiorów. Dodatkowo,
            znajdź różnicę między zbiorami, aby pokazać ćwiczenia, które były wykonywane w tygodniu
            pierwszym, ale nie w drugim. """
        
        week1 = ["Push-ups", "Squats", "Running", "Push-ups", "Push-ups",
        "Running"]
        week2 = ["Cycling", "Running", "Plank", "Cycling", "Cycling",
        "Running"]

        unique, unique_week1 = self.unique_exercises(week1, week2)
        print(f"Unikalne ćwiczenia: {unique}")
        print(f"Ćwiczenia z tygodnia 1 nie występujące w tygodniu 2: {unique_week1}")

    def unique_exercises(self,week1:list,week2:list)->tuple:
        set_week1 = set(week1)
        set_week2 = set(week2)
        unique = set_week1.union(set_week2)
        unique_week1 = set_week1.difference(set_week2)
        return unique, unique_week1

    
        
if __name__ == "__main__":
    #trzeba wpisać nazwę zadania z parametrami lub bez np. scripts.zad_4(calorie_goal=1900) lub scripts.zad_4()
    scripts=Scipts()
