print("~ Made by Pranjal Kumar")
print("THIS IS A APPROXIMATION & REFUNDABLE CHARGES ARE NOT INCLUDED (GROUP B COURSES ONLY)")
print("Choose number to select.")
cat1_fees = 198000
cat2_fees = 307000
cat3_fees = 405000
cat4_fees = 448000
cat5_fees = 493000


def fees_calculator_vellore(admission, cat, room_mess):
    print(f"Your Approximate fees for 4 yrs will be : ₹{admission + (cat + room_mess) * 4}")
    print("ALL THE BEST!")


def fees_calculator_chennai_bhopal_ap(admission, cat, room, mess):
    print()
    print(f"Your Approximate fees for 4 yrs will be : ₹{admission + (cat + room + mess) * 4}")
    print("ALL THE BEST!")


while True:
    college = int(input('''
1. VIT VELLORE
2. VIT CHENNAI
3. VIT BHOPAL
4. VIT AP
>>> '''))
    print()
    if college == 1:
        admission_fees = 15000
        print("DLX rooms & SPECIAL MESS are not included (Check PDF) : "
              "https://vit.ac.in/files/MH-FEE-structure-Indian-Category-2024-25"
              ".pdf")
        roomsize_vellore = int(input('''ROOM SIZE: 
1. Single Bedded
2. Double Bedded
3. Triple Bedded
4. Four Bedded
5. Six Bedded
 >>> '''))
        print()
        if roomsize_vellore == 1:
            ac_NONac = int(input('''
1. AC
2. NON AC
>>> '''))
            print()
            if ac_NONac == 1:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 186100
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 194800
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

            elif ac_NONac == 2:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 138600
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 147300
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

                if roomsize_vellore == 1:
                    ac_NONac = int(input('''
        1. AC
        2. NON AC
        >>> '''))
                    print()
                    if ac_NONac == 1:
                        mess_vellore = int(input(''' Mess:
        1. VEG
        2. NON VEG
        >>> '''))
                        print()
                        if mess_vellore == 1:
                            mess_room_fees_vellore = 186100
                            cat_selection = int(input('''CATEGORY:
        1. CATEGORY 1
        2. CATEGORY 2
        3. CATEGORY 3
        4. CATEGORY 4
        5. CATEGORY 5
        >>> '''))
                            print()
                            if cat_selection == 1:
                                fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                            elif cat_selection == 2:
                                fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                            elif cat_selection == 3:
                                fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                            elif cat_selection == 4:
                                fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                            elif cat_selection == 5:
                                fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                        elif mess_vellore == 2:
                            mess_room_fees_vellore = 194800
                            cat_selection = int(input('''CATEGORY:
        1. CATEGORY 1
        2. CATEGORY 2
        3. CATEGORY 3
        4. CATEGORY 4
        5. CATEGORY 5
        >>> '''))
                            print()
                            if cat_selection == 1:
                                fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                            elif cat_selection == 2:
                                fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                            elif cat_selection == 3:
                                fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                            elif cat_selection == 4:
                                fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                            elif cat_selection == 5:
                                fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

                    elif ac_NONac == 2:
                        mess_vellore = int(input(''' Mess:
        1. VEG
        2. NON VEG
        >>> '''))
                        print()
                        if mess_vellore == 1:
                            mess_room_fees_vellore = 138600
                            cat_selection = int(input('''CATEGORY:
        1. CATEGORY 1
        2. CATEGORY 2
        3. CATEGORY 3
        4. CATEGORY 4
        5. CATEGORY 5
        >>> '''))
                            print()
                            if cat_selection == 1:
                                fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                            elif cat_selection == 2:
                                fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                            elif cat_selection == 3:
                                fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                            elif cat_selection == 4:
                                fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                            elif cat_selection == 5:
                                fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                        elif mess_vellore == 2:
                            mess_room_fees_vellore = 147300
                            cat_selection = int(input('''CATEGORY:
        1. CATEGORY 1
        2. CATEGORY 2
        3. CATEGORY 3
        4. CATEGORY 4
        5. CATEGORY 5
        >>> '''))
                            print()
                            if cat_selection == 1:
                                fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                            elif cat_selection == 2:
                                fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                            elif cat_selection == 3:
                                fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                            elif cat_selection == 4:
                                fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                            elif cat_selection == 5:
                                fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

        elif roomsize_vellore == 2:
            ac_NONac = int(input('''
1. AC
2. NON AC
>>> '''))
            print()
            if ac_NONac == 1:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 153800
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 162500
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

            elif ac_NONac == 2:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 121500
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 130200
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

        elif roomsize_vellore == 3:
            ac_NONac = int(input('''
1. AC
2. NON AC
>>> '''))
            print()
            if ac_NONac == 1:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 147300
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 156000
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

            elif ac_NONac == 2:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 114800
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 123500
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

        elif roomsize_vellore == 4:
            ac_NONac = int(input('''
1. AC
2. NON AC
>>> '''))
            print()
            if ac_NONac == 1:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 135000
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 143700
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

            elif ac_NONac == 2:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 108500
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 117200
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

        elif roomsize_vellore == 5:
            ac_NONac = int(input('''
1. AC
2. NON AC
>>> '''))
            print()
            if ac_NONac == 1:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 126900
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 135600
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

            elif ac_NONac == 2:
                mess_vellore = int(input(''' Mess:
1. VEG
2. NON VEG
>>> '''))
                print()
                if mess_vellore == 1:
                    mess_room_fees_vellore = 103700
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)
                elif mess_vellore == 2:
                    mess_room_fees_vellore = 112400
                    cat_selection = int(input('''CATEGORY:
1. CATEGORY 1
2. CATEGORY 2
3. CATEGORY 3
4. CATEGORY 4
5. CATEGORY 5
>>> '''))
                    print()
                    if cat_selection == 1:
                        fees_calculator_vellore(admission_fees, cat1_fees, mess_room_fees_vellore)
                    elif cat_selection == 2:
                        fees_calculator_vellore(admission_fees, cat2_fees, mess_room_fees_vellore)
                    elif cat_selection == 3:
                        fees_calculator_vellore(admission_fees, cat3_fees, mess_room_fees_vellore)
                    elif cat_selection == 4:
                        fees_calculator_vellore(admission_fees, cat4_fees, mess_room_fees_vellore)
                    elif cat_selection == 5:
                        fees_calculator_vellore(admission_fees, cat5_fees, mess_room_fees_vellore)

    elif college == 2:
        admission_fees = 15000
        mess_chennai = int(input('''MESS:
1. VEG
2. NON VEG
3. SPECIAL 
4. FOOD PARK
>>> '''))
        mess_chennai_list = [78800, 87900, 97700, 101200]
        mess_chennai_charge = mess_chennai_list[mess_chennai - 1]
        print()
        roomsize_chennai = int(input('''ROOM:
1. DOUBLE BEDDED (Only AC)
2. TRIPLE BEDDED
3. 4 BEDDED
4. 6 BEDDED (Only AC)
>>> '''))
        print()
        if roomsize_chennai == 1:
            room_charge_chennai = 124200
            cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
            if cat_selection == 1:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 2:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 3:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 4:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 5:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai, mess_chennai_charge)

        elif roomsize_chennai == 2:
            ac_NONac = int(input('''1. AC
2. NON-AC
>>> '''))
            print()
            if ac_NONac == 1:
                room_charge_chennai = 115200
                cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai,
                                                      mess_chennai_charge)

            elif ac_NONac == 2:
                room_charge_chennai = 64200
                cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai,
                                                      mess_chennai_charge)

        elif roomsize_chennai == 3:
            ac_NONac = int(input('''1. AC
2. NON-AC
>>> '''))
            print()
            if ac_NONac == 1:
                room_charge_chennai = 107400
                cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai,
                                                      mess_chennai_charge)

            elif ac_NONac == 2:
                room_charge_chennai = 58700
                cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai,
                                                      mess_chennai_charge)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai,
                                                      mess_chennai_charge)

        elif roomsize_chennai == 4:
            room_charge_chennai = 94000
            cat_selection = int(input('''CATEGORY:
1. Category 1
2. Category 2
3. Category 3
4. Category 4
5. Category 5
>>> '''))
            if cat_selection == 1:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 2:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 3:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 4:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_chennai, mess_chennai_charge)
            if cat_selection == 5:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_chennai, mess_chennai_charge)

        print()

    elif college == 3:
        admission_fees = 15000
        mess_bhopal = 74500
        print('This does not include hostel options for Block 1 (Old hostel) & a bit cheaper.')
        roomsize_bhopal = int(input('''ROOM:
    1. DOUBLE BEDDED
    2. TRIPLE BEDDED
    3. 4 BEDDED (Bunker)
    4. 4 BEDDED (Flat)
    5. 6 BEDDED (NON AC)
    >>> '''))
        if roomsize_bhopal == 1:
            ac_NONac = int(input('''
    1. AC
    2. NON-AC
    >>> '''))
            print()
            if ac_NONac == 1:
                room_charge_bhopal = 118290
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

            if ac_NONac == 2:
                room_charge_bhopal = 90830
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

        if roomsize_bhopal == 2:
            ac_NONac = int(input('''
    1. AC
    2. NON-AC
    >>> '''))
            print()
            if ac_NONac == 1:
                room_charge_bhopal = 101770
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

            if ac_NONac == 2:
                room_charge_bhopal = 74240
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

        if roomsize_bhopal == 3:
            ac_NONac = int(input('''
    1. AC
    2. NON-AC
    >>> '''))
            print()
            if ac_NONac == 1:
                room_charge_bhopal = 85000
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

            if ac_NONac == 2:
                room_charge_bhopal = 51490
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

        if roomsize_bhopal == 4:
            ac_NONac = int(input('''
    1. AC
    2. NON-AC
    >>> '''))
            print()
            if ac_NONac == 1:
                room_charge_bhopal = 88000
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

            if ac_NONac == 2:
                room_charge_bhopal = 54490
                cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
                if cat_selection == 1:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 2:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 3:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 4:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
                if cat_selection == 5:
                    fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

        if roomsize_bhopal == 5:
            print("ONLY NON AC AVAILABLE!")
            print()
            room_charge_bhopal = 39260
            cat_selection = int(input('''CATEGORY:
    1. Category 1
    2. Category 2
    3. Category 3
    4. Category 4
    5. Category 5
    >>> '''))
            if cat_selection == 1:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat1_fees, room_charge_bhopal, mess_bhopal)
            if cat_selection == 2:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat2_fees, room_charge_bhopal, mess_bhopal)
            if cat_selection == 3:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat3_fees, room_charge_bhopal, mess_bhopal)
            if cat_selection == 4:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat4_fees, room_charge_bhopal, mess_bhopal)
            if cat_selection == 5:
                fees_calculator_chennai_bhopal_ap(admission_fees, cat5_fees, room_charge_bhopal, mess_bhopal)

    elif college == 4:
        print("*******************")
