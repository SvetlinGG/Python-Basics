
period = int(input())
doctors_count = 7
day_treated_patients = 0
day_untreated_patients = 0
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    patients_count = int(input())

    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors_count += 1

    if patients_count >= doctors_count:
        day_untreated_patients = patients_count - doctors_count
        day_treated_patients = patients_count - day_untreated_patients
        untreated_patients += day_untreated_patients

    else:
        day_treated_patients = patients_count


    treated_patients += day_treated_patients


print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')




