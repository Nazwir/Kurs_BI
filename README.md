Repositori ini dibuat untuk mengembangkan project Kurs Bank Indonesia. Repositori ini dikembangkan dengan bahasa pemrograman Python dan database SQL Server dengan menggunakan teknik Web Scraping dan dijalankan dengan 2 opsi melalui request dan Task Scheduler.

Instalasi yang Diperlukan:
Sebelum menjalankan kode ini, pastikan Anda telah menginstal:
1. Driver ODBC untuk SQL Server (biasanya "ODBC Driver 17 for SQL Server")
2. Library pyodbc: pip install pyodbc

Database
1. Ganti YOUR DRIVER, SEERVER, DATABASE, USERNAME, PASSWORD dengan kredensial SQL Server Anda.
2. Pastikan SQL Server Anda mengizinkan koneksi dari aplikasi Anda (firewall, authentication, dll.)
3. Untuk environment production, pertimbangkan untuk menggunakan connection pooling atau menyimpan konfigurasi database di environment variable.
