import sys
import pathlib

# setup for including the project_dir in path
ALGORITHMS_LAB_PATH = pathlib.Path(__file__).parents[1]
if str(ALGORITHMS_LAB_PATH) not in sys.path:
    sys.path.append(str(ALGORITHMS_LAB_PATH.absolute()))
