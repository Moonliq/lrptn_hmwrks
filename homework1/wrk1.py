def todo(age):
    if age < 3:
        return(f'You are {age} years old and you are Newborn')
    elif age >= 3 and age <= 6:
        return(f'You are {age} years old and you are Kindergartner')
    elif age > 6 and age <= 18:
        return(f'You are {age} years old and you are Schoolboy')
    elif age > 18 and age <= 24:
        return(f'You are {age} years old and you are Student')
    else:
        return (f'You are {age} years old and you are Worker')


print(todo(int(input('Your age please:'))))