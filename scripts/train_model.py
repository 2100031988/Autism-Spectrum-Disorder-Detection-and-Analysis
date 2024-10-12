from src.preprocess import load_and_clean_data, split_data
from src.model import train_model, evaluate_model
from src.visualize import plot_confusion_matrix

# Step 1: Load and preprocess the data
file_path = 'data/autism_data.csv'
df = load_and_clean_data(file_path)

# Print the column names to confirm
print("Columns in the dataset:", df.columns)

# Step 2: Split the data into training and testing sets
# Update the column name to match the actual name in the dataset
X_train, X_test, y_train, y_test = split_data(df, 'Class/ASD_b\'YES\'')

# Step 3: Train the model
model = train_model(X_train, y_train)

# Step 4: Evaluate the model
accuracy, report = evaluate_model(model, X_test, y_test)
print(f"Accuracy: {accuracy}")
print(report)

# Step 5: Plot confusion matrix
plot_confusion_matrix(y_test, model.predict(X_test))
