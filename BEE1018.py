val = input()
val = int(val)
print(val)
moneyList = (100,50,20,10,5,2,1)
finaList = []
for i in range(len(moneyList)):
    if val/moneyList[i] >= 1:
        billete = int(val/moneyList[i])
        finaList.append(f"{billete} nota(s) de R$ {moneyList[i]},00")
        val = val - (billete * moneyList[i])
    else:
        finaList.append(f"0 nota(s) de R$ {moneyList[i]},00")


for i in range(len(finaList)):
    print(finaList[i])