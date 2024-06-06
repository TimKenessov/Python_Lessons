def bank(X, Y):
    
    return X * (1 + 0.10) ** Y


X = 135000  
Y = 50     
result = bank(X, Y)
print("Сумма на счету спустя", Y, "лет:", result, "рублей")