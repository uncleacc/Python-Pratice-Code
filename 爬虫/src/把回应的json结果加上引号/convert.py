list = []
dic = []

with open("src.txt", mode="r", encoding='utf-8') as f:
    str = f.read()
    list = str.split('\n')

f.close()
with open("out.txt", mode="w", encoding='utf-8') as f:
    for s in list:
        s1 = s.split(':')[0].strip()
        s2 = s.split(':')[1].strip()
        f.write(f"\"{s1}\"" + ": " + f"\"{s2}\"," + "\n")
