
company_name = input()
number_tickets_for_adults = int(input())
number_tickets_for_kids = int(input())
ticket_price_for_adult = float(input())
tax_price = float(input())

ticket_price_for_kids = ticket_price_for_adult - (ticket_price_for_adult * 70) / 100
total_price_for_adult = ticket_price_for_adult + tax_price
total_price_for_kids = ticket_price_for_kids + tax_price
total_price_for_all_tickets = (total_price_for_kids * number_tickets_for_kids) + (total_price_for_adult * number_tickets_for_adults )
profit_from_tickets = total_price_for_all_tickets * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit_from_tickets:.2f} lv.")
