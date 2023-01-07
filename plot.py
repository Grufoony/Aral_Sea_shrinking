import matplotlib.pyplot as plt

years = [1977,1987,1998,2006,2010,2013,2014,2015,2019,2021]
areas = [1,0.808214600448317,0.581066614619375,0.304787167976721,0.264261253748292,0.271470986591908,0.155804751681187,0.211492396955233,0.168222170963525,0.159078408062599]

plt.plot(years, areas)
plt.plot(years, areas, 'bo')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Years", fontsize=15)
plt.ylabel("Normalize surface area", fontsize=15)
plt.show()
