cat("\f")
rm(list = ls())

source("00_packages.R")

train <- import("01_import_data/output/train.csv")

test <- import("01_import_data/output/test.csv")

str(train)
