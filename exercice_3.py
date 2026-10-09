n=int(input("Entrer un nombre strictement positif:"))
while n<=0:
    n=int(input("Ereur,entrer un nombre positif:"))
print("\n les nombres pairs sont :")
for i in range(2,n+1,2):
    print(i)
impairs=[]
for i in range(1,n+1):
    if i %2 !=0:
        impairs.append(i)
print("\n\n la liste des nombres impairs :",impairs)
somme=0
for nombre in impairs:
    somme=somme+nombre
print("la somme des nombres impair est:",somme)
produit=1
for nombre in impairs:
    produit=produit*nombre
print("le produit des nombres impairs est:",produit)
print("\n table de multiplication du produit:")
for i in range(1,13):
    print(f"{n}*{i}={n*i}")
