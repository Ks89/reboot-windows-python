import ctypes
from ctypes import wintypes

import win32security

from privilege import acquire_privilege

advapi32 = ctypes.windll.advapi32

with acquire_privilege(win32security.SE_SHUTDOWN_NAME):
    ret_val = advapi32.InitiateSystemShutdownExW(
        0, "Cloudbase-Init reboot",
        0, True, True, 0)
    if not ret_val:
        print("Reboot failed")

