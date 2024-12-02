# Sprawozdanie 1 z Zad. 1-7 Krzysztof Jósiak 122349
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej w mainie
# w zadaniach pan w spominał że np mamy już jakieś dane, więc w funkcjach są parametry, które można podać, ale nie trzeba 
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# są tez funkcje pomocnicze get_height(), get_weight(), get_activity_type() które zwracają wartości jakby nie były podane do funkcji, 
# ale to bardziej ze względuów na czytelność kodu niż na potrzebę
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił

def zad1():
    """ Zad 1.
    Napisz program który:
    1) prosi użytkownika o podanie swojego imienia
    2) następnie wyświetla wiadomość powitalną z użyciem tego imienia
    Funkcję przyjmowania danych z klawiatury znajdziesz w dokumentacji Pythona """
    name = input("Podaj swoje imię: ")
    print(f"Witaj {name}!")

def zad2():
    """Napisz program, który kalkuluje Basal Metabolic Rate (BMR) - podstawowa przemianę materii.
    Użyj równania Harrisa-Benedicta. Podbierz od użytkownika wysokość (w cm), wagę (w kg),
    wiek i płeć.
    Dla mężczyzn: BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    la kobiet: BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age) """

    BMR = get_BMR() #jest to w funkcji get_BMR() żeby można było użyć w zadaniu 3 jakby nie było podane

    print (f"Twoje BMR wynosi: {BMR} kcal\n")

def zad3(BMR:float=0)->float:

    """Po obliczeniu BMR, napisz program który mnoży BMR przez wskaźnik aktywności, przypisuje
        wyniki do zmiennych i drukuje wyniki na ekran:
        -   Siedzący tryb życia (bez treningów): BMR * 1.2
        -   Lekka aktywność (treningi 1-3 dni w tygodniu): BMR * 1.375
        -   Srednia aktywność (treningi 3-5 w tygodniu): BMR * 1.55
        -   Wysoka aktywność (treningi 6-7 w tygodniu): BMR * 1.725
        -   Absurdalna aktywność (intensywne treningi codziennie): BMR * 1.9 """
    
    if BMR==0:
        BMR = get_BMR() 


    activity_level=int(input("""Podaj swój poziom aktywności: 
    1-Siedzący tryb życia (bez treningów)
    2-Lekka aktywność (treningi 1-3 dni w tygodniu) 
    3-Średnia aktywność (treningi 3-5 w tygodniu)
    4-Wysoka aktywność (treningi 6-7 w tygodniu)
    5-Absurdalna aktywność (intensywne treningi codziennie)\n"""))

    activity_BMR=0    
    match activity_level:
        case 1:
            activity_BMR= BMR*1.2
        case 2:
            activity_BMR= BMR*1.375
        case 3:
            activity_BMR= BMR*1.55  
        case 4:
            activity_BMR= BMR*1.725
        case 5:
            activity_BMR= BMR*1.9
        case _:
            print("Nieprawidłowy poziom aktywności")      
    
    if activity_BMR>0:
        print(f"Twoje BMR wynosi: {activity_BMR} kcal")
        return activity_BMR
  
def zad4(height:int=0,weight:int=0):
    """ Masz już w sumie wysokość i masę użytkownika, przypisz do zmiennej BMI odpowiednią
    wartość: BMI = weight / (height_in_meters ** 2) """
    
    if height==0:
        height=get_height()
    if weight==0:
        weight=get_weight()    

    height_in_meters=height/100
    print(f"Twoje BMI wynosi {weight/height_in_meters**2}")

def zad5(BMR:float=0):

    """ Deficyt kaloryczny dla utraty wagi
        Napisz program, który oblicza, ile kalorii ktoś musi dziennie ograniczyć, aby stracić 1 kg w ciągu
        tygodnia. Jeden kilogram tłuszczu to około 7700 kalorii. Zapytaj użytkownika, ile kilogramów
        chce stracić w ciągu tygodnia, a następnie oblicz deficyt kaloryczny. Następnie wykorzystując
        wartość z zad 3. podaj użytkownikowi jego cel kaloryczny na dzień, oraz tygodniowy deficyt
        kaloryczny. """
    CALORIES_TO_LOSE_1KG = 7700
    # tutaj jeżeli nie podano BMR to obliczamy go z zad3 razem z aktywnością 
    # zdawało się że miało to więcej sensu niż bez , gdyż nien podał Pan w zadaniu BMR
    if BMR==0:
        BMR=zad3()

    weight_to_burn = float(input("Ile chcesz schudnąć kg w ciągu tygodnia? "))
    calories_to_burn = weight_to_burn * CALORIES_TO_LOSE_1KG
    calories_per_day = BMR - calories_to_burn / 7

    if calories_per_day < 0:
        print("Nie można schudnąć tyle w tak krótkim czasie")
    else:
        print(f"Twoje dzienne zapotrzebowanie kaloryczne wynosi {calories_per_day} kcal")

        print(f"Łącznie musisz spalić {calories_to_burn} kcal")

def zad6(weight:int=0):

    """ Oblicz kcal spalone w trakcie treningu.
        Napisz program obliczający ile kcal spali użytkownik w trakcie t minut treningu. Jego wagę już
        masz, spytaj ile czasu może poświęcić na trening.
        Calories Burned = MET * Weight (kg) * Duration (w godzinach)
        Bieganie 9.6 km/h : MET = 9.8
        Rower : MET = 8
        Box : MET = 7.8
        Spacer : Met = 3.8 """
    
    if weight==0:
        weight=get_weight()

    activity_type=int(input("""Podaj co chcesz trenować: 
    1-Bieganie
    2-Rower
    3-Box
    4-Chodzenie\n"""))
    
    training_duration=(int(input("Podaj czas treningu w minutach: ")))/60

    calories_burned=0
    match activity_type:
        case 1:
            calories_burned=training_duration*9.8*weight
        case 2:
            calories_burned=training_duration*8*weight
        case 3:
            calories_burned=training_duration*7.8*weight
        case 4:
            calories_burned=training_duration*3.8*weight
        case _:
            print("Nieprawidłowy rodzaj treningu")

    if calories_burned>0:
        print(f"Spalisz {calories_burned} kcal podczas treningu")

def zad7(weight:int=0):
    """  Korzystając z równań z zad 6. zapytaj użytkownika ile kcal chce spalić, następnie podaj mu ile
        czasu musi spędzić wykonując 4 czynności - Bieganie, Rower, Box, Spacer."""
    
    if weight==0:
        weight=get_weight()

    activity_type=get_activity_type()
    calories_to_burn=int(input("Ile kalorii chcesz spalić? "))   
    time_to_burn=0
    
    match activity_type:
        case 1:
            time_to_burn=calories_to_burn/(9.8*weight)
        case 2:
            time_to_burn=calories_to_burn/(8*weight)
        case 3:
            time_to_burn=calories_to_burn/(7.8*weight)
        case 4:
            time_to_burn=calories_to_burn/(3.8*weight)
        case _:
            print("Nieprawidłowy rodzaj treningu")
        
    if time_to_burn>0:
        print(f"Musisz spędzić {time_to_burn*60} minut(y) na treningu, aby spalić {calories_to_burn} kcal")


def get_activity_type()->int:
    
    #funkcja zwracająca rodzaj treningu

    activity_type=int(input("""Podaj co chcesz trenować: 
    1-Bieganie
    2-Rower
    3-Box
    4-Chodzenie\n"""))
    return activity_type

def get_weight()->int:
    #funkcja zwracająca wagę jakby nie była podana
    weight=int(input("Podaj swoją wagę w kg: "))
    return weight

def get_height()->int:
    #funkcja zwracająca wzrost jakby nie był podany
    height=int(input("Podaj swój wzrost w cm: "))
    return height

def get_BMR()->float:
    #funkcja zwracająca BMR jakby nie był podany albo do zad2
    height = float(input("Podaj swój wzrost w cm: "))
    weight = float(input("Podaj swoją wagę w kg: "))
    age = int(input("Podaj swój wiek: "))
    sex = input("Podaj swoją płeć (M/K): ")
    
    BMR = 0
    #sprawdzamy płeć i obliczamy BMR
    if sex.lower() == 'k':
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif sex.lower() == 'm':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    return BMR


if __name__ == "__main__":
    #trzeba wpisać nazwę zadania z parametrami lub bez np. zad3(BMR=2000) lub zad3()
    pass