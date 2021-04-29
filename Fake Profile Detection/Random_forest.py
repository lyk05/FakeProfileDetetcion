import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pickle
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv("G:/LYKOS PROGRESS/MAJOR/merge-csv.com__6002de2d457f3.csv")


X=dataset.drop("Target",axis=1)
y=dataset["Target"]



X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.20, random_state=20)




rf_classifier = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 51)
rf_classifier.fit(X_train, y_train)
y_pred_rf = rf_classifier.predict(X_test)


# pickle.dump(rf_classifier, open('fake_profile_detector.pickle', 'wb'))

print(classification_report(y_test, y_pred_rf))
print(metrics.accuracy_score(y_test, y_pred_rf, normalize=False))
# CM = confusion_matrix(y_test, y_pred_rf)
# sns.heatmap(CM)
# plt.ylabel('True Label')
# plt.xlabel('Predicted Label')
# plt.show()