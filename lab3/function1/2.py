def f_to_c(Fahrenheit):
    centigrade=(5 / 9) * (Fahrenheit - 32)
    return centigrade

Fahrenheit=int(input())
centigrade=f_to_c(Fahrenheit)
print(centigrade)