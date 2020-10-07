rm(list=ls())


library(xtable) #for table creation for latex
library(e1071)#for svm

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
                  rep(2, dim(ei_h)[1])    ) )

#counts plot
temp<-as.data.frame(cbind(ei,sp, color, texture, data))

#setup for SVM model

train<-as.data.frame(cbind(as.factor(labs), temp))
colnames(train)[1]<-"labs_svm"

#variables to keep
keep<-c(1:25)

#now let's tune the svm model using 5-folds on t-set and validaiton

set.seed(22773)

keep2<-which(train$labs_svm==1)
keep3<-which(train$labs_svm==2)

#80% for training and 20% for validation
obs_1 = keep2[1:floor(length(keep2)*0.80)]
obs_2 = keep3[1:floor(length(keep3)*0.80)]

obs<-c(obs_1, obs_2)

tc <- tune.control(cross = 5)

tune.out<-tune(svm, as.factor(labs_svm) ~.,
          data=train[obs, keep],
          kernel='radial',
          ranges=list(cost=c(1:2, 5, 10),
                      gamma=c(1/dim(train)[1], 1/dim(train[,keep])[2], 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.75, 1, 1.5 )
                      ) ,
          tunecontrol = tc)

summary(tune.out)

#training data
ypred=predict(tune.out$best.model ,train[obs,])
table(predict=ypred, truth=train$labs_svm[obs])
mean(ypred==as.factor(as.numeric(train$labs_svm[obs])))

#validation data
ypred=predict(tune.out$best.model ,train[-obs,])
table(predict=ypred, truth=train$labs_svm[-obs])
tab_v<-table(predict=ypred, truth=train$labs_svm[-obs])
mean(ypred==as.factor(as.numeric(train$labs_svm[-obs])))

#obtaining 95% CI
binom.test(x=sum(diag(tab_v)), n=sum(tab_v), p= mean(ypred==as.factor(as.numeric(train$labs_svm[-obs]))) )

#calculating varibale importance
w <- t(tune.out$best.model$coefs) %*% tune.out$best.model$SV    # weight vectors
w <- apply(w, 2, function(v){sqrt(sum(v^2))})                   # weight
w_sort <- sort(w, decreasing = T)

#max weight
w_max<-(w[1])

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

#
