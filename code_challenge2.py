#codechallenge2
print("--------------------------------------------------------")
money = int(input("Amount to deposit --"))

oneK = money // 1000
onek_tira = money % 1000

fiveh = onek_tira // 500
fiveh_tira = onek_tira % 500

threeH = fiveh_tira // 300
threeH_tira = fiveh_tira % 300

twoH = threeH_tira // 200
twoH_tira = threeH_tira % 200

oneH = twoH_tira // 100
oneH_tira = twoH_tira % 100

fifty = oneH_tira // 50
fifty_tira = oneH_tira % 50

bente = fifty_tira // 20
bente_tira = fifty_tira % 20

sampo = bente_tira // 10
sampo_tira = bente_tira % 10

lima = sampo_tira // 5  
lima_tira = sampo_tira % 5

piso = lima_tira // 1  
piso_tira = lima_tira % 1  

print("1000 -->", oneK)
print(" 500 -->", fiveh)
print(" 300-->", threeH)
print(" 200 -->", twoH)
print(" 100 -->", oneH)
print("  50 -->", fifty)
print("  20 -->", bente)
print("  10 -->", sampo)
print("   5 -->", lima)
print("   1 -->", piso)
print("--------------------------------------------------------")
