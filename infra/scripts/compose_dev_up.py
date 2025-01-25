import subprocess
from pathlib import Path

path = Path(__file__).parent.parent.parent

subprocess.run(
    f"docker compose -f {path}/docker-files/dev/compose-dev.yaml up -d fsm postgres",
    shell=True,
)
