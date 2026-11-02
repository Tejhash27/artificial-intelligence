
# Sentiment Analysis using NLP

from textblob import TextBlob

# Input text from user
text = input("Enter a sentence: ")

# Create TextBlob object
blob = TextBlob(text)

# Calculate sentiment polarity
polarity = blob.sentiment.polarity

# Display sentiment result
print("\nSentiment Analysis Result")

print("Input Text:", text)
print("Polarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive")

elif polarity < 0:
    print("Sentiment: Negative")

else:
    print("Sentiment: Neutral")
