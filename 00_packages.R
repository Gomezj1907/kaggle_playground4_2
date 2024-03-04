if(system.file(package='pacman') == ""){ install.packages('pacman')
  require(pacman)
  }else{require(pacman)}

p_load(rio, tidyverse, data.table,
       
       #Machine learning
       tidymodels, caret, ranger, rpart, rpart.plot, xgboost)
