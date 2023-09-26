from typing import Optional
import settings


class GithubClient:
    def __init__(
        self,
        base_url: Optional[str] = settings.GITLAB_BASE_URL,
        repo_path: Optional[str] = settings.GITLAB_PROJECT_ID,
        token: Optional[str] = settings.GITLAB_TOKEN,
    ) -> None:
        self.repo_path = repo_path
        self.token = token
        self.url = f"{base_url}/repos/{self.repo_path}"

    @property
    def auth_header(self) -> dict:
        return {"Authorization": f"token {self.token}"}
