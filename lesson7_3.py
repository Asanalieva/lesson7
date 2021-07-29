def a_div_b(a,b=1): #b is default argument
    c = a / b
    return c

c = a_div_b(a_div_b(2,1),a_div_b(10,1)) #2 / 10 bolot = 0.2
print(c)
d = a_div_b(b = 2, a = 4) # можем менять места сами здесь
print(d)