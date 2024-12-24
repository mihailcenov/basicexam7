number_joinery = int(input())
type_joinery = input() # – текст "90X130" или "100X150" или "130X180" или "200X300";
method_of_receiving = input()  # С доставка - "With delivery", Без доставка - "Without delivery"
price = 0.0
receiving_cost = 60

if number_joinery < 10:
    print(f"Invalid order")
else:
    if type_joinery == "90X130":
        price = 110
        if number_joinery > 60:
            price -= (price * 8) / 100
        elif number_joinery > 30:
            price -= (price * 5) / 100
    elif type_joinery == "100X150":
        price = 140.0
        if number_joinery > 80:
            price -= (price * 10) / 100
        elif number_joinery > 40:
            price -= (price * 6) / 100
    elif type_joinery == "130X180":
        price = 190.0
        if number_joinery > 50:
            price -= (price * 12) / 100
        elif number_joinery > 20:
            price -= (price * 7) / 100
    elif type_joinery == "200X300":
        price = 250.0
        if number_joinery > 50:
            price -= (price * 14) / 100
        elif number_joinery > 25:
            price -= (price * 9) / 100

    total_price = price * number_joinery

    if method_of_receiving == "With delivery":
        total_price += receiving_cost
    if number_joinery > 99:
        total_price -= total_price * 0.04


    print(f"{total_price:.2f} BGN")

#proba


