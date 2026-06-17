import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("C:/Users/rahul/BDA_Nayan/chicago_crimes.csv")

# Take smaller sample for ML
data = data.sample(n=50000, random_state=42)

# Select useful columns
data = data[["Primary Type", "District", "Year", "Arrest"]]

# Drop missing values
data = data.dropna()

# Convert categorical data
le = LabelEncoder()
data["Primary Type"] = le.fit_transform(data["Primary Type"])

# Features and target
X = data[["Primary Type", "District", "Year"]]
y = data["Arrest"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# ---- Test Case Prediction ----
# THEFT
# BATTERY
# CRIMINAL DAMAGE
# NARCOTICS
# ASSAULT
# OTHER OFFENSE
# BURGLARY
# MOTOR VEHICLE THEFT
# DECEPTIVE PRACTICE
# ROBBERY
# WEAPONS VIOLATION
# CRIMINAL TRESPASS
# PUBLIC PEACE VIOLATION
# OFFENSE INVOLVING CHILDREN
# PROSTITUTION
# SEX OFFENSE
# 1 to 25
# 2001 to 2020
print("\n--- Test Prediction ---")

crime_type = input("Enter Crime Type (e.g., THEFT): ")
district = int(input("Enter District (e.g., 8): "))
year = int(input("Enter Year (e.g., 2020): "))

# Encode crime type
crime_type_encoded = le.transform([crime_type])[0]

# Create DataFrame with correct column names
test_df = pd.DataFrame({
    "Primary Type": [crime_type_encoded],
    "District": [district],
    "Year": [year]
})

# Predict
prediction = model.predict(test_df)

# Output
if prediction[0]:
    print("Prediction: Arrest")
else:
    print("Prediction: No Arrest")