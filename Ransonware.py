import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.utils import resample


# Data Generation
def generate_data(num_records):
    file_sizes = np.random.randint(1000, 1000000, num_records)
    file_types = np.random.choice(['.exe', '.txt', '.dll', '.docx', '.zip'], num_records)
    num_connections = np.random.randint(0, 20, num_records)
    outbound_traffic = np.random.randint(10, 10000, num_records)
    encryption_rate = np.random.randint(0, 1000, num_records)
    labels = np.random.choice([0, 1], num_records, p=[0.7, 0.3])  # 70% benign, 30% ransomware

    data = {
        'file_size': file_sizes,
        'file_type': file_types,
        'num_connections': num_connections,
        'outbound_traffic': outbound_traffic,
        'encryption_rate': encryption_rate,
        'label': labels
    }

    df = pd.DataFrame(data)
    return df


df = generate_data(1000)

# Resample Data to balance classes
majority = df[df.label == 0]
minority = df[df.label == 1]

# Upsample minority class
minority_upsampled = resample(minority,
                              replace=True,  # sample with replacement
                              n_samples=len(majority),  # to match majority class
                              random_state=123)  # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([majority, minority_upsampled])

# Shuffle the data
df_upsampled = df_upsampled.sample(frac=1, random_state=123).reset_index(drop=True)

# Load Data
X = df_upsampled.drop('label', axis=1)
X = pd.get_dummies(X, columns=['file_type'])
y = df_upsampled['label']

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression with class_weight
log_reg = LogisticRegression(class_weight='balanced')
log_reg.fit(X_train_scaled, y_train)

# Decision Tree (no class_weight as trees are less sensitive to class imbalance)
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# SVM with class_weight
svm = SVC(class_weight='balanced')
svm.fit(X_train_scaled, y_train)

# Evaluation
models = {'Logistic Regression': log_reg, 'Decision Tree': tree, 'SVM': svm}
for name, model in models.items():
    if name in ['Logistic Regression', 'SVM']:
        y_pred = model.predict(X_test_scaled)
    else:
        y_pred = model.predict(X_test)

    print(f"{name} Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"{name} Classification Report:\n{classification_report(y_test, y_pred, zero_division=0)}")
    print(f"{name} Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
