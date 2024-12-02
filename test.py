"""
LAB 1 - Skryptowe języki programowania. Szymon Piórkowski gr. 4
Zad 1: Program prosi na początku użytkownika o podanie swojego imienia a następnie wyświetla wiadomość powitalną z jego imieniem
"""
name = str(input("Podaj swoje imie: \n"))
print(f"Witaj {name}!")

"""
Zad 2: Program pobiera od użytkownika: wzrost, wagę, wiek oraz płeć. Potem w zależności od wyboru płci dobiera odpowiedni wzór i kalkuje BMR
"""
height = float(input("Podaj wysokość (w cm)\n"))
weight = float(input("Podaj wagę (w kg)\n"))
age = int(input("Podaj wiek\n"))
sex = str(input("Podaj płeć: k - kobieta, m - mężczyzna\n"))
if sex == 'k' or sex == 'K' :
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    print(f"Twój BMR to: {bmr}")
elif sex == 'm' or sex == 'M':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    print(f"Twój BMR to: {bmr}")

"""
Zad 3:
"""
activity_type = int(input("Jaki masz styl życia? : \n 1 - siedzący tryb życia (bez treningów) \n 2 - lekka aktywność \n 3- średnia aktywność \n 4 - wysoka aktywność \n 5 - absurdalna aktywność"))
if activity_type == 1: #siedzący tryb życia
    pal = bmr * 1.2
    print("Twój wskaźnik wynosi: ", pal)
elif activity_type == 2: #lekka aktywność
    pal = bmr * 1.375
    print("Twój wskaźnik wynosi: ", pal)
elif activity_type == 3: #średnia aktywność
    pal = bmr * 1.55
    print("Twój wskaźnik wynosi: ", pal)
elif activity_type == 4: #wysoka aktywność
    pal = bmr * 1.725
    print("Twój wskaźnik wynosi: ", pal)
elif activity_type == 5: #absurdalna aktywność
    pal = bmr * 1.9
    print("Twój wskaźnik wynosi: ", pal)

"""
Zad 4: 
"""
height_in_meters = height * 100
bmi = weight/(height_in_meters**2)
print(f"Twoje BMI wynosi: {bmi}")

"""
Zad 5:
"""
#bmr = 2500
kilograms_to_lose = float(input("Ile chcesz stracić kilogramów w ciągu tygodnia?\n"))
caloric_deficit = 7700 * kilograms_to_lose
daily_caloric_goal = bmr - (caloric_deficit/7)
print(f"Twój cel kaloryczny na dzień wynosi {daily_caloric_goal}, a twój deficyt kaloryczny na tydzień wynosi {caloric_deficit}")
"""
Zad 6:
"""
minutes = int(input("Podaj ile minut chcesz poświęcić na trenning? \n"))
type_of_training = int(input("Wybierz jaki chcesz trening: \n 1 - bieganie 9,6 km/h \n 2 - rower \n 3 - box \n 4 - spacer \n"))
if type_of_training == 1:
    met = 9.8
elif type_of_training == 2:
    met = 8
elif type_of_training == 3:
    met = 7.8
elif type_of_training == 4:
    met = 3.8
calories_burrned = met * weight * (minutes/60)
print(f"Kalorie spalone podczas treningu: {calories_burrned}")
"""
Zad 7: 
"""
calories_burned_wanted = int(input("Podaj ile chcesz spalić kalori"))
training_duration_running = calories_burned_wanted / (9.8*weight)
training_duration_bike = calories_burned_wanted / (8*weight)
training_duration_box = calories_burned_wanted / (7.8*weight)
training_duration_walking = calories_burned_wanted / (3.8*weight)