from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
from models import save_kurs_data
from db import get_connection

import requests
import threading
import time

app = Flask(__name__)

def scrape_kurs_bi():
    url = "https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Tidak dapat mengakses {url}, status code {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    kurs_data = []
    
    # Temukan tabel yang sesuai (ubah jika perlu)
    table = soup.find("table")  
    if table:
        for row in table.find_all("tr")[1:]:  # Lewati header tabel
            cols = row.find_all("td")
            if len(cols) >= 4:
                try:
                    mata_uang   = cols[0].get_text(strip=True)
                    beli        = float(cols[1].get_text(strip=True).replace(",", ""))
                    jual        = float(cols[2].get_text(strip=True).replace(",", ""))
                    tengah      = float(cols[3].get_text(strip=True).replace(",", ""))
                    
                    kurs_data.append({
                        "mata_uang": mata_uang,
                        "beli": beli,
                        "jual": jual,
                        "tengah": tengah,
                        "sumber": "BI"
                    })
                except ValueError:
                    print(f"Peringatan: Format angka tidak sesuai untuk {mata_uang}")
    
    if kurs_data:
        save_kurs_data(kurs_data)
    else:
        print("Peringatan: Tidak ada data kurs yang ditemukan.")


#def run_scheduler():
    #schedule.every().day.at("21:28").do(scrape_kurs_bi)
    #schedule.every().day.at("21:30").do(scrape_kurs_bi)

   #print("Scheduler aktif, menunggu eksekusi pada pukul 09:00 dan 10:00 setiap hari...")

    #while True:
        #schedule.run_pending()
        #time.sleep(60)

       
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT TOP 20 mata_uang, beli, jual, tengah, tanggal FROM kurs ORDER BY tanggal DESC")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        print(f"Error database: {e}")
        data = []
    finally:
        cursor.close()
        conn.close()
    
    return jsonify(data)

# Mulai background thread
threading.Thread(target=scrape_kurs_bi, daemon=True).start()

#Menjalankan scheduler dalam background thread (Opsional)
#threading.Thread(target=run_scheduler, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    #scrape_kurs_bi()