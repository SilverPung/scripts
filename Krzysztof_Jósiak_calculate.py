
def calculate_bmr(weight, height, age, sex)->float:
    """ Calculate Basal Metabolic Rate based on weight [kg], height [cm], age [years] and sex [M/F] """
    if sex.lower() == 'k':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif sex.lower() == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        raise ValueError("Invalid gender")
    return  bmr

def calculate_daily_calories(bmr, activity_level)->float:
    """ Calculate daily calories based on Basal Metabolic Rate and activity level """
    match activity_level:
        case 1:
            activity_bmr=   bmr*1.2
        case 2:
            activity_bmr=   bmr*1.375
        case 3:
            activity_bmr=   bmr*1.55  
        case 4:
            activity_bmr=   bmr*1.725
        case 5:
            activity_bmr=   bmr*1.9
        case _:
            #print("Nieprawidłowy poziom aktywności") 
            pass     
    
    if activity_bmr>0:
        #print(f"Twoje   bmr wynosi: {activity_bmr} kcal")
        return activity_bmr