#outperformance measure

#ALL-IDB2
all_lamb<-0.9615
all<-c(0.8972, 0.9384, 0.9524,
      0.9567, 0.9611
       )

mean((all_lamb/all)-1)#0.0222544


#C-NMC
c_lamb<-0.919
cnmc<-c(0.869, 0.867,
        0.857, 0.879
        )

mean((c_lamb/cnmc)-1)#0.04731982


#overall
mean( ( c(c_lamb/cnmc, all_lamb/all ) -1 )  )#0.03851533

#
