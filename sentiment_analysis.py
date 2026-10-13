
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob

OUTPUT_DIR = Path("outputs")

# Sample tweets for demonstration.
tweets = [
    "I love this product. It is amazing!",
    "Today is a wonderful and happy day.",
    "The service was excellent.",
    "I am very pleased with the results.",
    "This is a fantastic experience.",
    "I hate this product. It is terrible.",
    "The service was awful.",
    "I am unhappy with this experience.",
    "This is the worst day ever.",
    "The quality is horrible.",
    "The meeting starts at ten o'clock.",
    "I went to the store today.",
    "The package arrived this morning.",
    "I am reading a book.",
    "The event is scheduled for Monday."
]


def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    results = []

    for tweet in tweets:
        sentiment, score = analyze_sentiment(tweet)

        results.append({
            "Tweet": tweet,
            "Sentiment": sentiment,
            "Polarity": round(score, 3)
        })

    df = pd.DataFrame(results)

    # Save classification results.
    df.to_csv(OUTPUT_DIR / "sentiment_results.csv", index=False)

    print("\n=== TWITTER SENTIMENT ANALYSIS ===\n")
    print(df.to_string(index=False))

    print("\nSentiment Summary:")
    print(df["Sentiment"].value_counts())

    # Generate a sentiment distribution chart.
    counts = (
        df["Sentiment"]
        .value_counts()
        .reindex(["Positive", "Negative", "Neutral"], fill_value=0)
    )

    counts.plot(kind="bar", figsize=(8, 5))
    plt.title("Sentiment Distribution of Sample Tweets")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=0)
    plt.tight_layout()

    chart_path = OUTPUT_DIR / "sentiment_chart.png"
    plt.savefig(chart_path, dpi=150)
    plt.show()

    # Analyze a tweet entered by the user.
    while True:
        text = input("\nEnter a tweet (or type exit): ").strip()

        if text.lower() == "exit":
            print("Sentiment analysis completed.")
            break

        if not text:
            print("Please enter some text.")
            continue

        sentiment, score = analyze_sentiment(text)

        print("Sentiment:", sentiment)
        print(f"Polarity score: {score:.3f}")

    print("\nResults saved in the outputs folder.")


if __name__ == "__main__":
    main()