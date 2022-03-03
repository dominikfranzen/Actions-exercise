from datetime import date

def calculate_age(birthdate, today):
    yearDifference = today.year - birthdate.year
    hadBirthdaythisyear = (today.month, today.day) < (birthdate.month, birthdate.day)
    if hadBirthdaythisyear :
        return yearDifference - 1
    return yearDifference