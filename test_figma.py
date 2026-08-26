import os, requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
token = os.environ.get("FIGMA_TOKEN")
file_key = "yCmfEYqA2Q0Ors05DTwjK7"

resp = requests.get(
    f"https://api.figma.com/v1/files/{file_key}",
    headers={"X-Figma-Token": token},
)
print("Status code:", resp.status_code)
print(resp.text[:1500])
