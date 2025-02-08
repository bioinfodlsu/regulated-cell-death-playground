if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("TCGAbiolinks")
BiocManager::install("RNAseqQC")
BiocManager::install("DESeq2")
BiocManager::install("ensembldb")
BiocManager::install("vsn")
BiocManager::install("illuminaHumanv4.db")
