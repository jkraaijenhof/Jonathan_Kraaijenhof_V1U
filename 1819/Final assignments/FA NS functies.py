def standaardprijs(afstandKm):
    if afstandKm < 0:
        afstandKm = 0

    if afstandKm > 50:
        prijs = 15 + 0.60 * afstandKm
    else:
        prijs = 0.80 * afstandKm
    return prijs

def ritprijs(leeftijd, weekendrit, kilometers):
    prijs = standaardprijs(kilometers)
    korting = 1

    if (leeftijd<12 or leeftijd>=65):
        korting = 0.7
        if weekendrit == 'Ja':
            korting = 0.65
    else:
        if weekendrit == 'Ja':
            korting = 0.60

    prijs = prijs * korting
    return prijs


invoerkm = int (input('Voer aantal kilometers in'))
invoerweekend = input('Is het weekend?')
leeftijd = int (input('Wat is uw leeftijd?'))
print ('U betaalt €',ritprijs(leeftijd,invoerweekend, invoerkm,))

