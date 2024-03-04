cat("\f")
rm(list = ls())

source("00_packages.R")

train <- import("01_import_data/input/train.csv")


test <- import("01_import_data/input/test.csv")

export(train, "01_import_data/output/train.csv")
export(test, "01_import_data/output/test.csv")
