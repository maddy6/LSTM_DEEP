args = commandArgs(trailingOnly=TRUE)

#### Install below packages 
options(warn=-1)
suppressWarnings(suppressMessages(library("plyr")))
suppressWarnings(suppressMessages(library("dplyr")))
suppressWarnings(suppressMessages(library("data.table")))
suppressWarnings(suppressMessages(library("Matrix")))
suppressWarnings(suppressMessages(library("stringr")))
suppressWarnings(suppressMessages(library("syuzhet")))
suppressWarnings(suppressMessages(library("tm")))
suppressWarnings(suppressMessages(library("openNLP")))
suppressWarnings(suppressMessages(library("rvest")))
suppressWarnings(suppressMessages(library("utils")))
suppressWarnings(suppressMessages(library("quanteda")))
suppressWarnings(suppressMessages(library("qdap")))
suppressWarnings(suppressMessages(library("doSNOW")))
suppressWarnings(suppressMessages(library("doParallel")))

### Load the Input Data (Trackwise Data)
df<- data.frame( fread(args[1], stringsAsFactors = FALSE))
df$Event.Description..English.<-gsub("\r\n", " ", df$Event.Description..English.)
df$Event.Description..English.<-gsub("\n", " ", df$Event.Description..English.)
df$Event.Description..English.<-gsub("\t", "", df$Event.Description..English.)

df1 = data.frame(df$PR.ID,df$Event.Description..English.)

### Naive Bayes Model
naive_sumly <- function(text, method = "bing")
{

  agg_txt <- text
  txt_string <- as.String(agg_txt)
  word_ann <- Maxent_Word_Token_Annotator()
  sent_ann <- Maxent_Sent_Token_Annotator()
  txt_annotations <- annotate(txt_string, list(sent_ann, word_ann))
  txt_doc <- AnnotatedPlainTextDocument(agg_txt, txt_annotations)
  
  st <- sents(txt_doc)
  wt <- words(txt_doc)
  
  sens <- get_sentences(agg_txt)

  words_per_sens<-llply(st, function(x){

    temp <- x
    
    return(temp)
  })
  
  
  if (length(sens) > 1)
  {
    sim_mat <- foreach(a = words_per_sens, .combine = "cbind") %:%
      foreach(b = words_per_sens, .combine = "c") %dopar% {
        length(intersect(a, b))/((length(a) + length(b))/2)
      }
    spars_sim_mat <- Matrix(sim_mat, sparse = T)
    if(colSums(spars_sim_mat)>1){
      diag(spars_sim_mat) <- 1
      sens_sim <- colSums(spars_sim_mat)-1
      dat <- data.table(sentence = sens, total_sim = colSums(spars_sim_mat)-1)
      
      paras <- unlist(strsplit(agg_txt, split = "\r\n", fixed = T))
  
      best_sens <- rep(NA, length(paras))
      max_para_vals <- rep(NA, length(paras))
    }
    
    if(colSums(spars_sim_mat)<=1){
      sens_sim <- colSums(spars_sim_mat)
      dat <- data.table(sentence = sens, total_sim = colSums(spars_sim_mat))
      
      paras <- unlist(strsplit(agg_txt, split = "\r\n", fixed = T))
  
      best_sens <- rep(NA, length(paras))
      max_para_vals <- rep(NA, length(paras))
    }
    
    i <- 1
    for (p in paras)
    {
    
      best_sen <- NA
      max_para_val <- 0
      para_sens <- get_sentences(p)
      for (s in para_sens)
      {
        m <- dat[grepl(s, sentence, fixed = TRUE),]$total_sim
        if (m > max_para_val)
        {
          max_para_val <- m
          best_sen <- as.character(s)
        }
        else
        {
          max_para_val <- max_para_val
          best_sen <- best_sen
        }
      }
      best_sens[i] <- best_sen
      max_para_vals[i] <- max_para_val
      i <- i + 1
   
    }
    best_sens <- best_sens[which(max_para_vals != 0)]
    max_para_vals <- max_para_vals[which(max_para_vals != 0)]
   
    return(list(summary = best_sens, max_sim_values = max_para_vals))
  }
  else
  {
    return(text)
  }
}

event_data = list()

for(i in 1:dim(df1)){

  event<- df1$df.Event.Description..English.[i]
  event<-gsub("[][!#?$%*Ã¢ÂÂ¬Ã¢ÂÂ¢()+<>@ÃÂ´^_`|~{}]", "", event)

  event<-gsub("\\(GMT\\)", "",event)
  event<-gsub("GMT", "",event)

  event<-gsub("\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}", "",event)
  event<-gsub("\\w+ \\w+ :", "",event)
  event<-gsub("(Y/N)", "",event)
  event<-gsub('[[:digit:]]+', '', event)
  event<-gsub("PM.* PID", "",event)
  event<-gsub("[][//-:]","",event)
  event_data[[i]]<-str_squish(event)
  
}

event_data = unlist(event_data)

event_data1 = list()

for(i in 1:length(event_data)){
 
  if(nchar(event_data[i])>0){
    event_data1[[i]] = event_data[i]
  }else{
    event_data1[[i]] = "No Sufficient data available"
  }
}

event_data1 = unlist(event_data1)


event_summary = list()
for(i in 1:length(event_data1)){
 
  trunc_article <- naive_sumly(text = event_data1[i])
  if(length(trunc_article)==1){
    event_summary[[i]] = trunc_article
  }else{
    event_summary[[i]] = trunc_article$summary
    
  }
}

event_summary = unlist(event_summary)


###### Material Number Mapping #####################

df2<- data.frame( fread(args[2], stringsAsFactors = FALSE))

material_no1 = list()

for(i in 1:length(df[,1])){

  if(df$PR.ID[i] %in% df2[,1] ==T){
    
    material_no1[[i]]<-df2[which(df$PR.ID[i]==df2[1]),5]
    
  }else{
    material_no1[[i]] = "NA" 
  }
  
}   

Short_Summary_by_AI_Model = paste(material_no1,event_summary)

final_df = data.frame(df,Short_Summary_by_AI_Model)

write.csv(final_df,args[3])


