import os
import re

# 設定目標資料夾
folder_path = r"C:\Users\178418\Pictures\Screenshots"  # 修改為你的資料夾路徑

# 遍歷資料夾內的所有檔案
for filename in os.listdir(folder_path):
    match = re.search(r"螢幕擷取畫面 \((\d+)\)", filename)  # 正則表達式匹配數字
    if match:
        num = int(match.group(1))  # 提取數字
        new_filename = re.sub(r"\((\d+)\)", f"({num:02})", filename)  # 替換為兩位數格式
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        if old_path != new_path:  # 避免重複命名
            os.rename(old_path, new_path)
            print(f"重命名: {filename} → {new_filename}")

print("批量重新命名完成！")
