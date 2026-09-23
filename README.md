# Cancer Dose Prediction Using Machine Learning

This project uses Machine Learning Regression to predict the prescribed drug dose for patients based on patient and disease-related features.

## Dataset

The dataset contains 1,000 patient records and 7 columns.

### Input Features

- Age
- Weight (kg)
- Height (cm)
- Tumor Size (mm)
- Disease Severity
- Completed Sessions

### Target

- Prescribed Dose (mg)

The dataset was loaded from an Excel file and checked for missing values and duplicate records. No missing values or duplicate records were found in the dataset.

## Machine Learning Model

A Linear Regression model from the scikit-learn library was used to predict the prescribed dose.

The dataset was divided into:

- 80% Training Data: 800 samples
- 20% Testing Data: 200 samples

A fixed `random_state=42` was used for reproducibility.

## Model Evaluation

The model was evaluated using MAE, MSE, RMSE, and R².

| Metric | Formula | Result |
|---|---|---:|
| MAE | `MAE = (1/n) Σ \|yᵢ - ŷᵢ\|` | 6.7589 mg |
| MSE | `MSE = (1/n) Σ (yᵢ - ŷᵢ)²` | 69.2245 |
| RMSE | `RMSE = √MSE` | 8.3201 mg |
| R² | `R² = 1 - (SSres / SStot)` | 0.9345 |

### Metric Explanation

- **MAE:** Measures the average absolute difference between actual and predicted doses.
- **MSE:** Measures the average squared prediction error.
- **RMSE:** Represents the typical prediction error in the same unit as the target variable (mg).
- **R²:** Measures how much of the variation in prescribed dose is explained by the model.

The model achieved an R² score of 0.9345 on the test set.

## Model Output

The project includes the following model output image:

![Model Output](output.png)

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
├── data.xlsx
├── output.png
├── main.ipynb
└── README.md
```

## Disclaimer

This project is intended for educational and machine learning purposes. It should not be used as a substitute for professional medical judgment or real-world clinical decision-making.