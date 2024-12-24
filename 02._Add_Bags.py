
price_luggage_over_20_kilos = float(input())
luggage_kilos = float(input())
days_to_departure = int(input())
number_luggage = int(input())
price_per_luggage = 0

if luggage_kilos < 10:
    price_per_luggage = price_luggage_over_20_kilos * 0.20
elif 10 <= luggage_kilos <= 20:
    price_per_luggage = price_luggage_over_20_kilos * 0.50
else:
    price_per_luggage = price_luggage_over_20_kilos

if days_to_departure > 30:
    price_per_luggage += price_per_luggage * 0.10
elif 7 <= days_to_departure <= 30:
    price_per_luggage += price_per_luggage * 0.15
elif days_to_departure < 7:
    price_per_luggage += price_per_luggage * 0.40

total_price = price_per_luggage * number_luggage
print(f"The total price of bags is: {total_price:.2f} lv.")
