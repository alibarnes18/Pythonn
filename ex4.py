

#ERROR 10.0.0.2 login failed
#ERROR 172.16.0.9 login failed

with open("access.log", "r") as f:
    with open("error.log", "w") as out:
        for line in f:
            if "ERROR" in line.
            out.write(line)