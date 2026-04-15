import yfinance as yf
import pandas as pd
from datetime import datetime

# 1. Danh sách 10 mã cổ phiếu lớn tại Nhật Bản
# .T là ký hiệu cho sàn Tokyo
tickers = [
    '7203.T', '9984.T', '6758.T', '9432.T', '6098.T',
    '8306.T', '8031.T', '4568.T', '6501.T', '6723.T'
]

print("Đang lấy dữ liệu từ Yahoo Finance... Vui lòng đợi.")

final_data = []

for symbol in tickers:
    try:
        # Lấy dữ liệu cổ phiếu
        stock = yf.Ticker(symbol)
        info = stock.fast_info
        
        # Trích xuất thông tin
        data = {
            "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Mã": symbol,
            "Giá hiện tại (Yên)": round(info['last_price'], 2),
            "Vốn hóa": f"{round(info['market_cap']/1e12, 2)} Nghìn tỷ"
        }
        final_data.append(data)
        print(f"Đã lấy xong: {symbol} - Giá: {data['Giá hiện tại (Yên)']}")
        
    except Exception as e:
        print(f"Lỗi khi lấy mã {symbol}: {e}")

# 2. Lưu tất cả vào file Excel
df = pd.DataFrame(final_data)
df.to_excel("top_10_chung_khoan_jp.xlsx", index=False)

print("\n--- HOÀN THÀNH ---")
print("Kết quả đã được lưu vào file: top_10_chung_khoan_jp.xlsx")
import matplotlib.pyplot as plt
import seaborn as sns

# 3. Vẽ biểu đồ so sánh giá
print("Đang khởi tạo biểu đồ...")
plt.figure(figsize=(12, 7)) # Kích thước biểu đồ
sns.set_style("whitegrid")

# Tạo biểu đồ cột
ax = sns.barplot(x="Mã", y="Giá hiện tại (Yên)", data=df, palette="viridis")

# Thêm tiêu đề và nhãn
plt.title("So sánh giá 10 mã cổ phiếu lớn nhất Nhật Bản", fontsize=16)
plt.xlabel("Mã cổ phiếu", fontsize=12)
plt.ylabel("Giá (Yên)", fontsize=12)

# Hiển thị số liệu trên đầu mỗi cột
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')

# Lưu biểu đồ thành file ảnh
plt.savefig("bieu_do_gia_jp.png")
print("Đã lưu biểu đồ vào file: bieu_do_gia_jp.png")

# Hiển thị biểu đồ lên màn hình
plt.show()
