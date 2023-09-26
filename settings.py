from dotenv import load_dotenv
import os


load_dotenv()


GITLAB_BASE_URL = os.getenv("GITLAB_BASE_URL", "https://gitlab.com/api/v4")
GITHUB_BASE_URL = os.getenv("GITHUB_BASE_URL", "https://api.github.com")

GITLAB_PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")
GITHUB_REPO_PATH = os.getenv("GITHUB_REPO_PATH")

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
