
# package_kg = float(input())
# service_type = input()
# distance_km = int(input())
#
# delivery_price = 0
#
# if service_type == 'standard':
#     if package_kg < 1:
#         delivery_price = distance_km  * 0.03
#
#         if service_type == 'express':
#             if package_kg < 1:
#                 delivery_price *= 0.8
#     elif package_kg == 1 or package_kg < 10:
#         delivery_price = distance_km * 0.05
#
#         if service_type == 'express':
#             if package_kg == 1 or package_kg < 10:
#                 delivery_price *= 0.4
#     elif package_kg == 10 or package_kg < 40:
#         delivery_price = distance_km * 0.1
#
#         if service_type == 'express':
#             if package_kg == 10 or package_kg < 40:
#                 delivery_price *= 0.05
#     elif package_kg == 40 or package_kg < 90:
#         delivery_price = distance_km * 0.15
#
# if service_type == 'express':
#     if package_kg == 40 or package_kg < 90:
#                delivery_price *= 0.02
#     elif package_kg == 90 or package_kg < 150:
#         delivery_price = distance_km * 0.2
#
#         if service_type == 'express':
#             if package_kg == 90 or package_kg < 150:
#                 delivery_price *= 0.01
#
# print(f'The delivery of your shipment with weight of {package_kg:.3f} kg. would cost {delivery_price:.2f} lv.')

packages_kg = float(input())
service_type = input()
distance_km = int(input())

price = 0
additional_for_the_serves = 0
if 1 > packages_kg:
    price = 3
elif 10 > packages_kg:
    price = 5
elif 40 > packages_kg:
    price = 10
elif 90 > packages_kg:
    price = 15
elif 150 > packages_kg:
    price = 20

if service_type == "express":
    if 1 > packages_kg:
        additional_for_the_serves = price * 0.80
    elif 10 > packages_kg:
        additional_for_the_serves = price * 0.40
    elif 40 > packages_kg:
        additional_for_the_serves = price * 0.05
    elif 90 > packages_kg:
        additional_for_the_serves = price * 0.02
    elif 150 > packages_kg:
        additional_for_the_serves = price * 0.01
    additional_for_the_serves = (packages_kg * (additional_for_the_serves / 100)) * distance_km


total = additional_for_the_serves + (distance_km * price) / 100

print(f"The delivery of your shipment with weight of {packages_kg:.3f} kg. would cost {total:.2f} lv.")