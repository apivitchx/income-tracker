def summary(income, expense):
    net = income - expense
    if net >= 0:
        print(f"สรุป: รายรับ {income} รายจ่าย {expense}")
        print(f"คงเหลือ: +{net} บาท ✓")
    else:
        print(f"สรุป: รายรับ {income} รายจ่าย {expense}")
        print(f"ขาดทุน: {net} บาท ✗")