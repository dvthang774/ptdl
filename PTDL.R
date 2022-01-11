library(dplyr)
library(tidyverse)
library(ggplot2)
library(plotly)

getwd()
data2<-read.csv('times_series2.csv')

# Multiple line plot
# Basic line plot
ggplot(data = data2, aes(x = X, y = ip13, group=1))+ 
      geom_line(color = "#00AFBB", size = 1) +
      geom_line(aes(x = X, y = promax, group=1),color="black")+
      geom_line(aes(x = X, y = pr13, group=1),color="green")+
      xlab("Date of data")  + ylab("Count")


feed<- data.frame(
  total    = c(307,194,806),
  feedback = c(100,48,193))
rownames(feed)<-c('13','13pro','13promax')
#plot1
ggplot(feed,aes(x = product,y = total))+
  geom_bar(stat="identity", width=0.5, color="blue",fill = "#FF6666")+
  ggtitle("Line up total sell")+
  xlab("Product")+ylab("Count")
#plot2
ggplot(feed,aes(x = product,y = feedback))+
  geom_bar(stat="identity", width=0.5, color="blue",fill = "#FF6656")+
  ggtitle("Line up total feedback")+
  xlab("Product")+ylab("Count")


chisq.test(feed)

rating<-data.frame(
  Percent = c(1.7,0.2,0.8,1.7,95),
  Rate=c('1','2','3','4','5')
)

ggplot(rating, aes(x = Rate, y = Percent))+ 
    geom_bar(color = "#00AFBB", size = 1) +
    xlab("Rate")+ylab("Percent")