ch, num = input("문제 번호: ").split(sep=".")

with open(f"Chapter{str(ch).zfill(2)}/{str(num).zfill(2)}.py", encoding="UTF-8") as f:
    for line in f.readlines():
        if line.startswith("# -----"):
            break
        print(line[1:].strip())
        