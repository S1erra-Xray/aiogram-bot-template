import subprocess
from os.path import dirname, abspath

requirements = subprocess.run("poetry export --without-hashes --format=requirements.txt", capture_output=True, text=True)
proj_top_dir = dirname(dirname(abspath(".")))

with open(f"{proj_top_dir}/requirements.txt", "w") as requirements_file:
    requirements_file.write(requirements.stdout)
    requirements_file.close()
