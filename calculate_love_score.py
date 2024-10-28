def calculate_love_score(name1, name2):
    lover= (name1+name2).lower()
    print(lover)
    names_check_true = 0
    letter_t = 0
    letter_r = 0
    letter_u = 0
    letter_e = 0
    letter_l = 0
    letter_o = 0
    letter_v = 0
    letter_e1 = 0
    names_check_love = 0
    
    for characters in lover:
        if characters == "t":
            names_check_true += 1
            letter_t += 1
        elif characters == "r":
            names_check_true += 1
            letter_r += 1
        elif characters == "u":
            names_check_true += 1
            letter_u += 1
        elif characters == "e":
            names_check_true += 1
            letter_e += 1
    print(f"""T occurs {letter_t} times
R occurs {letter_r} times
U occurs {letter_u} times
E occurs {letter_e} times
Total = {names_check_true}""")
    for characters in lover:
        if characters == "l":
            names_check_love += 1
            letter_l += 1
        elif characters == "o":
            names_check_love += 1
            letter_o += 1
        elif characters == "v":
            names_check_love += 1
            letter_v += 1
        elif characters == "e":
            names_check_love += 1
            letter_e1 += 1
    print(f"""L occurs {letter_l} times
O occurs {letter_o} times
v occurs {letter_v} times
E occurs {letter_e1} times
Total = {names_check_love}""")
    print(f"Love score =  {names_check_true}{names_check_love}")
calculate_love_score(name1 = "Kanye West", name2 = "Kim Kardashian")