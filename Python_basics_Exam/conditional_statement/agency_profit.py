company_name = input()
adult_tickets_count = int(input())
child_tickets_count = int(input())
ticket_price_adult = float(input())
service_fee = float(input())

total_price_adult_tickets = adult_tickets_count * (ticket_price_adult + service_fee)
child_ticket = (ticket_price_adult * 0.3) + service_fee

total_price_child_ticket = child_ticket * child_tickets_count
total_sum = total_price_child_ticket + total_price_adult_tickets
agency_profit = total_sum * 0.2

print(f'The profit of your agency from {company_name} tickets is {agency_profit} lv')
