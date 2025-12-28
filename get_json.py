import requests
import datetime
import json

# URL پایه
base_url_tala = "https://api.tgju.org/v1/market/indicator/summary-table-data/geram18" #طلای ۱۸ عیار
base_url_sekee = "https://api.tgju.org/v1/market/indicator/summary-table-data/gerami" # سکه گرمی

# هدرهای شبیه‌سازی مرورگر
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
}

# تابع برای ارسال درخواست
def fetch_data(start_date, end_date):
    params = {
        "lang": "fa",
        "order_dir": "asc",
        "start": 0,
        "length": 30,
        "convert_to_ad": 1,
        "from": start_date,  # تاریخ شروع
        "to": end_date,      # تاریخ پایان
    }

    response_tala = requests.get(base_url_tala, params=params, headers=headers)
    response_sekee = requests.get(base_url_sekee, params=params, headers=headers)

    # بررسی وضعیت پاسخ و ذخیره داده‌ها در فایل
    if response_sekee.status_code == 200 and response_sekee.status_code == 200:
        data_tala = response_tala.json()
        data_sekee = response_sekee.json()

        # ذخیره داده‌ها در فایل
        with open("data.json", "a") as f:
            f.write(json.dumps({"date_range": f"{start_date} - {end_date}", "tala": data_tala, "sekee": data_sekee}) + "\n")
        print(f"داده‌ها برای بازه {start_date} - {end_date} ذخیره شد.")
    else:
        print(f"خطا در دریافت داده‌ها: {response_tala.status_code}, {response_sekee.status_code}")

# تنظیم تاریخ شروع و پایان
start_date = "1403/12/01"  # تاریخ شروع
end_date = "1404/10/8"    # تاریخ پایان

# تبدیل تاریخ‌ها به فرمت datetime
start_datetime = datetime.datetime.strptime(start_date, "%Y/%m/%d")
end_datetime = datetime.datetime.strptime(end_date, "%Y/%m/%d")

# ارسال درخواست‌ها هر 30 روز
current_date = start_datetime
while current_date < end_datetime:
    next_date = current_date + datetime.timedelta(days=30)  # اضافه کردن 30 روز
    fetch_data(current_date.strftime("%Y/%m/%d"), next_date.strftime("%Y/%m/%d"))
    current_date = next_date  # به روزرسانی تاریخ فعلی
