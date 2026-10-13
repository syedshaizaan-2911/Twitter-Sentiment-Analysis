# Twitter Sentiment Analysis Using Python

## Project Overview

Twitter Sentiment Analysis is a Natural Language Processing (NLP) project that analyzes text and classifies its sentiment as Positive, Negative, or Neutral. The project uses the TextBlob library to calculate sentiment polarity and determine the overall sentiment of tweets.

## Objectives

* Analyze the sentiment of tweets using NLP techniques.
* Classify text into Positive, Negative, and Neutral categories.
* Calculate the polarity score for each tweet.
* Visualize the distribution of sentiments using a bar chart.
* Allow users to enter their own text for sentiment analysis.

## Technologies Used

* **Python** – Programming language
* **TextBlob** – Sentiment analysis
* **Pandas** – Data handling and analysis
* **Matplotlib** – Data visualization

## Features

* Sentiment classification of sample tweets.
* Polarity score calculation ranging from -1 to +1.
* Interactive text input for analyzing new tweets.
* Export of sentiment results to a CSV file.
* Bar chart showing the distribution of positive, negative, and neutral tweets.

## Project Structure

```text
Twitter-Sentiment-Analysis/
├── sentiment_analysis.py
├── requirements.txt
├── README.md
└── outputs/
    ├── sentiment_results.csv
    └── sentiment_chart.png
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Twitter-Sentiment-Analysis.git
cd Twitter-Sentiment-Analysis
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

If you use PowerShell and activation is blocked, you can skip activation and run Python directly from the virtual environment.

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python sentiment_analysis.py
```

The program analyzes sample tweets, displays sentiment classifications and polarity scores, generates a bar chart, and allows users to enter their own text.

## Sentiment Classification

TextBlob calculates a polarity score between -1 and +1.

* **Positive:** Polarity greater than 0
* **Negative:** Polarity less than 0
* **Neutral:** Polarity equal to 0

### Example

| Input Text                | Expected Sentiment |
| ------------------------- | ------------------ |
| I love this product!      | Positive           |
| This service is terrible. | Negative           |
| The meeting starts today. | Neutral            |

Actual classifications depend on the polarity calculated by TextBlob.

## Output

The project generates the following files:

* `outputs/sentiment_results.csv` – Contains tweets, sentiment labels, and polarity scores.
* `outputs/sentiment_chart.png` – Displays the distribution of sentiment categories.

## Applications

* Social media opinion analysis
* Customer feedback analysis
* Product review classification
* Brand reputation monitoring
* Public opinion research

## Limitations

This project uses a basic lexicon-based sentiment analysis approach. It may not correctly interpret sarcasm, slang, complex sentence structures, or context-dependent expressions. The sample dataset is provided for demonstration; live Twitter data collection is not included.

## Conclusion

The Twitter Sentiment Analysis project demonstrates how Natural Language Processing can be used to classify text into sentiment categories. It provides practical experience with Python, TextBlob, Pandas, and Matplotlib, along with basic data analysis and visualization.

## Disclaimer

This project is developed for educational and internship purposes only. Sentiment classifications are automated estimates and may not accurately represent the author's intended meaning.
