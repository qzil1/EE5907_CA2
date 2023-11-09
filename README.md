# Supplemental Content for EE5907 CA2 Report

This repository contains supplemental content for the EE5907 CA2 course, including several Jupyter notebooks demonstrating different machine learning techniques and a Python script for processing personal photographs.



## Contents

- `PCA.ipynb`: A Jupyter notebook demonstrating the implementation of Principal Component Analysis (PCA).

- `LDA.ipynb`: A Jupyter notebook demonstrating the implementation of Linear Discriminant Analysis (LDA).

- `SVM.ipynb`: A Jupyter notebook demonstrating the implementation of Support Vector Machines (SVM).

- `CNN.ipynb`: A Jupyter notebook demonstrating the implementation of Convolutional Neural Networks (CNN).

- `process_photos.py`: A Python script for processing personal photographs and storing them in a specified directory.

- `requirements.txt`: A text file listing the necessary Python packages for the project.

- `PIE`: The directory unzipped from the CMU PIE dataset. 

  > The files in this directory are organized into various types of folders, and the name of each folder corresponds to the name of its category.

- `Selfish`: (optional) The directory contains your **ORIGINAL** own selfish, you may alter the name of this folder.



## Installation of Dependencies

To install the required dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install all the Python packages listed in the `requirements.txt` file.



## Getting Started

To get started with the Jupyter notebooks, make sure you have Jupyter installed and simply open the `.ipynb` files in your Jupyter environment. You can install Jupyter via pip if you haven't installed it yet:

```bash
pip install jupyter
```

Then navigate to the repository's directory and run:

```bash
jupyter notebook
```

Choose the notebook you wish to open from the Jupyter interface.



## Running the jupyter notebook files

Just run each cell one by one. And **MUST** run them one by one.



## Photo Processing Script

The `process_photos.py` script is designed to take your personal photographs, perform some predefined processing, and then save them to the `./PIE/0` directory.

### Usage

1. Place your personal photographs in a designated folder.
2. Open `process_photos.py` and modify the `folder_path` variable to point to the folder containing your photographs.
3. Run the script. Processed images will be stored in the `./PIE/0` directory.

### Note

- Make sure that the `./PIE/0` directory exists and nothing in it, or the script will make the directory and overwrite the content in the `./PIE/0` directory.
- The script is set to classify all processed selfish photographs under the category '0'.

