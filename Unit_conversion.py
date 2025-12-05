def cm_to_m():
    cm = int(input("cm:"))
    print("m:",cm/100)

def m_to_cm():
    m = int(input("m:"))
    print("cm:",m*100)

def kg_to_g():
    kg = int(input("kg:"))
    print("g:",kg*1000)

def g_to_kg():
    g = int(input("kg:"))
    print("g:",g/1000)

def unit_conversion():
    while True:
        print('\n----------')
        print("[1]:cm->m")
        print("[2]:m->cm")
        print("[3]:kg->g")
        print("[4]:g->kg")
        print("[0]Quit")
        print('----------')
        menu = input('Menu:')
        print()
        if menu == '1':
            cm_to_m()
        elif menu == '2':
            m_to_cm()
        elif menu == '3':
            kg_to_g()
        elif menu == '4':
            g_to_kg()
        elif menu == '0':
            break
        else:
            print("잘못된 입력입니다. 다시선택하세요.")