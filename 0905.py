2) 

teksts = input("Pirmais spēlētājs, lūdzu, ievadi tekstu: ")
slēptais_teksts = ''.join('*' if burts.isalpha() else burts for burts in teksts)
print("Slēptais teksts:", slēptais_teksts)
ievadīts_burts = input("Pirmais spēlētājs, lūdzu, ievadi burtu: ").lower()
atjaunotais_teksts = ''.join(burts if burts.lower() == ievadīts_burts else slēp for burts, slēp in zip(teksts, slēptais_teksts))
print("Atjaunotais teksts:", atjaunotais_teksts)


1)
vards = input("Ievadiet vārdu: ")
apgriezts = vards[::-1]
apgriezts_ar_lielu_burtu = apgriezts.capitalize()
pirmais_burts = vards[0].capitalize()
teksts = "pamatīgs juceklis" if pirmais_burts != vards[0] else "ne"
print(f"{apgriezts_ar_lielu_burtu}, {teksts} {pirmais_burts}")
