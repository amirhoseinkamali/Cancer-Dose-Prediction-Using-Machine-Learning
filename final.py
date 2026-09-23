import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import tkinter as tk
from tkinter import messagebox



# Load data
data = pd.read_excel('project3_cancer_dose_data.xlsx')
print("First 5 rows:")
print(data.head())
print("\nData info:")
print(data.info())

X = data[['Age', 'Weight_kg', 'Height_cm', 'Tumor_Size_mm', 'Disease_Severity', 'Completed_Sessions']]
y = data[['Prescribed_Dose_mg']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\nModel Errors:")
print(f"MSE: {mse:.2f}")
print(f"MAE: {mae:.2f} mg")
print(f"RMSE: {rmse:.2f} mg")


# Main window
root = tk.Tk()
root.title("Cancer Drug Dose Predictor")
root.geometry("450x550")
root.configure(bg='#f0f0f0')

# Title
title_label = tk.Label(
    root, 
    text="Cancer Drug Dose Predictor", 
    font=("Arial", 16, "bold"),
    bg='#f0f0f0',
    fg='#1a237e'
)
title_label.pack(pady=15)

# Error metrics display
error_frame = tk.Frame(root, bg='#e3f2fd', relief='solid', bd=1)
error_frame.pack(pady=5, padx=20, fill='x')

tk.Label(
    error_frame,
    text="Model Performance",
    font=("Arial", 11, "bold"),
    bg='#e3f2fd'
).pack(pady=5)

tk.Label(
    error_frame,
    text=f"MAE: {mae:.2f} mg    MSE: {mse:.2f}    RMSE: {rmse:.2f} mg",
    font=("Arial", 10),
    bg='#e3f2fd',
    fg='#333'
).pack(pady=5)

# Input fields
input_frame = tk.Frame(root, bg='#f0f0f0')
input_frame.pack(pady=15, padx=20)

labels = [
    "Age (years)",
    "Weight (kg)",
    "Height (cm)",
    "Tumor Size (mm)",
    "Disease Severity (1-10)",
    "Completed Sessions"
]

entries = []

for i, label in enumerate(labels):
    row_frame = tk.Frame(input_frame, bg='#f0f0f0')
    row_frame.pack(pady=6, fill='x')
    
    tk.Label(
        row_frame,
        text=label + ":",
        font=("Arial", 11),
        bg='#f0f0f0',
        width=18,
        anchor='w'
    ).pack(side='left')
    
    entry = tk.Entry(
        row_frame,
        font=("Arial", 11),
        width=15,
        relief='solid',
        bd=1
    )
    entry.pack(side='left')
    entries.append(entry)

# Predict function
def predict():
    try:
        # Get values
        values = [float(entry.get()) for entry in entries]
        
        # Check disease severity range
        if values[4] < 1 or values[4] > 10:
            messagebox.showerror("Error", "Disease severity must be between 1 and 10")
            return
        
        # Predict
        result = model.predict([values])
        
        # Show result
        result_label.config(
            text=f"Predicted Dose: {result[0][0]:.2f} mg",
            fg='#1a237e',
            font=("Arial", 14, "bold")
        )
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# Predict button
predict_btn = tk.Button(
    root,
    text="Predict Dose",
    command=predict,
    bg='#1a237e',
    fg='white',
    font=("Arial", 12, "bold"),
    padx=30,
    pady=8,
    relief='raised',
    bd=2,
    cursor='hand2'
)
predict_btn.pack(pady=15)

# Result display
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg='#f0f0f0'
)
result_label.pack(pady=10)

# Exit button
exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    bg='#d32f2f',
    fg='white',
    font=("Arial", 10),
    padx=20,
    pady=5,
    relief='raised',
    bd=1,
    cursor='hand2'
)
exit_btn.pack(pady=10) 

root.mainloop()