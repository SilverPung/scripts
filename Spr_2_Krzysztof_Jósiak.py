import datetime as dt
import calendar
import math

# Sprawozdanie 2 z Zad. 8-17 Krzysztof Jósiak 122349
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej w mainie
# w zadaniach pan w spominał że np mamy już jakieś dane, więc w funkcjach są parametry, które można podać, ale nie trzeba 
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# całość zrobiłem jako klasę, gdyż chciałem je przećwiczyć, lecz nie powinno to stanowić problemu, gdyż każda funkcja jest niezależna

class Tasks:

    def __init__(self): 
        self.CALORIES_TO_LOSE_1KG = 7700 
        # zrobiłem to jako stałą, gdyż sądziłem że częściej będę tego używał, no i żeby poćwiczyć klasy
    
    def zad_8(self,age:int=0):
        """ Napisz program obliczający ‘target heart rate zone’, która wynosi pomiędzy 50% a 85%
            maksymalnego tempa bicia serca (max heart rate).
            Max heart rate oblicza się wg wzoru: 220-wiek. """
        
        if age==0:
            age = int(input("Podaj swój wiek: "))

        max_heart_rate = 220 - age

        target_heart_zone= [max_heart_rate * 0.5, max_heart_rate * 0.85]

        print(f"Twój zakres tętna to {target_heart_zone[0]} - {target_heart_zone[1]}")

    def zad_9(self,calorie_goal:int=0):
        """ Napisz program, który na podstawie dziennego celu kalorycznego (wartość już masz) proponuje
            rozkład makroelementów. Wydrukuj na ekran ile gram każdego makroelementu może spożyć
            użytkownik, by trzymać makro w diecie.
            Makroelementy: białko: 4kcal na gram, węglowodany: 4kcal na gram, tłuszcze: 9kcal na gram.
            Diety:
                - białkowa : 40% białko, 25% węglowodany, 35% tłuszcze
                - ketogeniczna; 20% białko, 10% węgle, 70% tłuszcze
                - mięsożerna: 35% białko, 5% węgle, 60% tłuszcze """
        
        if calorie_goal==0:
            calorie_goal = int(input("Podaj dzienny cel kaloryczny: "))

        diet=int(input("Jaką dietę chcesz zastosować,\n 1-Białkowa\n 2-Ketogeniczna\n 3-Mięsożerna\n"))

        #lista diet, żeby można było wyświetlić jaką dietę wybrał użytkownik, zeby ładniej wyglądało
        diets = ["Białkowej", "Ketogenicznej", "Mięsożernej"]

        #obliczanie makroelementów na podstawie diety
        match diet:
            case 1:
                protein = calorie_goal * 0.4 / 4
                carbs = calorie_goal * 0.25 / 4
                fats = calorie_goal * 0.35 / 9

            case 2:
                protein = calorie_goal * 0.2 / 4
                carbs = calorie_goal * 0.1 / 4
                fats = calorie_goal * 0.7 / 9
                
            case 3:
                protein = calorie_goal * 0.35 / 4
                carbs = calorie_goal * 0.05 / 4
                fats = calorie_goal * 0.6 / 9

            case _:
                print("Nieprawidłowy rodzaj diety")
                return

        #zaokrąglenie do dwóch miejsc po przecinku, bo nie ma sensu pokazywać 8 miejsc po przecinku
        print(f"Na diecie {diets[diet-1]} powinieneś spożyć {round(protein,2)}g białka, {round(carbs,2)}g węglowodanów, {round(fats,2)}g tłuszczu")

    def zad_10(self):
        """ Napisz program, który wyświetli aktualną datę i godzinę, co może być użyteczne do logowania
            czasu treningu w aplikacji fitness """
            
        now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now)
          
    def zad_11(self,weight:float=0,target_weight:float=0,average_calorie_deficit:int=0):
        """ Na podstawie obecnej wagi użytkownika, docelowej wagi użytkownika i średniego dziennego
            deficytu kalorycznego oblicz ile dni będzie trwała dieta. Pamiętaj, że 1kg to około 7700kcal.
            Następnie pobierz timestamp chwili obecnej i podaj dzień zakończenia diety. """
        
        if weight==0:
            weight = float(input("Podaj swoją wagę: "))
        if target_weight==0:
            target_weight = float(input("Podaj swoją docelową wagę: "))
        if average_calorie_deficit==0:
            average_calorie_deficit = int(input("Podaj średni dzienny deficyt kaloryczny: "))    


        now=dt.date.today()
        #obliczanie ile dni zajmie schudnięcie do docelowej wagi
        weight_to_lose = weight - target_weight
        calories_to_lose = weight_to_lose * self.CALORIES_TO_LOSE_1KG
        days_to_lose = calories_to_lose / average_calorie_deficit

        #zaokrąglenie w górę, bo raczej nie chcemy schudnąć 0.5 dnia
        days_to_lose =  math.ceil(days_to_lose)

        #obliczanie daty zakończenia diety funkcją timedelta
        finish_date = now + dt.timedelta(days=days_to_lose)

        print(f"Schudnięcie {weight_to_lose} kg zajmie {days_to_lose} dni")
        print(f"Planowany dzień zakończenia diety to {finish_date}")

    def zad_12(self):
        """ Napisz program, który oblicza spalone kalorie podczas biegu po okręgu o podanym promieniu.
            Załóż, że każde przebiegnięte 100 metrów spala 10 kalorii. Przyjmij od użytkownika promień w
            metrach. """
        radius = float(input("Podaj promień okręgu w metrach: "))
        
        lenght = 2 * math.pi * radius
        
        METERS_PER_CALORIES = 10
    
        calories_burned = lenght / METERS_PER_CALORIES

        #Kalorie zaokrągliłem do dwóch miejsc po przecinku, bo irytowało mnie jak mieliśmy z 8 miejsc
        print(f"Spalisz {round(calories_burned,2)} kcal podczas biegu dookoła okręgu o promieniu {radius}m")

    def zad_13(self):
        """ Napisz program, który wyświetli pierwszy i ostatni element z listy dni, w których odbywają się
            treningi """
        
        workout_days=["Monday","Wednesday","Friday"]

        print("Pierwszy dzień treningowy to", workout_days[0])

        print("Ostatni dzień treningowy to", workout_days[-1])
        
    def zad_14(self):
        """ Napisz program, który na podstawie roku i miesiąca zwróci kalendarz, pomagając
            użytkownikowi planować sesje treningowe. """
        month = int(input("Podaj Miesiąc "))
        years = int(input("Poda Rok "))

        if month < 1 or month > 12:
            print("Nieprawidłowy miesiąc")
            return
        
        print(calendar.month(years, month))
        

    def zad_15(self):
        """ Napisz program, który obliczy różnicę w liczbie dni pomiędzy dwiema datami treningów
            użytkownika. """
        first_day=input("Podaj datę pierwszego treningu: (DD-MM-YYYY) ")
        second_day=input("Podaj datę drugiego treningu: (DD-MM-YYYY) ")

        first_day=dt.datetime.strptime(first_day, "%d-%m-%Y")
        second_day=dt.datetime.strptime(second_day, "%d-%m-%Y")

        delta=second_day-first_day

        #abs bo nie chcemy ujemnej liczby dni nawet jak ktoś poda datę w odwrotnej kolejności
        print(f"Między pierwszym a drugim treningiem minęło {abs(delta.days)} dni")
            
    def zad_16(self):
        """ Napisz program, który sumuje kalorie spożyte podczas trzech posiłków. Jeśli kalorie ze
            wszystkich trzech posiłków są takie same, program powinien wyświetlić komunikat “Weź nie oszukuj”. """
        
        first_meal=int(input("Podaj ilość kalorii w pierwszym posiłku: "))

        second_meal=int(input("Podaj ilość kalorii w drugim posiłku: "))

        third_meal=int(input("Podaj ilość kalorii w trzecim posiłku: "))
        
        if first_meal == second_meal == third_meal:
            print("Weź nie oszukuj")
            return
        
        total_calories = first_meal + second_meal + third_meal
        print(f"Łącznie zjadłeś {total_calories} kalorii")

    def zad_17(self,steps_count:int=0):
        """ Napisz program, który sprawdza, czy liczba kroków wykonanych w ciągu dnia jest parzysta czy
            nieparzysta. """
        if steps_count == 0:
            steps_count = int(input("Ile kroków zrobiłeś dzisiaj? "))

        if steps_count % 2 == 0:
            print("Wykonałeś parzystą liczbę kroków")
        else:
            print("Wykonałeś nieparzystą liczbę kroków")



if __name__ == "__main__":
    #trzeba wpisać nazwę zadania z parametrami lub bez np. tasks.zad_9(calorie_goal=1900) lub tasks.zad_9()
    tasks = Tasks()
    tasks.zad_16()

