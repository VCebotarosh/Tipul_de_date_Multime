#In aceasta versiune valorile care nu corespund cerintelor doar se omit si programul opereaza cu valorile care satisfac conditia
multime=input("Dati elementele primei multimi: ")
multime=list(multime.strip().split(" "))
multimea_a=set(multime)
multime=input("Dati elementele multimii a doua: ")
multime=list(multime.strip().split(" "))
multime_b=set(multime)
multimea_a_filter=[]
multime_b_filter=[]
for element in multimea_a:
    try:
        a=int(element)
        multimea_a_filter.append(a)
    except ValueError:
        continue
for element in multime_b:
    try:
        b=int(element)
        multime_b_filter.append(b)
    except ValueError:
        continue
multimea_a_filter=set(multimea_a_filter)
multime_b_filter=set(multime_b_filter)
print(f"Intersectia celor 2 multimi este : {multimea_a_filter.intersection(multime_b_filter)}")
print(f"Reuniunea celor 2 multimi este : {multimea_a_filter.union(multime_b_filter)}")
print(f"Diferenta multimii A {multimea_a_filter} si multimii B {multime_b_filter} este : {multimea_a_filter.difference(multime_b_filter)}")
print(f"Diferenta multimii B {multime_b_filter} si multimii A {multimea_a_filter} este : {multime_b_filter.difference(multimea_a_filter)}")
