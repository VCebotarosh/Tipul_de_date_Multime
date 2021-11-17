multime=input("Dati elementele primei multimi: ")
multime=list(multime.strip().split(" "))
multimea_a=set(multime)
multime=input("Dati elementele multimii a doua: ")
multime=list(multime.strip().split(" "))
multime_b=set(multime)
if all(element.isdigit() for element in multimea_a) and all (element.isdigit()for element in multime_b):
        print(f"Intersectia celor 2 multimi este : {multimea_a.intersection(multime_b)}")
        print(f"Reuniunea celor 2 multimi este : {multimea_a.union(multime_b)}")
        print(f"Diferenta multimii A {multimea_a} si multimii B {multime_b} este : {multimea_a.difference(multime_b)}")
        print(f"Diferenta multimii B {multime_b} si multimii A {multimea_a} este : {multime_b.difference(multimea_a)}")
else:
    print(f"Ceea ce ati introdus nu satisface conditiile problemei")



