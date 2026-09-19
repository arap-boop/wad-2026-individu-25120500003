# 🎟️ FastAPI Endpoint - Topik Tiket (WAD 2026)

Repositori ini dibuat untuk memenuhi tugas individu pengembangan backend menggunakan **FastAPI** dengan topik **T2 | Tiket**.

## 📌 Fitur & Validasi Endpoint
Aplikasi ini menyediakan RESTful API untuk manajemen data tiket event dengan aturan validasi berikut:
* **`kode_tiket`**: Wajib menggunakan pola format `EVT-XXXX` (di mana `XXXX` adalah 4 digit angka, contoh: `EVT-9999`).
* **`kuota`**: Nilai integer yang wajib lebih besar dari 0 (`> 0`).
* **`nama_event`**: Nama event yang diselenggarakan

---

## 🚀 Daftar Endpoint (API Specs)

| Method | Endpoint | Deskripsi | Response Status |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/tiket` | Membuat data tiket baru (menyertakan header `Location`) | `201 Created` / `422 Unprocessable Entity` |
| **GET** | `/api/tiket` | Mendapatkan daftar seluruh tiket (mendukung `?skip`, `?limit`, `?search`) | `200 OK` |
| **GET** | `/api/tiket/{id}` | Mendapatkan detail tiket berdasarkan ID | `200 OK` / `404 Not Found` |

---

## 🛠️ Cara Menjalankan Proyek

1. **Clone Repository & Masuk ke Folder:**
   ```bash
   git clone [https://github.com/username-anda/wad-2026-individu-25120500003.git](https://github.com/username-anda/wad-2026-individu-25120500003.git)
   cd wad-2026-individu-25120500003