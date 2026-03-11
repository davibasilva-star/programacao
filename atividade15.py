total = float(input("Digite o valor total da conta: R$ "))
parte = total / 3
carlos = int(parte)
andre = int(parte)
felipe = total - (carlos + andre)
print(f"Carlos deve pagar: R$ {carlos:.2f}")
print(f"André deve pagar: R$ {andre:.2f}")
print(f"Felipe deve pagar: R$ {felipe:.2f}")

