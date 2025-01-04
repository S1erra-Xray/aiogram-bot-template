import subprocess
import sys

image_name = sys.argv[1]
subprocess.run(f"docker image rm -f {image_name}", shell=True)
