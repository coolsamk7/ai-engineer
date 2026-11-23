import json
from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class TriageResult(BaseModel):
    summary: str = Field(max_length=100)
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
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None
