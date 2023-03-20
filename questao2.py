n = int(input("Qual número deseja checar? "))
sequencia = [0, 1]

for i in range(n+1):
    ultimo = sequencia[-1]
    penultimo = sequencia[-2]
    if n != 1:
        sequencia.append(ultimo + penultimo)
    if ultimo > n:
        break

if n in sequencia:
    print("SIM, este número está na sequência de Fibonacci")
else:
    print("NÃO, este número não está na sequência de Fibonacci")