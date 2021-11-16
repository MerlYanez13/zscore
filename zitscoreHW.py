import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd 
import csv 
import random
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0, counter):
        index=random.randint(0,len(data)-1)
        val=data[index]
        dataset.append(val)
    mean=statistics.mean(dataset)
    return mean 
def showfig(meanlist):
    mean=statistics.mean(meanlist)
    sd=statistics.stdev(meanlist)
    sd1start,sd1end=mean-sd, mean+sd
    sd2start,sd2end=mean-(2*sd), mean+(2*sd)
    sd3start,sd3end=mean-(3*sd), mean+(3*sd)        
    fig=ff.create_distplot([meanlist],["meanlist"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.15],mode="lines",name="mean"))
    fig.show()

def main():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)
    #showfig(meanlist)
    mean=statistics.mean(meanlist)
    print("sampling mean: ",mean)
    sd=statistics.stdev(meanlist)
    print("sampling deviation: ", sd)
    return mean, sd
mean, sd=main()
populationmean=statistics.mean(data)
print("population mean: ", populationmean)
populationsd=statistics.stdev(data)
print("population deviation: ", populationsd)
zscore=(mean-populationmean)/populationsd
print(zscore)
sd1start,sd1end=populationmean-populationsd, populationmean+populationsd
sd2start,sd2end=populationmean-(2*populationsd), populationmean+(2*populationsd)
sd3start,sd3end=populationmean-(3*populationsd), populationmean+(3*populationsd)
fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x=[populationmean,populationmean],y=[0,0.02],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.02],mode="lines",name="sd1start"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.02],mode="lines",name="sd1end"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.02],mode="lines",name="sd2start"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.02],mode="lines",name="sd2end"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.02],mode="lines",name="sd3start"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.02],mode="lines",name="sd3end"))
#fig.show()