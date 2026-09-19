import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("🚀 Memulai verifikasi otomatis untuk Endpoint Tiket (T2)...")
    
    payload_valid = {
        "kode_tiket": "EVT-9999",
        "kuota": 50,
        "nama_event": "Konser Musik Akhir Tahun"
    }
    response = requests.post(f"{BASE_URL}/api/tiket", json=payload_valid)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    print("✅ [PASS] POST /api/tiket berhasil (Status 201)")
    
    assert "location" in response.headers, "Header 'Location' tidak ditemukan!"
    print("✅ [PASS] Header Location ada")

    payload_invalid = {
        "kode_tiket": "SALAH-FORMAT",
        "kuota": 0,                     
        "nama_event": "Event Gagal"
    }
    response_invalid = requests.post(f"{BASE_URL}/api/tiket", json=payload_invalid)
    assert response_invalid.status_code == 422, f"Expected 422, got {response_invalid.status_code}"
    print("✅ [PASS] Validasi Pydantic /api/tiket gagal dengan benar (Status 422)")

    response_get = requests.get(f"{BASE_URL}/api/tiket?skip=0&limit=5&search=Konser")
    assert response_get.status_code == 200, f"Expected 200, got {response_get.status_code}"
    print("✅ [PASS] GET /api/tiket berhasil (Status 200)")

    response_404 = requests.get(f"{BASE_URL}/api/tiket/99999")
    assert response_404.status_code == 404, f"Expected 404, got {response_404.status_code}"
    print("✅ [PASS] GET /api/tiket/{id} mengembalikan 404 jika ID tidak ada")

    print("\n🎉 SEMUA PENGUJIAN BERHASIL (PASS)! 🎉")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Server FastAPI belum menyala! Jalankan 'uvicorn main:app --reload' terlebih dahulu.")
        sys.exit(1)
    except AssertionError as e:
        print(f"❌ TEST GAGAL: {e}")
        sys.exit(1)