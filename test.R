### Index Fund V1.0


setwd("E:/Users/mayur.v/Documents/Index_Method/Data/")
data1<-read.csv("Bitcoin.csv")
data2<-read.csv("Dash.csv")
data3<-read.csv("Ethereum.csv")
data4<-read.csv("Litecoin.csv")
data5<-read.csv("Monero.csv")
data6<-read.csv("Dogecoin.csv")
data7<-read.csv("NEM.csv")
data8<-read.csv("Dcr.csv")
data9<-read.csv("Ethereum_classic.csv")

dim(data9)

data_final<-data.frame(data1$Date,data1$Marketcap.USD.,data2$Marketcap.USD.,data3$Marketcap.USD.,
                 data4$Marketcap.USD.,data5$Marketcap.USD.,data6$Marketcap.USD.,
                 data7$Marketcap.USD.,data8$Marketcap.USD.,data9$Marketcap.USD.)
dim(data_final)
#View(data_Final)

colnames(data_final)<-c("Date","Bitcoin", "Dash", "Ethereum", "Litecoin",
                  "Monero", "Dogecoin", "NEM", "Dcr", "Ethereum_classic")



###### Sum of market capitalization by date
Final_df4<-data.frame()
#Final_df5<-data.frame()
for(i in 1:423){
  print(i)
  Final_df4<-rbind(Final_df4, sum(data_final$Bitcoin[i]+ data_final$Dash[i] +
                 data_final$Ethereum[i] + data_final$Litecoin[i] + 
                 data_final$Monero[i] + data_final$Dogecoin[i] +
                 data_final$NEM[i] + data_final$Dcr[i] +
                 data_final$Ethereum_classic[i]))
  #Final_df4
  
}
colnames(Final_df4)<-c("Sum_market_capitalization")


####### Divisor
Final_df1<- data.frame(Final_df4, Final_df4$Sum_market_capitalization/1000)
colnames(Final_df1)<-c("Sum_market_capitalization","Divisor")

head(Final_df1)
data_final<-data.frame(data_final,Final_df1)
head(data_final)
##################

Final_df5<-data.frame()
for(i in 1:423){
    print(i)
    Final_df6<- data.frame(data_final$Sum_market_capitalization[i]/data_final$Divisor[i+1])
    Final_df5<-rbind(Final_df5,Final_df6)
  
}


######################
