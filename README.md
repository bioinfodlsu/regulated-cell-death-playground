# Regulated Cell Death Playground

![badge][badge-r]
![badge][badge-python]

Collection of analysis scripts and notebooks related to regulated cell death

The analyses and results can be viewed at https://bioinfodlsu.com/regulated-cell-death-playground/

## 🧪 Reproducing Our Results

### A. Read Mapping and Quantification

#### Requirements

- **Operating system:** Linux or Windows (using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install))
- **Notes:**
  - Our scripts for read mapping and quantification are written in Bash.
  - Use `bash` (not `sh`) to run the scripts since we used some Bash-specific syntax for some of the scripts

#### Setting up Dependencies

### B. Downstream Analysis

#### Requirements

- **Operating system:** Linux, Windows, or macOS
- **Notes:**
  - Our downstream analysis scripts are written in Python and R. We have tested our scripts on Python 3.12 and R 4.4.1.

#### Setting up Dependencies

1. Set up the R dependencies:

   - Most IDEs, such as [RStudio](https://posit.co/download/rstudio-desktop/), will automatically prompt you to install the required dependencies when you open a notebook. These dependencies are typically downloaded via [CRAN](https://cran.r-project.org/).
   - However, some bioinformatics-specific dependencies are not available at CRAN and have to be downloaded via [Bioconductor](https://www.bioconductor.org/). To download them in one go, run `install-dependencies.r`

1. Set up the Python dependencies:

## 💻 Authors

- **Mark Edward M. Gonzales** <br>
  gonzales.markedward@gmail.com

- **Kim Williame Lee** <br>
  kim_leejra@dlsu.edu.ph

- **Dr. Anish M.S. Shrestha** <br>
  anish.shrestha@dlsu.edu.ph

This is part of the **"Investigating regulated necrotic cell death in colorectal cancer using a multi-omics approach"** project funded by the [Department of Science and Technology &ndash; Philippine Council for Health Research and Development](https://www.pchrd.dost.gov.ph/) (DOST-PCHRD). This project is led by Dr. Rafael A. Espiritu of the Department of Chemistry, College of Science, De La Salle University.

[badge-r]: https://img.shields.io/badge/r-%23276DC3.svg?style=flat&logo=r&logoColor=white
[badge-python]: https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white
