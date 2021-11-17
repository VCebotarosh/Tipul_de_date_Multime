try:
    multime=input("Dati elementele primei multimi: ")
    multimea_a=set(list(map(lambda x: int(x), multime.strip().split(" "))))
    multime=input("Dati elementele multimii a doua: ")
    multimea_b=set(list(map(lambda x: int(x), multime.strip().split(" "))))
    print(f"Intersectia celor 2 multimi este : {multimea_a.intersection(multimea_b)}")
    print(f"Reuniunea celor 2 multimi este : {multimea_a.union(multimea_b)}")
    print(f"Diferenta multimii A {multimea_a} si multimii B {multimea_b} este : {multimea_a.difference(multimea_b)}")
    print(f"Diferenta multimii B {multimea_b} si multimii A {multimea_a} este : {multimea_b.difference(multimea_a)}")
except ValueError:
    print("Datele introduse nu satisfac conditiile problemei")