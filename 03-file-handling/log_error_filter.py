

#ERROR 10.0.0.2 login failed
#ERROR 172.16.0.9 login failed

from pathlib import Path

_LOG = Path(__file__).resolve().parent / "data" / "access.log"
with open(_LOG, "r") as f:
    with open("error.log", "w") as out:
        for line in f:
            if "ERROR" in line.
            out.write(line)