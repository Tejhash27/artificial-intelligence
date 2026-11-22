# Sentiment Analysis using NLP

# Function for sentiment analysis
def analyze_sentiment(text):

    positive_words = [
        "good", "great", "happy", "excellent",
        "love", "wonderful", "best", "awesome",
        "nice", "amazing"
    ]

    negative_words = [
        "bad", "sad", "hate", "worst",
        "poor", "terrible", "awful",
        "angry", "boring", "disappointed"
    ]

    # Convert text to lowercase
    text = text.lower()

    # Tokenization
    words = text.split()

    positive_count = 0
    negative_count = 0

    # Count positive and negative words
    for word in words:
        word = word.strip(".,!?")

        if word in positive_words:
            positive_count += 1

        elif word in negative_words:
            negative_count += 1

    # Determine sentiment
    if positive_count > negative_count:
        return "Positive"

    elif negative_count > positive_count:
        return "Negative"

    else:
        return "Neutral"


# Main program
print("SENTIMENT ANALYSIS USING NLP")
print("----------------------------")

# Sample sentences
sentences = [
    "I love this product",
    "This is a bad experience",
    "The product is good and excellent",
    "I hate this service",
    "The weather is normal today"
]

# Analyze each sentence
for sentence in sentences:

    result = analyze_sentiment(sentence)

    print("\nSentence:", sentence)
    print("Sentiment:", result)

print("\nAnalysis Completed Successfully!")
