from config import keys

def get_sub():
    sub = input("Введите вещество: ")
    return sub

def divide(sub):
    l_el = []
    l_in = []
    l = []
    for i in range(len(sub)):
        if sub[i].isupper():
            l_el.append(sub[i])
            if i < len(sub)-1 and sub[i+1].islower():
                l_el[len(l_el)-1] = l_el[len(l_el)-1] + str(sub[i+1])
        elif sub[i].isdigit():
            if sub[i-1].isdigit():
                l_in[len(l_in) - 1] = l_in[len(l_in) - 1] + str(sub[i])
            else:
                l_in.append(sub[i])
            for j in range(len(l_el)-2):
                if l_el[len(l_el)-1] == l_el[j]:
                    del l_el[len(l_el)-1]
                    l_in[j] = str(int(l_in[j]) + int(l_in[len(l_in)-1]))
                    del l_in[len(l_in)-1]
        if (sub[i].isalpha() and i == len(sub) - 1) or (sub[i].isalpha() and sub[i+1].isupper()):
            l_in.append("1")
            for j in range(len(l_el)-2):
                if l_el[len(l_el)-1] == l_el[j]:
                    del l_el[len(l_el)-1]
                    l_in[j] = str(int(l_in[j]) + int(l_in[len(l_in)-1]))
                    del l_in[len(l_in)-1]
    l.append(l_el)
    l.append(l_in)
    return l

def get_sum(el, ind):
    sum = 0
    for i in range(len(el)):
        sum += float(keys[el[i]]) * int(ind[i])
    return sum

def check(sub):
    if len(sub) == 0 or not sub[0].isalpha():
        print("Некорректное вещество.")
        sub = get_sub()
        sub = check(sub)
    if sub[0].islower():
        print("Учитывайте регистр.")
        sub = get_sub()
        sub = check(sub)
    for i in range(len(sub)):
        if not sub[i].isdigit() and not sub[i].isalpha():
            print("Некорректное вещество.")
            sub = get_sub()
            sub = check(sub)
    for i in range(len(sub)-1):
        if (sub[i].islower() and sub[i+1].islower()) or (sub[i].isdigit() and sub[i+1].islower()):
            print("Учитывайте регистр.")
            sub = get_sub()
            sub = check(sub)
    for i in divide(sub)[0]:
        if i not in keys.keys():
            print("Некорректное вещество.")
            sub = get_sub()
            sub = check(sub)
            break
    return sub
