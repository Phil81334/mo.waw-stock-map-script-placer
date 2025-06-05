# --- Imports ---

import os
import subprocess

# --- Main ---

def run_executable(running_dir: str, exe_path: str, exe_args: str) -> dict:
    """
    Runs the given executable with no arguments.
    exe_path: Path to the executable file
    """
    os.chdir(running_dir)  # required

    try:
        subprocess.Popen(
            [exe_path, exe_args],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return {"success": True, "data": None}
    except Exception as e:
        return {"success": False, "exception": type(e).__name__, "error": str(e)}
    