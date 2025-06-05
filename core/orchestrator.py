# --- Imports ---

import logging

# --- Logger ---

logger = logging.getLogger(__name__)

# --- Main ---

from core.main_window import MainWindow
from core.script_placer import ScriptPlacer

class Orchestrator:
    def __init__(self) -> None:
        self.main_window = MainWindow()
        self.main_window.close_event.connect(self.shutdown)

        self.scriptPlacer = ScriptPlacer(self.main_window)
    
    def run(self) -> None:
        self.main_window.show()

    def shutdown(self) -> None:
        # Clean up long running tasks
        logger.info("Shutting down long running tasks")
    