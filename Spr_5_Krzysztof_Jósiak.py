import random as r


# Sprawozdanie 5 Krzysztof Jósiak 122349 zad 1-7
# Wszystkie zadania są w jednym pliku, aby uruchomić konkretne zadanie trzeba wpisać do instrukcji warunkowej
# gdyż chciałem żeby można było uruchomić każde zadanie z osobna bez konieczności podawania danych
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# całość zrobiłem jako klasę, gdyż chciałem je sobie jeszcze przećwiczyć
# funkcje do zadania są odrazu pod właściwym zadaniem


class Scripts:

    def __init__(self):
        pass

    def zad_1(self):
        """ Użytkownik bierze udział w ‘30-day Push Up Challenge’. Napisz program który wyświetla
            użytkownikowi ile popek musi zrobić każdego dnia, zakładając, że zaczyna o 5ciu i codziennie
            musi zrobić 5 więcej, z wyjątkiem dnia odpoczynku - niedzieli. Program na koniec musi również
            podać ile pompek użytkownik wykonał sumarycznie przez te 30 dni. """
        number_of_pushups = 0
        total=0
        for n in range(30):
            if (n+1) % 7 == 0:
                print(f"Dzień {n+1} odpoczynek")
            else:
                number_of_pushups += 5
                print(f"Dzień {n+1} :{number_of_pushups} pompki")
                total+=number_of_pushups

        print(f"Łącznie pompki: {total}")        


    def zad_2(self):
        """ Napisz program, który pobiera od użytkownika proponowane hasło i zwraca mu komentarz
            czego brakuje w jego haśle - hasło musi zawierać wielką i małą literę, liczbę, znak specjalny,
            musi mieć przynajmniej 5 znaków. Wykorzystaj if do sprawdzenia każdego warunku, użyj listy
            bledy do zebrania wszystkich niespełnionych warunków. Wydrukuj rekomendacje na ekran.
            Niech użytkownik wpisuje do skutku (użyj pętli while), chyba, ze wpisze ‘wyjscie’. """
        while(True):
            password = input("Podaj hasło: (wyjscie aby zakończyć): ")
            if password == "wyjscie":
                break
            errors = self.check_password(password)
            if errors:
                for error in errors:
                    print(error)
            else:
                print("Hasło poprawne")
                break

    def check_password(self,password:str)->list:
        numbers = "1234567890"
        errors = [] 
        if len(password) < 5:
            errors.append("Hasło za krótkie")
        if password.lower() == password:
            errors.append("Hasło nie zawiera wielkich liter")
        if password.upper() == password:
            errors.append("Hasło nie zawiera małych liter")
        if password.isalnum():
            errors.append("Hasło nie zawiera znaków specjalnych")
        if not any(char in numbers for char in password):
            errors.append("Hasło nie zawiera cyfr")
        return errors
    

    def zad_3(self):
        """ Użyj operatorów logicznych, aby sprawdzić, czy osoba może uzyskać dostęp do programu
            siłowni dla juniorów na podstawie wieku i zgody rodziców. Osoba musi mieć ponad 13 lat i
            zgodę opiekuna, lub tylko ponad 18 lat. Jeśli osoba spełnia warunki, ustaw zmienną dostęp =
            1. Niech liczba lat będzie losową liczbą całkowitą i a zgoda opiekuna losową wartością
            boolean. W celu stworzenia losowych wartości użyj import random. """
        age = r.randint(1, 25)# losowy wiek od 1 do 25  bo łatwiej sprawdzić czy działa, i gdyż nie było podanego zakresu
        parent_agreed = r.choice([True, False])

        print(f"Wiek: {age}, zgoda rodziców: {parent_agreed}")
        access=0
        if age >= 18:
            access=1
        elif age >= 13 and parent_agreed:
            access=1
        
        print(f"Dostęp: {access}")


    def zad_4(self):
        """ Stwórz listę o nazwie ‘kroki’, która zawiera 1440 losowych elementów pomiędzy liczbami 0 a
            14. Użyj do tego pętli i biblioteki random. Jest to lista kroków wykonanych danego dnia,
            zapisywana co minutę. Zsumuj kroki i sprawdź, czy przekroczono 10 000 kroków. Na ekran
            napisz ‘Udało się osiągnąć cel’ jeśli liczba kroków przekracza 10k, ‘Nie udało się osiągnąć celu’,
            jeśli nie. """
        steps= []
        for n in range(1440):
            steps.append(r.randint(0,14))
        
        total = sum(steps)
        print(f"Łączna liczba kroków: {total}")
        if total >= 10000:
            print("Cel osiągnięty")
        else:
            print("Nie udalo się osiągnąć celu")  
    

    def zad_5(self):
        """ Stwórz listę o nazwie ‘HRM’, która zawiera 1440 losowych elementów pomiędzy liczbami 35 a
            190. Napisz program, który kategoryzuje listę odczytów tętna na różne strefy (spoczynkowa,
            spalanie tłuszczu, kardio, szczytowa) i zlicza, ile odczytów przypada na każdą z tych stref.
            Wydrukuj na ekran: Wiek osoby, Maksymalne tętno, wartości zakresów dla każdej strefy, liczbę
            pomiarów w każdej strefie. """
        HRM = []
        heart_rates={"Strefa spoczynkowa":0,"Strefa spalania tłuszczu":0,
                     "Strefa kardiologiczna":0,"Strefa intensywna":0}
                    # słownik do zliczania pomiarów w poszczególnych strefach tętna

        age = r.randint(13,120)
        heart_rate_max = 220 - age
        intensive_zone_treshold = 0.85 * heart_rate_max
        kardiologic_zone_treshold = 0.7 * heart_rate_max
        fat_burning_zone_treshold = 0.5 * heart_rate_max

        for n in range(1440):# dodajemy 1440 pomiarów i odrazu sprawdzamy w jakiej strefie się znajduje
            HRM.append(r.randint(35, 190))
            if HRM[n] > intensive_zone_treshold:
                heart_rates["Strefa intensywna"] += 1
            elif HRM[n] > kardiologic_zone_treshold:
                heart_rates["Strefa kardiologiczna"] += 1
            elif HRM[n] > fat_burning_zone_treshold:
                heart_rates["Strefa spalania tłuszczu"] += 1
            else:
                heart_rates["Strefa spoczynkowa"] += 1
                
        
        print (f"Wiek: {age}")
        print(f"Max HR: {heart_rate_max}")
        print(f"Strefa intensywna: {intensive_zone_treshold:.2f} : {heart_rate_max:.2f}")
        print(f"Strefa kardiologiczna: {kardiologic_zone_treshold:.2f} : {intensive_zone_treshold:.2f}")
        print(f"Strefa spalania tłuszczu: {fat_burning_zone_treshold:.2f} : {kardiologic_zone_treshold:.2f}")
        print(f"Strefa spoczynkowa: 35 : {fat_burning_zone_treshold:.2f}")
        print(f"Pomiary")
        for name, value in heart_rates.items():
            print(f" \t {name}: {value}")
    

    def zad_6(self):
        """  Używając pętli i instrukcji if wydrukuj na ekranie poniższy wzór:
            ******
            *
            ***
            *
            * """
        for n in range(5):
            if n == 0:
                  print("*"*6)
            elif n == 2:
                print("*"*3)
            else:
                print("*")


    def zad_7_for(self):
        """Napisz program, który wypisuje liczby od 1 do 10
            - Korzystając z pętli for
            - Korzystając z pętli while """
        for n in range(1,11):
            print(n)
    

    def zad_7_while(self):
        n=1
        while n<=10:
            print(n)
            n+=1


   
        




if __name__ == "__main__":
    s = Scripts()
    #s.zad_1()