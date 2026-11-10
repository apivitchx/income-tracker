print("โปรแกรมรายรับ-รายจ่าย v1.0")

def add_income(amount, note):
    print(f"รายรับ: {amount} บาท ({note})")

add_income(1000, "เงินเดือน")

def summary(income, expense):
    print(f"สรุป: รายรับ {income} รายจ่าย {expense} คงเหลือ {income - expense}")