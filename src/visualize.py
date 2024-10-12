import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred):
    """
    Plot a confusion matrix.
    """
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Plot feature importance based on the trained model.
    """
    importances = model.feature_importances_
    indices = sorted(range(len(importances)), key=lambda k: importances[k], reverse=True)
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importance')
    plt.bar(range(len(importances)), importances[indices], align='center')
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.show()
