import pandas as pd
import matplotlib.pyplot as plt
pop_df = pd.read_csv("populationByCountry.csv",usecols=['country','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
master_df = pd.read_csv("master.csv",usecols=["country","year","suicides_no"])
#master_df
master_df = master_df.loc[(master_df.country =='Canada')&(master_df.year >= 1985)&(master_df.year <=2010)]
# print(master_df)

master_df = master_df.groupby(['year']).sum()
# master_df
pop_df = pop_df[pop_df.country=='Canada']

years = pop_df.keys().tolist()
years.pop(0)
canada_pop = []
suicides_no = []
for item in pop_df:
    canada_pop.append(pop_df[item].values[0])


for item in master_df["suicides_no"]:
    suicides_no.append(item)

canada_pop.pop(0)
result  = pd.DataFrame({"year":years,"population":canada_pop,"suicides_no":suicides_no})
print(result)

resultFile = open("canadaSuicidesNoCorrelatingWithPopulation.csv","w")
index = 0
resultFile.write("year,population,suicides_no\n")
while index<len(result["year"]):
    resultFile.write(str(result["year"][index])+","+str(result["population"][index])+","+str(result["suicides_no"][index])+"\n")
    index+=1


# plt.rcParams.update({'font.size': 18})
# # draw chart
# plt.plot(result["year"],result["population"], label = "population")
# plt.plot(result["year"],result["suicides_no"], label = "suicides No")
#

fig, ax = plt.subplots()
# plot each data-point
for i in range(len(result['suicides_no'])):
    ax.scatter(result['suicides_no'][i], result['year'][i])
    #ax.scatter(result['population'][i], result['year'][i])

# set a title and labels
ax.set_title('Canada population and suicide 1985-2010 ')
ax.set_xlabel('Suicide Num')
ax.set_ylabel('Year')

plt.rcParams.update({'font.size': 10 })
#plt.savefig("correlation.png")
#plt.legend()

plt.show()