import pytest

from ai_engineer.triage import parse_triage


def test_good_input_parses():
    raw = '{"summary": "Card charged twice", "priority": "high", "category": "billing"}'
    result = parse_triage(raw)
    assert result is not None
    assert result.priority == "high"
    assert result.tags == []


@pytest.mark.parametrize(
    "raw",
    [
        '{"summary": "Login fails", "priority": "urgent", "category": "account"}',  # bad priority
        '{"summary": "x", "priority": "low", "category": "sales"}',  # bad category
        '{"priority": "low", "category": "bug"}',  # missing summary
        '{"summary": "'
        + "a" * 101
        + '", "priority": "low", "category": "bug"}',  # summary too long
        "Sure! This is billing.",  # not JSON
        '["answer"]',  # JSON, but a list
    ],
)
def test_invalid_returns_none(raw):
    assert parse_triage(raw) is None
