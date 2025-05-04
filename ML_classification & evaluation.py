# Importing required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Example data
data = pd.DataFrame({
    'Disorder': ['Anxiety', 'Depression', 'Bipolar', 'PTSD', 'Depression', 'Anxiety'],
    'Incidence_Rate': [0.1, 0.2, 0.15, 0.12, 0.18, 0.11]
})

# Encode the 'Disorder' column
label_encoder = LabelEncoder()
data['Disorder_Encoded'] = label_encoder.fit_transform(data['Disorder'])

# Features and target
X = data[['Incidence_Rate']]  # Feature
y = data['Disorder_Encoded']  # Target

# Train-test split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize models
models = {
    'Support Vector Machine': SVC(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=1),  # ✅ fixed here
    'Logistic Regression': LogisticRegression(max_iter=1000)
}

# Dictionary to store evaluation metrics
metrics = {}

# Train and evaluate models
for model_name, model in models.items():
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Predict on test set

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    # Store metrics
    metrics[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1
    }

# Convert metrics into a DataFrame for better display
metrics_df = pd.DataFrame(metrics).T
print(metrics_df)
