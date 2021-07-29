def func():
    while  True:
        try:
            age = int(input())
            return age                           #break # когда будет integer STOP болот
        except  ValueError:                            # Exception:# any mistake
            print("Enter integer")
age = func()
print(age)
raise ValueError


