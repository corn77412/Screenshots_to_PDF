# 按 Win + PrtScn，這樣會螢幕截圖並自動保存為PNG檔案，並儲存在"C:/Users/178418/Pictures/Screenshots/"。
import os
from PIL import Image
from reportlab.pdfgen import canvas

# 設定圖片來源資料夾
img_folder = "C:/Users/178418/Pictures/Screenshots/"  # 來源資料夾，存放 16:9 的截圖圖片
output_pdf_path = "output.pdf"  # 生成的 PDF 檔案名稱

# 讀取所有 PNG 圖片，並按照名稱排序，確保順序正確
image_files = sorted([f for f in os.listdir(img_folder) if f.endswith(".png")])

# 如果資料夾內沒有找到 PNG 圖片，則結束程式
if not image_files:
    print("未找到任何 PNG 圖片，請確認圖片目錄是否正確。")
    exit()

# 創建 PDF 檔案
c = canvas.Canvas(output_pdf_path)

# 遍歷資料夾內的所有圖片，並逐一處理
for img_file in image_files:
    img_path = os.path.join(img_folder, img_file)  # 獲取圖片完整路徑

    # 開啟圖片
    img = Image.open(img_path)
    img_width, img_height = img.size  # 取得圖片的原始寬度與高度

    # 計算裁切後的寬度，使其符合 210:297 的比例（與 A4 直式比例一致）
    target_width = int(img_height * 210 / 297)

    # 計算左右兩側需要裁切的範圍
    left_crop = (img_width - target_width) // 2  # 左側裁切的起點
    right_crop = left_crop + target_width  # 右側裁切的終點

    # 執行裁切，只保留圖片的中間區域，使其符合 210:297 比例
    cropped_img = img.crop((left_crop, 0, right_crop, img_height))

    # 儲存臨時裁切圖片，確保每張圖片都是不同的檔案名稱
    temp_img_path = f"temp_cropped_{img_file}"
    cropped_img.save(temp_img_path)

    # 設定 PDF 頁面的大小與裁切後的圖片大小一致
    c.setPageSize((target_width, img_height))

    # 在 PDF 當前頁面上放入裁切後的圖片
    c.drawImage(temp_img_path, 0, 0, width=target_width, height=img_height)

    # 新增新的 PDF 頁面
    c.showPage()

    # 刪除臨時儲存的裁切圖片，以節省磁碟空間
    os.remove(temp_img_path)

# 儲存 PDF 檔案
c.save()

# 印出成功訊息
print(f"PDF 已成功生成：{output_pdf_path}")
