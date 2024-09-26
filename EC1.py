print("Available movies today: ")
print("A)12 Strong: \t1)2:30  2)4:40  3)7:50  4)10:50")
print("B)Coco: \t1)12:40 2)3:45")
print("C)The Post: \t1)12:45 2)3:35  3)7:05  4)9:55")

movie_choice = input("Movie choice:\t")
if (movie_choice != 'A') and (movie_choice != 'B') and (movie_choice != 'C'):
    print("Invalid option; please restart app...")
else:
    showtime = (input("Showtime:\t"))
    if movie_choice == 'A' and (showtime != '1' and showtime != '2' and showtime != '3' and showtime != '4'):
        print("Invalid option; please restart app...")
    elif movie_choice == 'B' and (showtime != '1' and showtime != '2'):
        print("Invalid option; please restart app...")
    elif movie_choice == 'C' and (showtime != '1' and showtime != '2' and showtime != '3' and showtime != '4'):
        print("Invalid option; please restart app...")
    else:
        number_of_adult_tickets = int(input("Adult tickets:\t"))
        if number_of_adult_tickets > 30:
            print("Invalid option; please restart app...")
        number_of_kid_tickets = int(input("Kid tickets:\t"))
        if number_of_kid_tickets > 30:
            print("Invalid option; please restart app...")
        elif number_of_kid_tickets + number_of_adult_tickets > 30:
            print("Invalid option; please restart app...")
        else:
            if movie_choice == 'B' and showtime == '1' or movie_choice == 'C' and showtime == '1':
                total_cost = 11.17 * number_of_adult_tickets + 8 * number_of_kid_tickets
                print(f"Total cost:\t${total_cost:.2f}")
            else:
                total_cost = 12.45 * number_of_adult_tickets + 9.68 * number_of_kid_tickets
                print(f"Total cost:\t${total_cost:.2f}")