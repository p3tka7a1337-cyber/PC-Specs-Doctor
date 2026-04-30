import psutil
import subprocess
import re

def get_cpu():
    try:
        # PowerShell метод (най-точен за Windows)
        cmd = 'powershell "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"'
        output = subprocess.check_output(cmd, shell=True)
        cpu = output.decode(errors="ignore").strip().split("\n")[0]
        return cpu if cpu else "Unknown CPU"
    except:
        return "Unknown CPU"


def get_gpu():
    try:
        # PowerShell метод (по-нов от wmic)
        cmd = 'powershell "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"'
        output = subprocess.check_output(cmd, shell=True)
        gpus = output.decode(errors="ignore").strip().split("\n")

        gpus = [g.strip() for g in gpus if g.strip()]
        return gpus[0] if gpus else "Unknown GPU"

    except:
        return "Unknown GPU"


def get_ram():
    return round(psutil.virtual_memory().total / (1024 ** 3))


def get_user_specs():
    return {
        "cpu": get_cpu(),
        "gpu": get_gpu(),
        "ram": get_ram()
    }