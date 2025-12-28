import json
import plotly.graph_objects as go
from datetime import datetime

# خواندن داده‌ها از فایل JSON
with open("output.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# آماده‌سازی داده‌ها
dates = []
ratios = []

# استخراج تاریخ‌ها و نسبت‌ها از داده‌ها
for line in data:
    for entry in line:
        dates.append(datetime.strptime(entry["date_gregorian"], "%Y/%m/%d"))  # تبدیل تاریخ میلادی به datetime
        ratios.append(entry["ratio"])

# ساخت نمودار با استفاده از Plotly
fig = go.Figure()

# اضافه کردن داده‌ها به نمودار
fig.add_trace(go.Scatter(
    x=dates,
    y=ratios,
    mode='lines+markers',  # نمایش خط و نقاط
    name='Ratio',  # نام داده
    line=dict(color='blue'),  # رنگ خط
    marker=dict(color='red', size=5)  # رنگ و اندازه نقاط
))

# تنظیمات نمودار
fig.update_layout(
    title="نسبت ربع سکه به طلا بر اساس تاریخ",
    xaxis_title="تاریخ",
    yaxis_title="نسبت (Ratio)",
    xaxis=dict(
        tickformat="%Y/%m/%d",  # فرمت تاریخ
        tickangle=45,  # چرخاندن تاریخ‌ها
    ),
    plot_bgcolor='white',  # رنگ پس‌زمینه نمودار
    paper_bgcolor='white',  # رنگ پس‌زمینه صفحه
    showlegend=True  # نمایش legend
)

# نمایش نمودار
fig.show()

# ذخیره نمودار به صورت HTML
fig.write_html("chart_tradingview_style.html")
