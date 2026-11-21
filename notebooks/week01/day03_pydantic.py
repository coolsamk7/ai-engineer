from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class Answer(BaseModel):
    answer: str
    confidence: float = Field(ge=0, le=1)  # 0 ≤ x ≤ 1, like @Min/@Max
    source: Literal["docs", "web"] = "docs"  # only these values, like @IsIn


def parse_answer(raw: str) -> Answer | None:
    try:
        return Answer.model_validate_json(raw)  # JSON.parse + validate in one step
    except ValidationError as e:
        print(f"invalid: {e.error_count()} error(s)")
        for err in e.errors():
            print("   ", err["loc"], "->", err["msg"])
        return None


print(parse_answer('{"answer": "RAG", "confidence": 0.9}'))  # 1
print(parse_answer('{"answer": "RAG", "confidence": 1.5}'))  # 2
print(parse_answer('["answer"]'))  # 3
print(parse_answer("Sure! Here is the answer"))  # 4
print(parse_answer('{"answer": "RAG", "confidence": "0.9", "source": "blog"}'))  # 5
