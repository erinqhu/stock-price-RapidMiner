import csv
import matplotlib.pyplot as plt; plt.rcdefaults()

f = open("Fundamentals_clean_merged_Q1 V2.csv")
rows = csv.reader(f)

next(rows)

class Fundamental:
    EPS = 0
    afterTaxROE = 0
    outstanding = 0
    incomeCS = 0
    sector = ""
    year = 0

data = []
for row in rows:
    d = Fundamental()
    d.EPS = int(row[1])
    d.year = float(row[2])
    d.afterTaxROE = float(row[3])
    d.incomeCS = float(row[8])
    d.outstanding = float(row[16])
    d.sector = row[17]
    
    data.append(d)

l1 = filter(lambda x: x.outstanding > 13836078.431, data)
l2 = filter(lambda x: x.incomeCS > 150710500, l1)
l3 = list(filter(lambda x: x.afterTaxROE > 6.5, l2))

class Sector:
    Name = ""
    num = 0

sectors = map(lambda x: x.sector, data)
sectors = set(list(sectors))

qSectors =[]
for sector in sectors:
    l4 = list(filter(lambda x: x.sector == sector, l3))
    
    s = Sector()
    s.Name = sector
    s.num = len(l4)
    
    qSectors.append(s)

qSectors = sorted(qSectors, key = lambda x: x.num, reverse = True)

sumNum = sum(list(map(lambda x: x.num, qSectors)))
gdata = []
labels = list(map(lambda x: x.Name, qSectors))
for i in range(len(qSectors)):
    gdata.append(qSectors[i].num / sumNum * 100)
    print("Top " + str(i+1) + " performing industry: " + qSectors[i].Name + " " + str(qSectors[i].num / sumNum * 100) + "%")
"""
plt.bar(range(len(gdata)), gdata, align='center', alpha=0.5)
plt.xticks(range(len(gdata)), labels, rotation = 90)
plt.ylabel('Percentage (%)')
plt.title('Top-Performing Industries')
plt.show()
"""

for sector in qSectors:
    lst = list(filter(lambda x: x.sector == sector, data))
    lst2 = list(filter(lambda x: x.year == "2016", lst))
    print(sector + " " + str(len(lst2)))









