showroom = set()
showroom.add("Honda Civic")
showroom.add("Kia Sorento")
showroom.add("Tesla Model X")
showroom.add("Chrysler PT Cruiser Convertable")

print(len(showroom))
showroom.add("Chrysler PT Cruiser Convertable")
print(showroom)

new_whips = {"Renault Dauphine", "DMC Delorean"}
showroom.update(new_whips)
print(showroom)
showroom.discard("DMC Delorean")
print(showroom)

junkyard = set()
junkyard.add("Chrysler PT Cruiser Convertable")
junkyard.add("Renault Dauphine")
junkyard.add("Fuller Dymaxion")
junkyard.add("Ford Pinto")

print(showroom.intersection(junkyard))
showroom.union(junkyard)
showroom.discard("Ford Pinto")