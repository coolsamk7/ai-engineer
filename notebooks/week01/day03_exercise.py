from pydantic import BaseModel, Field, ValidationError
from typing import Literal
import json


class TriageResult(BaseModel):
    summary: str = Field(..., max_length=100)
    priority: Literal["low", "medium", "high"]
    category: Literal["billing", "bug", "account", "other"]
    tags: list[str] = Field(default_factory=list)
    assignee: str | None = None


def parse_triage(raw: str) -> TriageResult | None:
    try:
        return TriageResult.model_validate(json.loads(raw))
    except ValidationError as e:
        for error in e.errors():
            print(f"Field: {error['loc']}, Error: {error['msg']}")
        return None
    except json.JSONDecodeError as d:
        print("Error while decoding json")
        return None


good = '{"summary": "Card charged twice", "priority": "high", "category": "billing", "tags": ["payments"]}'

bad_priority = '{"summary": "Login fails", "priority": "urgent", "category": "account"}'

not_json = "Sure! This looks like a billing issue."

print("Good:", parse_triage(good))
print("Bad priority:", parse_triage(bad_priority))
print("Not JSON:", parse_triage(not_json))

