from pathlib import Path

import pytest
from pydantic import ValidationError

from repo_stats.models.repo_model import Repo

FIXTURES = Path(__file__).parent / "fixtures"


def test_parses_real_github_response() -> None:
    raw = (FIXTURES / "uv.json").read_text()
    repo = Repo.model_validate_json(raw)

    assert repo.full_name == "astral-sh/uv"
    assert repo.stargazers_count == 92640
    assert repo.language == "Rust"


@pytest.mark.parametrize(
    "bad_json",
    [
        '{"full_name": "a/b"}',
        '{"full_name": "a/b", "stargazers_count": "lots", "forks_count": 0, "open_issues_count": 0, "language": null}',
        "not json at all",
    ],
)
def test_rejects_bad_json(bad_json: str) -> None:
    with pytest.raises(ValidationError):
        Repo.model_validate_json(bad_json)

