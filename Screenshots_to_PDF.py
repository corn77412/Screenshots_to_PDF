# 按 Win + PrtScn，這樣會螢幕截圖並自動保存為PNG檔案，並儲存在"C:/Users/178418/Pictures/Screenshots/"。
#執行程式碼後，PDF檔會出現在與程式碼相同的資料夾。
import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from io import BytesIO

# 設定圖片來源資料夾
img_folder = "C:/Users/178418/Pictures/Screenshots/"  # 來源資料夾，存放 16:9 的截圖圖片
output_pdf_path = "output.pdf"  # 生成的 PDF 檔案名稱

# A4 紙張尺寸 (毫米)
a4_width_mm = 210
a4_height_mm = 297

# 讀取所有 PNG 圖片，並按照名稱排序
image_files = sorted([f for f in os.listdir(img_folder) if f.endswith(".png")])

# 如果資料夾內沒有找到 PNG 圖片，則結束程式
if not image_files:
    print("未找到任何 PNG 圖片，請確認圖片目錄是否正確。")
    exit()

# 創建 PDF 檔案，並設定頁面大小為 A4
c = canvas.Canvas(output_pdf_path)
c.setPageSize((a4_width_mm * mm, a4_height_mm * mm))

# 遍歷資料夾內的所有圖片，並逐一處理
for img_file in image_files:
    img_path = os.path.join(img_folder, img_file)  # 獲取圖片完整路徑

    try:
        # 開啟圖片
        img = Image.open(img_path)
        img_width, img_height = img.size  # 取得圖片的原始寬度與高度

        # 計算目標寬度，使其符合 A4 的直式比例 (210:297)
        target_width = int(img_height * a4_width_mm / a4_height_mm)

        # 計算左右兩側需要裁切的範圍
        left_crop = (img_width - target_width) // 2
        right_crop = left_crop + target_width

        # 執行裁切
        cropped_img = img.crop((left_crop, 0, right_crop, img_height))

        # 計算圖片在 PDF 頁面上的縮放比例，使其寬度適應 A4 寬度
        scale_factor = (a4_width_mm * mm) / cropped_img.width

        # 計算縮放後的圖片高度
        scaled_height = cropped_img.height * scale_factor

        # 將 PIL Image 物件轉換為 ReportLab 可繪製的格式
        img_buffer = BytesIO()
        cropped_img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        reportlab_img = ImageReader(img_buffer)

        # 將 ReportLab 的圖片物件繪製到 PDF 頁面的中央 (垂直置中)
        x_position = 0
        y_position = (a4_height_mm * mm - scaled_height) / 2

        c.drawImage(reportlab_img, x_position, y_position, width=a4_width_mm * mm, height=scaled_height)

        # 新增新的 PDF 頁面
        c.showPage()

    except FileNotFoundError:
        print(f"錯誤：找不到圖片檔案 {img_path}")
    except Exception as e:
        print(f"處理圖片 {img_file} 時發生錯誤：{e}")

# 儲存 PDF 檔案
c.save()

# 印出成功訊息
print(f"PDF 已成功生成：{output_pdf_path}")
