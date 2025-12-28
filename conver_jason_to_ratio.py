import json

# تابعی برای محاسبه میانگین بزرگترین و کوچکترین اعداد
def calculate_average(values):
    max_val = max(values)
    min_val = min(values)
    return (max_val + min_val) / 2

# خواندن فایل JSON
with open("data.json", "r", encoding="utf-8") as file:
    lines = file.readlines()

result = []

# پردازش هر خط فایل
for line in lines:
    data = json.loads(line.strip())  # تبدیل خط به دیکشنری

    # استخراج داده‌ها
    tala_data = data["tala"]["data"]
    sekee_data = data["sekee"]["data"]

    # لیستی برای ذخیره نتایج
    final_data = []

    # ✅ گرفتن مینیمم طول طلا و سکه
    min_length = min(len(tala_data), len(sekee_data))

    for i in range(min_length):
        # داده‌های طلا
        tala_values = tala_data[i][:4]
        tala_values = [int(val.replace(",", "")) for val in tala_values]
        tala_avg = calculate_average(tala_values)

        # داده‌های سکه
        sekee_values = sekee_data[i][:4]
        sekee_values = [int(val.replace(",", "")) for val in sekee_values]
        sekee_avg = calculate_average(sekee_values)

        # تاریخ‌ها
        date_gregorian = tala_data[i][6]
        date_shamsi = tala_data[i][7]

        # محاسبه نسبت میانگین سکه به طلا
        ratio = sekee_avg / tala_avg if tala_avg != 0 else 0

        # افزودن داده‌ها به لیست نهایی
        final_data.append({
            "date_gregorian": date_gregorian,
            "date_shamsi": date_shamsi,
            "tala_avg": tala_avg,
            "rob_zir": sekee_avg,
            "ratio": ratio
        })

    # افزودن داده‌ها به لیست نتایج کلی
    result.append(final_data)

# نوشتن نتایج به فایل خروجی
with open("output.json", "w", encoding="utf-8") as output_file:
    json.dump(result, output_file, ensure_ascii=False, indent=4)

print("عملیات با موفقیت انجام شد.")
