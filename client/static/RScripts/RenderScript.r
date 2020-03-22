
library(rmarkdown)

# To run this script
# Open up Command Prompt from the scripts directory and input
# RScript RenderScript.R 101_File_Name.rmd

Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc")

args <- commandArgs(trailingOnly = TRUE)
inputDir <- "../RMarkdown/"
inputFile <- paste0(inputDir, args[1])

# Set Variable Paths
css <- "libs/style.css"                           # Stylesheet
libDir <- file.path("../ROutput/libs/")           # Libraries
outputDir = "../ROutput"

# Render Document function
renderDoc <- function(filename) {
  
  # Render Function
  rmarkdown::render(inputFile
                    ,output_dir = outputDir
                    ,html_document(theme = "lumen"
                                   ,highlight = "tango"
                                   ,toc = TRUE
                                   ,toc_float = TRUE
                                   ,code_folding = "hide"
                                   ,code_download = TRUE
                                   ,self_contained = FALSE
                                   ,lib_dir = libDir
                                   ,css = css))
}


renderDoc(inputFile)
# "File Rendered: " + inputFile