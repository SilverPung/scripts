import math
import datetime


# Sprawozdanie 8 Krzysztof Jósiak 122349 zad 1-6
# wywołanianie kazdego zadania jest w specjalnej klasie Scripts, która ma metody zad_1, zad_2 itd.
# każde zadanie jest w osobnej metodzie, więc można je wywołać osobno
# polecenie zadania jest na początku każdej funkcji tak jak pan prosił
# nad klasą Srcipts są klasy tworzone do wykonania zadania, np User, FoodItem itd.



class Observer:
    def update(self, message):
        raise NotImplementedError("Podklasa musi zaimplementować metodę abstrakcyjną")

class Subject:
    def attach(self, observer):
        raise NotImplementedError("Podklasa musi zaimplementować metodę abstrakcyjną")
    def detach(self, observer):
        raise NotImplementedError("Podklasa musi zaimplementować metodę abstrakcyjną")
    def notify(self, message):
        raise NotImplementedError("Podklasa musi zaimplementować metodę abstrakcyjną")

class User:
    def __init__(self,height:int,weight:int,age:int,sex:chr,activity_level:float=1.2):
        """
        Args:
            height (int): height in cm
            weight (int): weight in kg
            age (int): age in years
            sex (chr): 'M' or 'K'
            activity_level (float, optional): activity level. Defaults to 1.2.
        """
        self.height = height 
        self.weight = weight
        self.age = age
        self.sex=sex
        self.activity_level = activity_level

    def calculate_bmr(self):
        if self.sex.lower() == 'k':
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        elif self.sex.lower() == 'm':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            raise ValueError("Invalid gender")
        return  bmr
    
    def calculate_daily_calories(self):
        bmr = self.calculate_bmr()
        return bmr*self.activity_level
    
    def calculate_bmi(self):
        return self.weight/((self.height/100)**2)

class FoodItem:
    def __init__(self,name:str,weight:int,proteinPer100g:float,carbsPer100g:float,fatsPer100g:float):
        """_

        Args:
            name (str): name of the food item
            weight (int): weight of the food item in grams
            proteinPer100g (float): protein content per 100g
            carbsPer100g (float): carbs content per 100g    
            fatsPer100g (float): fats content per 100g
        """
        self.name = name
        self.weight = weight
        self.proteinPer100g = proteinPer100g
        self.carbsPer100g = carbsPer100g
        self.fatsPer100g = fatsPer100g

    def calculate_calories(self):
        return (self.proteinPer100g*4 + self.carbsPer100g*4 + self.fatsPer100g*9)* self.weight/100
    def __add__(self,other):
        # dzielę przez 2, bo chcę średnią wartość odżywczą z dwóch produktów bo tak zrozumiałem z polecenia
        return FoodItem(self.name+" and "+other.name,self.weight+other.weight,(self.proteinPer100g+self.proteinPer100g)/2,(self.carbsPer100g+other.carbsPer100g)/2,(self.fatsPer100g+other.fatsPer100g)/2)
    def __str__(self):
        return f"{self.name}, {self.weight}g, {self.calculate_calories()} kcal"

class Exercise:
    def __init__(self,name:str,duration:int,MET:float):
        self.name = name
        self.duration = duration
        self.MET = MET

    def get_exercise_summary(self):
        print(f"Name: {self.name}")
        print(f"Duration: {self.duration}")
        print(f"MET: {self.MET}")

class CardioExercise(Exercise):
    def __init__(self,name:str,duration:int,MET:float,distance:int):
        super().__init__(name,duration,MET)
        self.distance = distance
    def get_exercise_summary(self):
        super().get_exercise_summary()# wywołanie metody z klasy bazowej
        print(f"Distance: {self.distance}")
    
class StrengthExercise(Exercise):
    def __init__(self,name:str,duration:int,MET:float,reps:int,sets:int):
        super().__init__(name,duration,MET)
        self.reps = reps
        self.sets = sets

    def get_exercise_summary(self):
        super().get_exercise_summary()# wywołanie metody z klasy bazowej
        print(f"Reps: {self.reps}")
        print(f"Sets: {self.sets}")

class MilestoneNotifier(Observer):
    def update(self, message):
        print(message)

class ProgressTracker(Subject):
    def __init__(self):
        self.weights = {}
        self.observers = []
    def add_weight_entry(self,date:datetime.date,weight:float):
        self.weights[date] = weight
        self.check_milestones(weight)
    def get_weight_entry(self,date:datetime.date):
        return self.weights[date]
    def weight_change_velocity(self):
        dates = list(self.weights.keys())
        weights = list(self.weights.values())
        return (weights[-1]-weights[0])/((dates[-1]-dates[0]).days)
    def __lt__(self,other):
        return self.weight_change_velocity() < other.weight_change_velocity()
    
    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def check_milestones(self,weight):
        if weight <= 70:
            self.notify(f"Masz wagę poniżej 70 kg")

class Scripts:
    def zad_1():
        """We wcześniejszych zadaniach masz funkcję, która kalkuluje BMR wykorzystując dane od
            użytkownika. Zrefaktoruj (zmień kod bez zmieniania jego funkcjonalności) swój kod tak, żeby
            stworzyć klasę User, która posiada atrybuty - height (int), weight (int), age(int), gender (m lub f),
            activity_lvl (wartość domyślna = 1.2), oraz metody do kalkulacji BMR, BMI i dziennego
            zapotrzebowania kalorycznego - calculteBMR(), calculateBMI(), dailyCalorieRequirement()
            (BMR*activity_lvl).
            Stwórz poniższe 2 instancje tych klas i wydrukuj na ekran ich BMR i BMI i
            dailyCalorieRequirement.
            user1 = User(height=185, weight=80, age=30, gender='m')
            user2 = User(height=160, weight=50, age=25, gender='f')"""
        user = User(180,80,25,'M',1.375)
        print(f"User bmr: {round(user.calculate_bmr(),2)}")
        print(f"User daily calories: {round(user.calculate_daily_calories(),2)}")
        print(f"User bmi: {round(user.calculate_bmi(),2)}")
        print("")
        user2 = User(160,60,25,'K')
        print(f"User2 bmr: {round(user2.calculate_bmr(),2)}")
        print(f"User2 daily calories: {round(user2.calculate_daily_calories(),2)}")
        print(f"User2 bmi: {round(user2.calculate_bmi(),2)}")

    def zad_2():
        """Stwórz klasę FoodItem, w celu efektywnego przedstawienia produktów spożywczych. Atrybuty
            klasy: name, weight, fatPer100, carbsPer100, proteinPer100 Metody: calculateCalories() -
            oblicza kcal danego dania zakładając, że
            Fat: 9 kcal/g
            Carbs: 4 kcal/g
            Protein: 4 kcal/g
            Weight określa wagę produktu
            Stwórz poniższe 3 instancje i wydrukuj obliczone kalorie
            chicken_breast = FoodItem('Chicken Breast', 200, 3.6, 0, 31)
            whey_powder = FoodItem('Whey Powder', 30, 1, 4, 24)
            eggs = FoodItem('Eggs', 50, 5, 1.1, 6)
        """ 
        chicken_breast = FoodItem('Chicken Breast', 200, 3.6, 0, 31)
        whey_powder = FoodItem('Whey Powder', 30, 1, 4, 24)
        eggs = FoodItem('Eggs', 50, 5, 1.1, 6)

        print(f"Chicken Breast calories: {round(chicken_breast.calculate_calories(),2)}")
        print(f"Whey Powder calories: {round(whey_powder.calculate_calories(),2)}")
        print(f"Eggs calories: {round(eggs.calculate_calories(),2)}")

    def zad_3():
        """Zaimplementuj metody magiczne, aby umożliwić dodawanie dwóch obiektów klasy FoodItem,
            co zaowocuje nowym obiektem FoodItem z odpowiednimi wartościami odżywczymi. Dodatkowo
            zaimplementuj metodę __str__, aby uzyskać czytelny format wyjściowy.
            Zdefiniuj metodę __add__, aby obsłużyć dodawanie.
            Upewnij się, że nowy obiekt FoodItem ma nazwę powstającą z połączenia dwóch
            wcześniejszych nazw, a przypisany jest do instancji caleDanie. Dodaj do siebie chicken_breast
            i eggs, wydrukuj zsumowane wartości. Wydrukuj calculateCalories dla nowego obiektu.
        """
        chicken_breast = FoodItem('Chicken Breast', 200, 3.6, 0, 31)
        eggs = FoodItem('Eggs', 50, 5, 1.1, 6)

        caleDanie = chicken_breast + eggs
        print(caleDanie)

    def zad_4():
        """Stwórz klasę bazową Exercise z atrybutami name, duration (w minutach) i MET. Następnie
            utwórz klasy pochodne CardioExercise i StrengthExercise, które dziedziczą po klasie Exercise.
            Dodaj specyficzne atrybuty dla każdej z klas pochodnych: distance dla CardioExercise oraz
            reps, sets dla StrengthExercise. Użyj funkcji super() żeby zainicjalizować atrybuty z klasy
            bazowej. Zaimplementuj metodę get_exercise_summary(), która drukuje wszystkie te
            informacje w klasie bazowej i przeciąż ją w podklasach, tak, by dodatkowo drukowała też
            atrybuty z podklas. Zainicjuj poniższe dwa obiekty i wydrukuj exercise summary dla obu.
            running = CardioExercise('Running', 30, 10, 5)
            weightlifting = StrengthExercise('Weightlifting', 45, 6, 8, 4)
        """
        running = CardioExercise('Running', 30, 10, 5)
        weightlifting = StrengthExercise('Weightlifting', 45, 6, 8, 4)

        running.get_exercise_summary()
        weightlifting.get_exercise_summary()

    def zad_5():
        """Opracuj klasę ProgressTracker, która będzie śledzić wagę użytkownika w czasie.
            Przechowuj dane w słownikach, gdzie kluczami będą daty.
            Zaimplementuj metodę 
            add_weight_entry() (dodanie wpisu wagi), 
            get_weight_entry()(wydobycie wagi wg daty),
            weight_change_velocity() (last weight - first weight) / time delta)
            Przeładuj jedną z metod magicznych do porównywania wartości (__lt__) tak, by zwracała True
            lub False w zależności od weight_change_velocity dwóch porównywanych instancji
            ProgressTracker.
            Zainicjuj poniższe obiekty i dodaj poniższe wartości:
            import datetime
            tracker1 = ProgressTracker()
            tracker2 = ProgressTracker()
            tracker1.add_weight_entry(datetime.date(2023, 11, 1), 78)
            tracker1.add_weight_entry(datetime.date(2023, 11, 15), 76)
            tracker2.add_weight_entry(datetime.date(2023, 11, 1), 82)
            tracker2.add_weight_entry(datetime.date(2023, 11, 15), 79)
            Wydrukuj na ekran odpowiedź na pytanie : tracker1 chudnie szybciej niż tracker2: True/False
        """ 
        tracker1 = ProgressTracker()
        tracker2 = ProgressTracker()
        tracker1.add_weight_entry(datetime.date(2023, 11, 1), 78)
        tracker1.add_weight_entry(datetime.date(2023, 11, 15), 76)
        tracker2.add_weight_entry(datetime.date(2023, 11, 1), 82)
        tracker2.add_weight_entry(datetime.date(2023, 11, 15), 79)

        print(tracker1 < tracker2)
    
    def zad_6():
        """ W tym zadaniu przeprowadzę Cię przez zastosowanie wzorca Observer (observer design
        pattern). Ten wzorzec jest przydatny, gdy wiele obiektów zależy od stanu jednego obiektu i
        wszystkie muszą zareagować na jego zmianę. Promuje luźne powiązanie (Loose coupling)
        między tymi obiektami, co ułatwia utrzymanie i rozbudowę systemu.
            1. Zdefiniuj interface Observer
            Jest to klasa abstrakcyjna lub interfejs zawierający metodę update() (lub podobną),
            która będzie wywoływana, gdy stan podmiotu ulegnie zmianie. Każda klasa, która chce
            działać jako obserwator, musi zaimplementować metodę update(), aby obsłużyć
            otrzymywane powiadomienia.
            class Observer:
            def update(self, message):
            raise NotImplementedError("Podklasa musi zaimplementować
            metodę abstrakcyjną")

            2. Zdefiniuj interfejs Subject
            Subject zarządza listą subskrypcji i wysyła powiadomienia do obserwatorów. Klasa
            będzie posiadała metody attach(), detach() i notify(). attach(): Dodaje
            obserwatora do listy subskrypcji. detach(): Usuwa obserwatora z listy subskrypcji.
            notify(): Informuje wszystkich zarejestrowanych obserwatorów o zmianie.
            class Subject:
            def attach(self, observer):
            raise NotImplementedError("Podklasa musi zaimplementować
            metodę abstrakcyjną")
            def detach(self, observer):
            raise NotImplementedError("Podklasa musi zaimplementować
            metodę abstrakcyjną")
            def notify(self, message):
            raise NotImplementedError("Podklasa musi zaimplementować
            metodę abstrakcyjną")

            3. Konkretna implementacja - ProgressTracker
            ProgressTracker ma mieć możliwość śledzenia postępów użytkownika i powiadamianie
            obserwatorów o ważnych zmianach, takich jak osiągnięcie celu.
            Klasa ProgressTracker musi dziedziczyć z klasy Subject.
            Dodaj do klasy ProgressTracker listę observers jako instance variable.
            Dodaj do klasy ProgressTracker definicję metody .attach(self, observer), która dodaje
            obserwatorów do listy observers.
            Dodaj do klasy ProgressTracker definicję metody .detach(self, observer), która usuwa
            obserwatorów z listy observers.
            Dodaj do klasy ProgressTracker definicję metody .notify(self, message), która iteruje
            przez listę observers i dla każdego observera na liście wywołuje metodę
            .update(message)
            Dodaj do klasy ProgressTracker definicję metody check_milestones(self, weight), która
            sprawdza, czy waga jest poniżej 70, jeśli tak, wywołuje self.notify((f"Masz wagę poniżej
            70 kg")
            Dodaj do metody add_weight_entry linijkę
            self.check_milestones(weight)
            
            4. Konkretny obserwator - MilestoneNotifier
            Zaimplementuj klasę MilestoneNotifier, która dziedziczy z klasy Observer. Zdefiniuj w
            niej metodę update(self, message), która wyświetla message na ekran.
            Na koniec wykonaj ten kod:
            tracker = ProgressTracker()
            notifier = MilestoneNotifier()
            tracker.attach(notifier)
            tracker.add_weight_entry('2023-11-20', 75)
            tracker.add_weight_entry('2023-11-21', 70)
            # Wyzwala powiadomienie """
        
        tracker = ProgressTracker()
        notifier = MilestoneNotifier()
        tracker.attach(notifier)
        tracker.add_weight_entry('2023-11-20', 75)
        tracker.add_weight_entry('2023-11-21', 70)

if __name__ == "__main__":
    Scripts.zad_6()



