from repo_stats.models.repo_model import Repo
from repo_stats.table import format_table


def make_repo(name: str, stars: int) -> Repo:
    return Repo(
        full_name=name,
        stargazers_count=stars,
        forks_count=1,
        open_issues_count=2,
        language=None,
    )


def test_sorted_by_stars_with_error_last() -> None:
    names = ["small/repo", "bad/repo", "big/repo"]
    results = [
        make_repo("small/repo", 10),
        ValueError("boom"),
        make_repo("big/repo", 92640),
    ]

    lines = format_table(names, results).splitlines()

    assert lines[1].startswith("big/repo")
    assert "92,640" in lines[1]
    assert lines[2].startswith("small/repo")
    assert lines[3] == f"{'bad/repo':<22}ERROR: boom"
    assert lines[1].endswith("-")
