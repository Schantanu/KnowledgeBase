
library(rmarkdown)
library(readxl)

# Set Working Directory
setwd("C:/TESTRMD")
Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc")

# Set Fixed Paths
css <- "libs/style.css"

# Read Website Structure
# df <- read_xlsx("RSCRIPT/DocStructure.xlsx", sheet = "Data")

# Set Today's Date Parameters
todayDay <- weekdays(as.Date(Sys.Date()))
todayDate <- format(as.Date(Sys.Date()), "%d")


files <- list.files(pattern = "\\.rmd$", ignore.case=TRUE)
files

# Render Document function
# renderDoc <- function(i) {

  # Set Variable Paths
  # inputfile <- file.path(getwd(),df$InputFile[i])
  # outputdir <- file.path(getwd(),"ROUTPUT")
  # libs <- file.path(getwd(),"ROUTPUT/libs")
  # libs <- file.path(getwd(),df$OutputDir[i])
  
  inputfile <- file.path(getwd(), 'RMDTest.rmd')
  outputdir <- file.path(getwd(),"ROUTPUT")
  libs <- file.path(getwd(),"ROUTPUT/libs")
  
  # Render Function
  rmarkdown::render(inputfile
                    ,output_dir = "ROUTPUT"
                    ,html_document(theme = "lumen"
                                   ,highlight = "tango"
                                   ,toc = TRUE
                                   ,toc_float = TRUE
                                   ,code_download = TRUE
                                   ,code_folding = "hide"
                                   ,self_contained = FALSE
                                   ,lib_dir = libs
                                   # ,includes = includes
                                   ,css = css))
# }

# Render Doc by ID
# renderDoc(1)

# Loop to Render Document as per Update Frequency
# for (i in 1:nrow(df)) {
#   renderDoc(i)
# }
