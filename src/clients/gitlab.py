from typing import Optional
import settings


class GitlabClient:
    def __init__(
        self,
        base_url: Optional[str] = settings.GITLAB_BASE_URL,
        project_id: Optional[str] = settings.GITLAB_PROJECT_ID,
        token: Optional[str] = settings.GITLAB_TOKEN,
    ) -> None:
        self.project_id = project_id
        self.token = token
        self.url = f"{base_url}/projects/{self.project_id}"

    @property
    def auth_header(self) -> dict:
        return {"Private-Token": self.token}
