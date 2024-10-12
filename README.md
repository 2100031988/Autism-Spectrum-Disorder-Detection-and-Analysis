
<p align="center">
  <img src="https://github.com/<your-username>/<your-repo>/blob/main/path-to-image/check.png" alt="Project Logo" width="200">
</p>

<h1 align="center"> Autism Spectrum Disorder (ASD) Detection and Analysis </h1>

<p align="center">
    <img src="https://img.shields.io/github/contributors/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis" alt="Contributors">
    <img src="https://img.shields.io/github/stars/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis" alt="Stars">
    <img src="https://img.shields.io/github/issues/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis" alt="Issues">
    <img src="https://img.shields.io/github/license/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis" alt="License">
</p>

<p align="center">
  <a href="https://github.com/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis/issues">Report Bug</a> |
  <a href="https://github.com/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis/pulls">Request Feature</a> |
  <a href="https://github.com/2100031988/Autism-Spectrum-Disorder-Detection-and-Analysis">View Repo</a>
</p>

---

## 🌟 Project Overview

This project uses Python and machine learning techniques for the detection and analysis of Autism Spectrum Disorder (ASD). It applies data preprocessing and classification models, such as Random Forest, to predict ASD based on behavioral data. The project includes data visualizations and insights, offering a comprehensive analysis of ASD patterns.

---

## 📂 Project Structure

```bash
ASD_Detection_Project/
│
├── data/
│   └── autism_data.csv           # Dataset
│
├── notebooks/
│   └── eda.ipynb                 # Jupyter notebook for exploratory data analysis
│
├── src/
│   ├── __init__.py               # To treat src as a Python module
│   ├── preprocess.py             # Data preprocessing
│   ├── model.py                  # Model Training and Evaluation
│   └── visualize.py              # Data Visualization
│
├── scripts/
│   └── train_model.py            # Main script to run training and evaluation
│
├── requirements.txt              # List of dependencies
├── README.md                     
└── .gitignore                    # To ignore unnecessary files
```

---

## 🚀 Features

- **Data Preprocessing**: Handles missing values and encodes categorical data.
- **Classification Models**: Uses Random Forest to classify and predict ASD.
- **Data Visualizations**: Includes confusion matrices, correlation heatmaps, and feature importance plots for deeper insights.

---

## 💻 How to Run

### Clone the repository:
```bash
git clone https://github.com/<your-username>/<your-repo>
cd ASD_Detection_Project
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Download the dataset and place it in the `data/` folder (if not already included):
- [UCI Autism Screening Adult Dataset](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult)

### Explore the dataset:
Open the exploratory analysis Jupyter notebook:
```bash
jupyter notebook notebooks/eda.ipynb
```

### Train and evaluate the model:
Run the `train_model.py` script to load the data, preprocess it, train the model, and evaluate the results:
```bash
python scripts/train_model.py
```

---

## 🛠️ Technologies Used
- **Python**: For data processing and machine learning.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For building machine learning models.
- **Matplotlib** & **Seaborn**: For data visualization.

---

## 📊 Visualizations

- **Confusion Matrix**: Displays the performance of the classification model.
- **Correlation Heatmap**: Shows relationships between numeric features.
- **Feature Importance**: Highlights the most influential features in the prediction model.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/<your-username>/<your-repo>/blob/main/LICENSE) file for more details.

---

<p align="center">
  <img src="https://github.com/<your-username>/<your-repo>/blob/main/path-to-image/check.png" alt="ASD Detection" width="100">
</p>
