import pandas as pd
from datetime import datetime

# --- 1. โครงสร้างข้อมูลเบื้องต้น (ใช้ Pandas DataFrame จำลองฐานข้อมูล) ---
def initialize_inventory():
    data = {
        'ชื่อสินค้า': ['ปากกา A', 'สมุด B', 'หมึกพิมพ์ C'],
        'หมวดหมู่': ['เครื่องเขียน', 'เครื่องเขียน', 'สำนักงาน'],
        'หน่วย': ['ด้าม', 'เล่ม', 'ขวด'],
        'ตั้งต้น': [100, 50, 20],
        'รับเข้า': [10, 5, 2],
        'ใช้': [2, 1, 0],         # เบิกใช้ภายใน (ตัวเลขที่กรอก/คำนวณ)
        'ขาย/POS': [15, 8, 3],    # ยอดขาย
        'คงเหลือ': [0, 0, 0],     # จะถูกคำนวณอัตโนมัติ
        'หมายเหตุ': ['-', '-', '-']
    }
    df = pd.DataFrame(data)
    return df

# --- 2. ฟังก์ชันคำนวณสต๊อกอัตโนมัติ ---
def calculate_stock(df):
    """คำนวณ 'คงเหลือ' = ตั้งต้น + รับเข้า - ใช้ - ขาย/POS"""
    df['คงเหลือ'] = df['ตั้งต้น'] + df['รับเข้า'] - df['ใช้'] - df['ขาย/POS']
    return df

# --- 3. ฟังก์ชันเพิ่มสินค้าใหม่ ---
def add_product(df, name, category, unit, initial_stock, note='-'):
    new_product = pd.DataFrame([{
        'ชื่อสินค้า': name, 
        'หมวดหมู่': category, 
        'หน่วย': unit, 
        'ตั้งต้น': initial_stock,
        'รับเข้า': 0,
        'ใช้': 0,
        'ขาย/POS': 0,
        'คงเหลือ': initial_stock,
        'หมายเหตุ': note
    }])
    df = pd.concat([df, new_product], ignore_index=True)
    print(f"\n>> เพิ่มสินค้า '{name}' เรียบร้อยแล้ว")
    return df

# --- 4. ฟังก์ชันจำลองการสร้างรายงาน PDF (ต้องใช้ไลบรารีอื่น ๆ สำหรับการสร้าง PDF จริง) ---
def generate_pdf_report_simulation(df, branch_name, staff_name, staff_id):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ใช้งานจริงต้องติดตั้งไลบรารี PDF เช่น reportlab หรือ fpdf2
    
    print("\n" + "="*70)
    print(f"** รายงานสต๊อกสินค้า **")
    print(f"สาขา: {branch_name} | วันที่: {date_now}")
    print(f"พนักงาน: {staff_name} (ID: {staff_id})")
    print("="*70)
    
    # จำลองการแสดงผลข้อมูล
    print(df.to_string())
    
    print("="*70)
    print("... (จำลองการสร้างไฟล์ PDF เสร็จสมบูรณ์) ...")
    
# --- 5. ตัวอย่างการใช้งาน (Mock App Flow) ---
if __name__ == "__main__":
    
    # 1. ข้อมูลการล็อกอิน/สาขา (ตั้งเองได้)
    BRANCH_NAME = "สาขาพระราม 9"
    STAFF_NAME = "อารยา ศรีสุข"
    STAFF_ID = "AR001"
    
    # 2. เริ่มต้นฐานข้อมูล
    inventory_df = initialize_inventory()
    
    # 3. เพิ่มรายการสินค้าใหม่
    inventory_df = add_product(inventory_df, 'กระดาษ A4', 'สำนักงาน', 'รีม', 50)
    
    # 4. คำนวณสต๊อกสินค้าทั้งหมด
    inventory_df = calculate_stock(inventory_df)
    
    # 5. แสดงผล (จำลองการสร้างรายงาน)
    generate_pdf_report_simulation(inventory_df, BRANCH_NAME, STAFF_NAME, STAFF_ID)
