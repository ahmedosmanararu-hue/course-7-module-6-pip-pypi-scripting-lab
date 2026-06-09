# automation_tool/__init__.py

from .generate_log import fetch_data, write_log_to_file

# Optional: Define what gets imported when someone uses "from automation_tool import *"
__all__ = ["fetch_data", "write_log_to_file"]