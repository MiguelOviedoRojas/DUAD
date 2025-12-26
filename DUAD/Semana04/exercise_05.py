#5. Dada `n` cantidad de notas de un estudiante, calcular:
   # 1. Cuantas notas tiene aprobadas (mayor a 70).
   # 2. Cuantas notas tiene desaprobadas (menor a 70).
   # 3. El promedio de todas.
   # 4. El promedio de las aprobadas.
   # 5. El promedio de las desaprobadas.


approved_notes = 0
failing_grades = 0
prom_total = 0
prom_approved = 0
prom_failing = 0
counter = 1

total_amount = int(input("Enter your total amount of notes: "))
while(counter <= total_amount):
    actual_note = int(input(f"Enter note {counter}: "))
    if(actual_note >= 70):
        approved_notes = approved_notes + 1
        prom_total = prom_total + actual_note
        prom_approved = prom_approved + actual_note
        counter = counter + 1
    else:
        failing_grades = failing_grades + 1
        prom_total = prom_total + actual_note
        prom_failing = prom_failing + actual_note
        counter = counter + 1

print(f"The number of Approved Notes is: {approved_notes}")
print(f"The number of Failing Grades is: {failing_grades}")

prom_total = prom_total / total_amount
print(f"The Total Average is: {prom_total}")

if(approved_notes <= 0):
    print(f"The Average number of Passes is: {approved_notes}")
else:
    prom_approved = prom_approved / approved_notes
    print(f"The Average number of Passes is: {prom_approved}")

if(prom_failing <= 0):
    print(f"The Average number of Failures is: {failing_grades}")
else: 
    prom_failing = prom_failing / failing_grades
    print(f"The Average number of Failures is: {prom_failing}")








