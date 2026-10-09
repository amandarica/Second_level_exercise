n=int(input("Combien de chauffeurs voulez vous saisir:"))
chauffeurs=[]
for i in range(n):
    nom=input("Entrer le nom du chauffeur:")
    chauffeurs.append(nom)
distances=[]
for i in range(n):
    distance=float(input("Entrer la distancce en km:"))
    distances.append(distance)
distance_min=distances[0]
Position=0
for i in range(1,n):
    if distances[i]<distance_min:
        distance_min=distances[i]
        Position=i
print("le chauffeur le plus proche est:",chauffeurs[Position])
print("Sa distance est :",distances[Position],"km")
print("Sa position dans la liste est :",Position)