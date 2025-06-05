# --- Imports ---

import json
import logging
import os
import sys
import traceback

# --- Logger ---

logger = logging.getLogger(__name__)

# --- Constants ---

LOADED = False
CWD = os.path.join(os.path.dirname(sys.executable), '_internal') if getattr(sys, 'frozen', False) else os.getcwd()

LOCAL: dict

WAW_ROOT_DIR: str

# --- Main ---

def load_local() -> None:
    """
    Loads local configuration from the local.json file.
    """
    global LOCAL
    path = os.path.join(CWD, 'resources', 'json', 'local.json')
    with open(path, 'r') as f:
        LOCAL = json.load(f)

def set_globals() -> None:
    """
    Sets global variables.

    This function should be called after all other config functions are called.
    """
    global WAW_ROOT_DIR
    WAW_ROOT_DIR = LOCAL['waw_root_dir']
    
    # logger.debug("Globals set")

def validate_waw_root_dir() -> None:
    """
    Validates the WaW root directory.
    """
    if not os.path.exists(WAW_ROOT_DIR):
        msg = f"Error: The WaW Root Directory '{WAW_ROOT_DIR}' does not exist"
        logger.debug(msg)
        raise Exception(msg)

# --- Initialize ---

def initialize() -> None:
    """
    Initialize config.

    This function should be called after logger is set in main.py, and before everything else.
    """
    global LOADED

    config_steps = [
        (load_local, None),
        (set_globals, None),
        (validate_waw_root_dir, None)
    ]

    for func, args in config_steps:
        try:
            if args is None:
                func()
            else:
                if isinstance(args, list):
                    func(*args)
                else:
                    func(args)
        except Exception as e:
            logger.error(f"An error occurred in '{func.__name__}', error: {e}")
            # traceback.print_exc()
            return

    LOADED = True
    logger.info("Config successfully loaded")
