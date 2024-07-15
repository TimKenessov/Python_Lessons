def is_year_leap(year):
    
    if year % 4 == 0:
        return True
    else:
        return False

year_to_check = 2023
leap_year = is_year_leap(year_to_check)

print(f"Год {year_to_check}: {leap_year}")
