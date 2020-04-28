
f = open("date.txt", 'r')
nr=int(f.readline())  #nr de tranzitii
nr1=int(f.readline()) #nr de stari
start=int(f.readline()) #starea initiala
end=list() #lista cu starile finale
x=f.readline()
x=x.split()
for e in x:
    end.append(int(e)) #crearea unei liste cu starile finale
dfa={}
for i in range(0, nr):
    x = f.readline()
    x = x.split()
    if int(x[0]) in dfa:
        dfa[int(x[0])][x[2]] = int(x[1])
    else:
        dfa[int(x[0])] = {}
        dfa[int(x[0])][x[2]] = int(x[1])
print(dfa)
r = dict(dfa)
print('\n')
for i in range(0, nr1-1):
    for j in range (i+1, nr1):
        if i not in end and j not in end or i in end and j in end:
            if (dfa[i].items() == dfa[j].items()):
                print("Starile", i, "si", j, "sunt echivalente, deci putem sterge una dintre ele", '\n')
                del r[j]
print(r, '\n')