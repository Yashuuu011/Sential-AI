"""
Root package shim so `uvicorn backend.main:app` works when run from the repository root
(e.g. on Render when Root Directory is not set to `MalwareDetect`).
"""

import os
import sys

_repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_malware_detect_dir = os.path.join(_repo_root, "MalwareDetect")

if _malware_detect_dir not in sys.path:
    sys.path.insert(0, _malware_detect_dir)

# Ensure relative paths (like ./malware_model_output/lightgbm.pkl) resolve from MalwareDetect/
if os.path.isdir(_malware_detect_dir):
    os.chdir(_malware_detect_dir)

# Point submodules (backend.main, backend.routers, etc.) to MalwareDetect/backend
__path__ = [os.path.join(_malware_detect_dir, "backend")]

