import os
import pandas as pd
import dill
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv(r"C:\Users\tmani\Downloads\StudentsPerformance.csv")

# Features and target
X = df.drop(columns=['math score'])
y = df['math score']

# Identify categorical and numerical features
categorical_features = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
numerical_features = ['reading score', 'writing score']

# Preprocessing
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(sparse=False, handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=128, random_state=42))
])

# Train
model.fit(X_train, y_train)

# Save preprocessor and regressor separately
os.makedirs('artifacts', exist_ok=True)
with open('artifacts/preprocessor.pkl', 'wb') as f:
    dill.dump(preprocessor, f)

with open('artifacts/model.pkl', 'wb') as f:
    dill.dump(model.named_steps['regressor'], f)

print("Model and preprocessor saved successfully.")
