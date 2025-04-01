import requests

url = "https://nlp100.github.io/data/popular-names.txt"
response = requests.get(url)
data = response.text

filename = "popular-names.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(data)

# 10. 計算行數 
print("10. 文件總行數:")
with open(filename, "r", encoding="utf-8") as f:
    print(sum(1 for _ in f))

# 11. 替換制表符為空格 
print("\n11. 替換制表符為空格:")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.replace("\t", " "), end="")

# 12. 提取第一、二列
col1, col2 = [], []
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        col1.append(parts[0])
        col2.append(parts[1])

with open("col1.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(col1) + "\n")
with open("col2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(col2) + "\n")
print("\n12. 第一列與第二列已保存為 col1.txt 和 col2.txt")

# 13. 合併 col1.txt 和 col2.txt
print("\n13. 合併 col1.txt 和 col2.txt:")
with open("col1.txt", "r", encoding="utf-8") as f1, open("col2.txt", "r", encoding="utf-8") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + "\t" + line2.strip())

# 14. 前 N 行
N = 10  
print(f"\n14. 前 {N} 行:")
with open(filename, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= N:
            break
        print(line, end="")

# 15. 後 N 行 
print(f"\n15. 後 {N} 行:")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[-N:]:
        print(line, end="")

# 16. 分割成 N 份 
print(f"\n16. 將文件分為 {N} 份:")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    chunk_size = len(lines) // N
    for i in range(N):
        part = lines[i * chunk_size: (i + 1) * chunk_size]
        with open(f"split_{i+1}.txt", "w", encoding="utf-8") as f_out:
            f_out.writelines(part)
        print(f"split_{i+1}.txt 創建完成")

# 17. 第一列的唯一值 
print("\n17. 第一列中的非重複字符串:")
unique_names = sorted(set(col1))
print("\n".join(unique_names))

# 18. 按第三列降序排序 
print("\n18. 以第三列為指標對各行進行降序排序:")
with open(filename, "r", encoding="utf-8") as f:
    sorted_lines = sorted(f.readlines(), key=lambda x: int(x.split("\t")[2]), reverse=True)
    for line in sorted_lines:
        print(line, end="")

# 19. 計算第一列的出現頻率並排序 
print("\n19. 第一列的字符串出現頻率降序排列:")
from collections import Counter
counted = Counter(col1)
for name, count in sorted(counted.items(), key=lambda x: x[1], reverse=True):
    print(f"{count} {name}")
