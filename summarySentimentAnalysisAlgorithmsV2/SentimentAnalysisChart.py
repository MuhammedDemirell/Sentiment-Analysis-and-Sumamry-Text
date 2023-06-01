import matplotlib.pyplot as plt
import SummarySentimentAnalysis as ssa


def matplotlibOutput():
    prediction = ssa.predictSentiment()
    models = ['Positive', 'Negative']
    scores = [prediction, (1 - prediction)]
    colors = ['tab:green', 'tab:red']

    plt.bar(models, scores, color=colors)
    plt.ylim([0, 1])
    plt.title("Score for Sentiment Analysis Models")
    plt.xlabel("Sentiment Analysis")
    plt.ylabel("Score (out of 1)")
    plt.show()
