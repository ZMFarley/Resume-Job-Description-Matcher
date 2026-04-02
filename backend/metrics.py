#Calculate relevant metrics and graphs for classifier performance
def __output_metrics(clf: LogisticRegression, training_embedding_matrix: np.ndarray, label_matrix: np.ndarray, predicted_results: np.ndarray) -> None:
    #Calculate relevant metrics and graph for the classifier
    print(classification_report(label_matrix, predicted_results))
    print(confusion_matrix(label_matrix, predicted_results))
    print("Reciever Operating Characteristic Area Under the Curve Score", roc_auc_score(label_matrix, clf.predict_proba(training_embedding_matrix)[:, 1]))
    plot = RocCurveDisplay.from_predictions(label_matrix, clf.predict_proba(training_embedding_matrix)[:, 1], plot_chance_level = True)
    _ = plot.ax_.set(xlabel="False Positive Rate", ylabel="True Positive Rate",
    title="Trainning AI vs Real Image Detection\nReceiver Operating Characteristic",
    )
    plt.show()