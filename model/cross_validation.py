import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def cross_validation_split(df, target_column, n_splits=10):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    splits = []
    for train_index, val_index in kf.split(X):
        X_train, X_val = X.iloc[train_index], X.iloc[val_index]
        y_train, y_val = y.iloc[train_index], y.iloc[val_index]
        splits.append((X_train, X_val, y_train, y_val))
    return splits

def perform_cross_validation(df, target_column):
    splits = cross_validation_split(df, target_column)
    results = []
    for i, (X_train, X_val, y_train, y_val) in enumerate(splits):
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        accuracy = accuracy_score(y_val, y_pred)
        results.append((i, accuracy))
    avg_accuracy = sum(acc for _, acc in results) / len(results)
    return results, avg_accuracy


#Hinzufügen in boardgameapp.py für Ausführung
# st.write("Durchführung der Cross-Validation...")
 #       results, avg_accuracy = perform_cross_validation(df, 'target')
  #      for i, accuracy in results:
   #         st.write(f"Fold {i+1} Accuracy: {accuracy:.4f}")
    #    st.write(f"Average Accuracy: {avg_accuracy:.4f}")#