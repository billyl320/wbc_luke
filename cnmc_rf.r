rm(list=ls())


library(xtable) #for table creation for latex
library(e1071)#for svm
library(caret)#for more info on training rf
library(randomForest)#for more info on training rf

#reporting session info
sessionInfo()


#shape metrics
da_a1 = read.table('al1_SHAPES.txt', sep=',', header=TRUE)
da_a2 = read.table('al2_SHAPES.txt', sep=',', header=TRUE)
da_h = read.table('hem_SHAPES.txt', sep=',', header=TRUE)

data = rbind(da_a1, da_a2, da_h)

#eis
ei_a1 = read.table('al1.txt', sep=',', header=TRUE)
ei_a2 = read.table('al2.txt', sep=',', header=TRUE)
ei_h = read.table('hem.txt', sep=',', header=TRUE)

ei_a<-rbind(ei_a1, ei_a2)
ei = rbind(ei_a1, ei_a2, ei_h)
#obtaining sp values
sp<-ei[,1]/(ei[,1]+ei[,2])

#color
color_a1 = read.table('al1_COLORS.txt', sep=',', header=TRUE)
color_a2 = read.table('al2_COLORS.txt', sep=',', header=TRUE)
color_h = read.table('hem_COLORS.txt', sep=',', header=TRUE)

color = rbind(color_a1, color_a2, color_h)

#texture
texture_a1 = read.table('al1_TEXTURE.txt', sep=',', header=TRUE)
texture_a2 = read.table('al2_TEXTURE.txt', sep=',', header=TRUE)
texture_h = read.table('hem_TEXTURE.txt', sep=',', header=TRUE)

texture = rbind(texture_a1, texture_a2, texture_h)

labs2<-as.factor(c(
                  rep("all", dim(ei_a)[1]),
                  rep("hem", dim(ei_h)[1])    ) )


labs<-as.factor(c(
                  rep(1, dim(ei_a)[1]),
                  rep(0, dim(ei_h)[1])    ) )

#counts plot
temp<-as.data.frame(cbind(ei,sp, color, texture, data))

#setup for RF model

train<-as.data.frame(cbind(as.factor(labs), temp))
colnames(train)[1]<-"labs_svm"

#variables to keep
keep<-c(1:25)

#now let's tune the svm model using 5-folds on t-set and validaiton

set.seed(22773)

keep2<-which(train$labs_svm==1)
keep3<-which(train$labs_svm==0)

#80% for training and 20% for validation
obs_1 = keep2[1:floor(length(keep2)*0.80)]
obs_2 = keep3[1:floor(length(keep3)*0.80)]

obs<-c(obs_1, obs_2)

#cv setup
tc <- trainControl(method='cv',
                  number = 5,
                  search='grid')

grid <- expand.grid(mtry=c(1:10))

#perform cv random forest
tune.out<-train(as.factor(labs_svm) ~.,
          data=train[obs, keep],
          method='rf',
          importance=TRUE,
          trControl = tc,
          tuneGrid=grid)

#print results
print(tune.out)

w<-as.matrix(tune.out$finalModel$importance[,3])
w_sort<-w[order(-w[,1]), , drop = FALSE]

#max weight
w_max<-(w_sort[1])

#normalized weights relative to the max
w_norm<- w_sort / w_max

#table for Latex
#normalized
xtable(as.matrix(w_norm), digits=3)

#table for Latex
#non normalized
xtable(as.matrix(w), digits=3)

#VarImp based on feature type
vars_c<-c(4:17)
vars_t<-c(18:19)

#vImp<-matrix(nrow=1, ncol=3, data=0)
vImp<-c(0,0,0)
names(vImp)<-c("Color", "Texture", "Shape")

vImp[1]<-sum(w[vars_c])
vImp[2]<-sum(w[vars_t])
vImp[3]<-sum(w[-c(vars_t, vars_c)])

vImp_sort <- sort(vImp, decreasing = T)

xtable(t(as.matrix(vImp_sort/vImp_sort[1])), digits=3 )


varImp(tune.out$finalModel)

varImp(tune.out)

#output accuracy on training data
ypred=predict(tune.out$finalModel ,train[obs,])
table(predict=ypred, truth=train$labs_svm[obs])
mean(ypred==train$labs_svm[obs])

#confusion matrix
confusionMatrix(ypred, train$labs_svm[obs])

#setup matrix to collect scores
measures_train<-matrix(nrow=2, ncol=3, data=0 )
rownames(measures_train)<-c('0', '1')
colnames(measures_train)<-c("Precision", "Recall", "F-1 Score")

#collecting measures
precision <- posPredValue(ypred, train$labs_svm[obs], positive="0")
recall <- sensitivity(ypred, train$labs_svm[obs], positive="0")
F1 <- (2 * precision * recall) / (precision + recall)
measures_train[1,1]<-precision
measures_train[1,2]<-recall
measures_train[1,3]<-F1

precision <- posPredValue(ypred, train$labs_svm[obs], positive="1")
recall <- sensitivity(ypred, train$labs_svm[obs], positive="1")
F1 <- (2 * precision * recall) / (precision + recall)
measures_train[2,1]<-precision
measures_train[2,2]<-recall
measures_train[2,3]<-F1

xtable(measures_train)

colMeans(measures_train)

#collecting accuracy on validation data
ypred=predict(tune.out$finalModel ,train[-obs,])
table(predict=ypred, truth=train$labs_svm[-obs])
mean(ypred==train$labs_svm[-obs])

#confusion matrix for validation data
confusionMatrix(ypred, train$labs_svm[-obs])

#matrix for validation data measures
measures_valid<-matrix(nrow=2, ncol=3, data=0 )
rownames(measures_valid)<-c('0', '1')
colnames(measures_valid)<-c("Precision", "Recall", "F-1 Score")

#collecting measures
precision <- posPredValue(ypred, train$labs_svm[-obs], positive="0")
recall <- sensitivity(ypred, train$labs_svm[-obs], positive="0")
F1 <- (2 * precision * recall) / (precision + recall)
measures_valid[1,1]<-precision
measures_valid[1,2]<-recall
measures_valid[1,3]<-F1

precision <- posPredValue(ypred, train$labs_svm[-obs], positive="1")
recall <- sensitivity(ypred, train$labs_svm[-obs], positive="1")
F1 <- (2 * precision * recall) / (precision + recall)
measures_valid[2,1]<-precision
measures_valid[2,2]<-recall
measures_valid[2,3]<-F1

xtable(measures_valid)

colMeans(measures_valid)

#
