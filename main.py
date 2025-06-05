# --- Imports ---

import colorlog
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from PySide6.QtWidgets import QApplication

# --- Logger (Must be called before any logging/custom imports) ---

def set_logger() -> None:
    # Format Strings
    fmt_str = '%(log_color)s%(asctime)s%(reset)s - %(log_color)s%(name)s%(reset)s - %(log_color)s%(levelname)s%(reset)s - %(message)s'
    timefmt_str = '%H:%M:%S'
    datefmt_str = '%Y-%m-%d'
    datetimefmt_str = f"{datefmt_str} {timefmt_str}"

    # Root Logger Config
    logging.basicConfig(
        level=logging.DEBUG,
        format=fmt_str,
        datefmt=datetimefmt_str,
        handlers=[]  # Start with no handlers; you'll add your own below
    )

    # File Logs
    logs_dir = os.path.join(os.path.dirname(sys.executable), '_internal', 'logs') if getattr(sys, 'frozen', False) else os.path.join(os.getcwd(), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt=datetimefmt_str)
    
    # File Handler (Logs DEBUG and above)
    debug_file_handler = TimedRotatingFileHandler(
        filename=os.path.join(logs_dir, "debug.log"),
        when='midnight',
        interval=1,
        backupCount=7
    )
    debug_file_handler.setLevel(logging.DEBUG)  # Capture all logs
    debug_file_handler.setFormatter(file_formatter)

    # File Handler (Logs INFO and above)
    info_file_handler = TimedRotatingFileHandler(
        filename=os.path.join(logs_dir, "info.log"),
        when='midnight',
        interval=1,
        backupCount=7
    )
    info_file_handler.setLevel(logging.INFO)  # Only capture INFO and above
    info_file_handler.setFormatter(file_formatter)

    # Console Handler (Terminal Output, Filtered)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)  # Change dynamically based on needs
    console_formatter = colorlog.ColoredFormatter(
        fmt_str,
        datefmt=datetimefmt_str,
        log_colors={
            'DEBUG': 'purple',
            'INFO': 'cyan',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    console_handler.setFormatter(console_formatter)

    # Root Logger Handlers
    root_logger = logging.getLogger()
    root_logger.addHandler(debug_file_handler)
    root_logger.addHandler(info_file_handler)
    root_logger.addHandler(console_handler)

    # logger.debug("Logger set")

set_logger()

# --- Logger ---

logger = logging.getLogger(__name__)

# --- Config ---

app = QApplication(sys.argv)

def init_config() -> None:
    import core.config as config
    from components.ok_dialog import displayOkDialog
    config.initialize()
    if not config.LOADED:
        displayOkDialog(
            title="Error",
            message="Failed to load config, check logs for more information"
        )
        sys.exit(1)

init_config()

# --- Main ---

def main() -> None:
    try:
        from core.orchestrator import Orchestrator
        orchestrator = Orchestrator()
        orchestrator.run()
        sys.exit(app.exec())
    except Exception:
        logger.exception("An error occurred")
        sys.exit(1)

# --- Run ---

main()

"""
# Compile all python files
py -m compileall .

# Build exe (via .spec file)
pyinstaller exe.spec --clean -y

# Run both commands (only executes second one with first one succeeds)
py -m compileall . ; pyinstaller exe.spec --clean -y

# ; is a command separator in powershell
# && is a command separator in cmd
"""

# NOTE: when issues in program, run exe via cmd-prompt to view output
# "C:\Users\Phil-\__Workbase__\Repositories\mo.waw-stock-map-script-placer\dist\waw-stock-map-script-placer v1.2.1\waw-stock-map-script-placer v1.2.1.exe"