from pydantic import BaseModel


class Repo(BaseModel):
    full_name: str
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    language: str | None
