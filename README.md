# Regulated Cell Death Playground

![badge][badge-r]
![badge][badge-python]

Collection of analysis scripts and notebooks related to regulated cell death

**The analyses and results can be viewed at https://bioinfodlsu.com/regulated-cell-death-playground/**

## 🧪 Reproducing our results

### Cloning our repository

1. Clone this repository by running:

   ```
   git clone https://github.com/bioinfodlsu/regulated-cell-death-playground
   ```

### Downloading our dataset

1. Download our dataset from this [link](), and place it at the root of the cloned repository.

   💡 If you want to verify the integrity of the downloaded dataset, compute the SHA-512 checksum of the downloaded zipped folder using a hashing utility like `certutil` in Windows, `shasum` in Mac, or `sha512sum` in Linux. You should obtain the following checksum:

   ```
   <checksum>
   ```

1. Extract the contents of the downloaded zipped folder. The extraction process should result in a folder named `data`, and inside it are two folders: `patient` and `public`.

1. Verify that your folder structure is as follows:

   - `regulated-cell-death-playground` (root)
     - `data`
       - `patient`
       - `public`
     - `analysis`

**Note:** If you prefer to run the entire pipeline for generating our dataset (instead of simply downloading it), refer to this [section](https://github.com/bioinfodlsu/regulated-cell-death-playground?tab=readme-ov-file#%EF%B8%8F-running-our-dataset-generation-pipeline).

### Running our analysis scripts and notebooks

1. Our analysis scripts and notebooks are written in R and found inside the `analysis` folder. Refer to this [page](https://bioinfodlsu.com/regulated-cell-death-playground/) for a description of each script/notebook.

1. To set up the dependencies, run `dependencies/install-dependencies.r`.

**Note:** We tested our code on R 4.4.1.

## 🖇️ Running our dataset generation pipeline

1. Install the package manager Conda. We recommend installing [Miniconda](https://docs.anaconda.com/miniconda/install/).
1. Install the workflow management system [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html) by running:

   ```
   conda create -c conda-forge -c bioconda -n snakemake snakemake
   ```

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
