name = "Sam"
items = ["a", "b", "c"]
score = 0.87654
big = 1234567

# 1. basics: any expression works inside { }
print(f"Hi {name}, you have {len(items)} items")

# 2. format specs: after the colon
print(f"{score:.2f}")  # 2 decimals
print(f"{score:.1%}")  # as a percentage
print(f"{big:,}")  # thousands separator
print(f"[{name:>6}]")  # right-align, width 6

# 3. debug: name AND value
print(f"{score=}")

# 4. prompt building, and the JSON trap
question = "What is RAG?"
context = "RAG = retrieval-augmented generation."
prompt = f"""Answer using only the context.

Context: {context}
Question: {question}
Reply as JSON: {{"answer": "..."}}"""
print(prompt)

price = 1499.5
tokens = 37
limit = 128
print(f"₹{price:,.2f}")
print(f"{tokens / limit:.0%} used")
print(f"{{tokens}}")
print(f"{tokens=}")
