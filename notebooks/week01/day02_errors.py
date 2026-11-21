import json


def parse_answer(raw: str) -> str | None:
    try:
        data = json.loads(raw)  # like JSON.parse
        return data["answer"]
    except json.JSONDecodeError as e:
        print(f"not JSON: {e}")
        return None
    except KeyError:
        print("JSON, but no 'answer' key")
        return None
    except TypeError:
        print("JSON, but not an object")
        return None


print(parse_answer('{"answer": "retrieval-augmented generation"}'))
print(parse_answer("Sure! Here is the answer: RAG"))
print(parse_answer('{"result": "RAG"}'))
print(parse_answer('["answer"]'))
question = "What is RAG?"
print(f'Question: {question} Reply as JSON: {{"answer": "..."}}')
