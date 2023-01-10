lapinsAdultes = 0
lapinsEnfants = 2

mois = int(input("Combien de mois ? "))
for i in range(mois):
    enfants = lapinsAdultes
    lapinsAdultes += lapinsEnfants
    lapinsEnfants = enfants

print("Il y aura ", lapinsAdultes, " lapins adultes et ", lapinsEnfants, " lapins enfants au bout de ", mois, " mois. ")