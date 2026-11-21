import json

from pydantic import BaseModel, Field, ValidationError


class Citation(BaseModel):
    doc_id: str
    page: int


class Answer(BaseModel):
    answer: str
    confidence: float = Field(ge=0, le=1)
    citations: list[Citation] = Field(
        default_factory=list
    )  # fresh list per object, same idea as your None fix


raw = (
    '{"answer": "RAG", "confidence": 0.8, '
    '"citations": [{"doc_id": "a1", "page": "3"}, {"doc_id": "b2"}]}'
)

try:
    Answer.model_validate_json(raw)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])

ok = Answer.model_validate_json('{"answer": "RAG", "confidence": 0.8}')
print(ok.model_dump())

print(json.dumps(Answer.model_json_schema(), indent=2))
