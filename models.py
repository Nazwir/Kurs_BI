from db import get_connection
from datetime import datetime

def save_kurs_data(kurs_list):
    conn = get_connection()
    cursor = conn.cursor()
    
    today = datetime.today().date()

    for kurs in kurs_list:
        try:
            cursor.execute("""
                INSERT INTO kurs (tanggal, mata_uang, beli, jual, tengah, sumber)
                VALUES (?, ?, ?, ?, ?, ?)
            """, today, kurs['mata_uang'], kurs['beli'], kurs['jual'], kurs['tengah'], kurs['sumber'])
        except Exception as e:
            print(f"Error saat menyimpan data {kurs['mata_uang']}: {e}")

    conn.commit()
    cursor.close()
    conn.close()