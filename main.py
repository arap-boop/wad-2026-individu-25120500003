from fastapi import FastAPI, HTTPException, status, Response, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="API Manajemen Tiket - WAD 2026",
    version="1.0.0",
    description="Layanan backend untuk pengelolaan tiket event perkuliahan."
)

database_tiket = []
id_counter = 1

class TiketBase(BaseModel):
    kode_tiket: str = Field(
        ..., 
        pattern=r"^EVT-\d{4}$", 
        description="Format wajib: EVT- diikuti 4 digit angka (contoh: EVT-1234)",
        examples=["EVT-5021"]
    )
    kuota: int = Field(
        ..., 
        gt=0, 
        description="Jumlah kuota tiket harus lebih besar dari 0",
        examples=[100]
    )
    nama_event: str = Field(
        ..., 
        min_length=3, 
        max_length=100, 
        description="Nama event yang diselenggarakan",
        examples=["Workshop FastAPI Modern"]
    )

class TiketCreate(TiketBase):
    pass

class TiketResponse(TiketBase):
    id: int = Field(..., examples=[1])

    class Config:
        from_attributes = True



@app.post(
    "/api/tiket", 
    response_model=TiketResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Membuat tiket baru"
)
def create_tiket(tiket_in: TiketCreate, response: Response):

    global id_counter
    
    tiket_baru = {
        "id": id_counter,
        "kode_tiket": tiket_in.kode_tiket,
        "kuota": tiket_in.kuota,
        "nama_event": tiket_in.nama_event
    }
    
    database_tiket.append(tiket_baru)
    
    response.headers["Location"] = f"/api/tiket/{id_counter}"
    
    id_counter += 1
    return tiket_baru


@app.get(
    "/api/tiket", 
    response_model=List[TiketResponse],
    status_code=status.HTTP_200_OK,
    summary="Mengambil daftar seluruh tiket"
)
def get_semua_tiket(
    skip: int = Query(0, ge=0, description="Jumlah data yang dilewati (pagination)"),
    limit: int = Query(10, ge=1, le=100, description="Maksimum data yang diambil"),
    search: Optional[str] = Query(None, description="Pencarian berdasarkan nama event atau kode tiket")
):
   
    hasil = database_tiket
    
    if search:
        search_query = search.lower()
        hasil = [
            t for t in hasil 
            if search_query in t["nama_event"].lower() or search_query in t["kode_tiket"].lower()
        ]
        
    return hasil[skip : skip + limit]


@app.get(
    "/api/tiket/{id}", 
    response_model=TiketResponse,
    status_code=status.HTTP_200_OK,
    summary="Mengambil detail tiket berdasarkan ID"
)
def get_detail_tiket(id: int):
 
    tiket = next((t for t in database_tiket if t["id"] == id), None)
    
    if not tiket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Tiket dengan ID '{id}' tidak ditemukan."
        )
        
    return tiket