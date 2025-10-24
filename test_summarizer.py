from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

text = """
Artificial Intelligence is transforming technology and our lives.
It is now used in healthcare, finance, education, and many other fields.
"""

# Generate summary
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

print("Original Text:\n", text)
print("\nSummary:\n", summary[0]['summary_text'])
