




#Final_df <- within(data_final, Sum_market_capitalization <- cumsum(Bitcoin + Dash + Ethereum + Litecoin+
#                                           Monero+Dogecoin+NEM+Dcr+Ethereum_classic))

#View(Final_df)

###### Calculate the Divisor                                                                                        

Final_df1<- data.frame(Final_df,Final_df$Sum_market_capitalization/1000)

##### Calculate the Index

colnames(Final_df1)<-c("Date","Bitcoin", "Dash", "Ethereum", "Litecoin",
                       "Monero", "Dogecoin", "NEM", "Dcr", "Ethereum_classic",
                       "Sum_market_capitalization","Divisor")
#View(Final_df1)
###################


Final_df3<-data.frame()
for(i in Final_df1$Sum_market_capitalization){
  for(j in Final_df1$Divisor){
    Final_df3<- data.frame(Final_df1,Final_df1$Sum_market_capitalization[i]/Final_df1$Divisor[j+1])
    Final_df3<-rbind(Final_df3,Final_df1)
  }
}


i=1
j=1
Final_df1$Sum_market_capitalization[i]
Final_df1$Divisor[j+1]
View(Final_df2)
