import os
from PIL import Image

# 設定圖片來源資料夾
img_folder = "C:/Users/178418/Pictures/Screenshots/"  # 來源資料夾，存放 16:9 的截圖圖片
output_folder = "C:/Users/178418/Pictures/CroppedScreenshots/"  # 生成的 A4 比例 PNG 檔案存放資料夾

# A4 紙張的比例 (寬度:高度)
a4_ratio = 210 / 297
target_height = 1080  # 設定目標高度為 1920 像素

# 確保輸出資料夾存在，如果不存在則創建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"已創建輸出資料夾：{output_folder}")

# 讀取所有 PNG 圖片，並按照名稱排序
image_files = sorted([f for f in os.listdir(img_folder) if f.endswith(".png")])

# 如果資料夾內沒有找到 PNG 圖片，則結束程式
if not image_files:
    print("未找到任何 PNG 圖片，請確認圖片目錄是否正確。")
    exit()

# 遍歷資料夾內的所有圖片，並逐一處理
for img_file in image_files:
    img_path = os.path.join(img_folder, img_file)  # 獲取圖片完整路徑
    output_path = os.path.join(output_folder, f"A4_{img_file}")  # 生成的 A4 比例圖片輸出路徑

    try:
        # 開啟圖片
        img = Image.open(img_path)
        img_width, img_height = img.size  # 取得圖片的原始寬度與高度

        # 計算基於目標高度的縮放比例
        scale_factor = target_height / img_height

        # 計算縮放後的目標寬度
        scaled_width = int(img_width * scale_factor)

        # 計算目標裁切寬度，使其符合 A4 的比例
        target_crop_width = int(target_height * a4_ratio)

        # 計算左右兩側需要裁切的範圍
        left_crop = (scaled_width - target_crop_width) // 2
        right_crop = left_crop + target_crop_width

        # 縮放圖片並執行裁切
        resized_img = img.resize((scaled_width, target_height))
        cropped_img = resized_img.crop((left_crop, 0, right_crop, target_height))

        # 儲存裁切後的圖片為 PNG 檔案
        cropped_img.save(output_path, "PNG")
        print(f"已處理並儲存：{img_file} -> {output_path}")

    except FileNotFoundError:
        print(f"錯誤：找不到圖片檔案 {img_path}")
    except Exception as e:
        print(f"處理圖片 {img_file} 時發生錯誤：{e}")

# 印出完成訊息
print("所有 PNG 圖片已處理完成。")
