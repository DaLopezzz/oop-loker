# GET A JOB - Sequence Diagram

## Deskripsi & Prinsip Desain

**Sequence Diagram** ini memodelkan interaksi dinamis antar-objek berdasarkan urutan waktu (*time sequence*) pada sistem **GET A JOB**. Seluruh alur disusun mengikuti arsitektur berlapis (*Layered Architecture*) dan pola *Data Access Object* (DAO) yang telah ditetapkan pada rancangan sistem:

1. **Aktor (`User`, `HRD`, `AdminSistem`):** Pihak eksternal yang memicu interaksi dengan aplikasi.
2. **Presentation Layer (`:MainApp`):** Titik masuk aplikasi (`main.py`) yang menerima input pengguna dan menampilkan hasil ke layar.
3. **Service Layer (`:LamaranService`, `:VerifikasiService`):** Lapisan logika bisnis (`services/`) yang mengorkestrasi validasi aturan bisnis (BR-01 s.d. BR-17).
4. **Domain Model Layer (`:Lamaran`, `:PengajuanPerusahaan`):** Entitas OOP (`models/`) yang menjaga enkapsulasi dan integritas perubahan status objek.
5. **DAO Implementation Layer (`:*DAOImpl`):** Implementasi akses data (`dao/*_dao_impl.py`) yang menjalankan *query* SQL ke database.
6. **Database (`:MySQL`):** Penyimpanan data relasional MySQL.

> **Standar Notasi (Sub-CPMK 4):** Setiap skenario menggunakan *lifeline* berstandar UML, *activation bar* untuk menandai masa aktif eksekusi proses, penomoran pesan berurutan dari atas ke bawah, serta *combined fragment* **`alt`** untuk memodelkan percabangan kondisi berhasil dan gagal secara jelas dan mudah dibaca.

---

## Skenario 1: Pengajuan Lamaran Pekerjaan oleh User

### Alur Singkat
1. **User** memilih lowongan yang diminati dan menekan menu pengiriman lamaran melalui `:MainApp`.
2. `:MainApp` meneruskan permintaan ke `:LamaranService`.
3. `:LamaranService` menjalankan 3 pemeriksaan berurutan sesuai aturan bisnis:
   * Kelengkapan berkas CV pada profil `User` (**BR-11**).
   * Status lowongan masih `TERBUKA` melalui `:LowonganDAOImpl` (**BR-10**).
   * User belum pernah melamar pada lowongan yang sama melalui `:LamaranDAOImpl` (**BR-12**).
4. Jika seluruh validasi terpenuhi (`[Validasi Berhasil]`), sistem membuat objek `Lamaran` dengan status awal `MENUNGGU_REVIEW` (**BR-13**) dan menyimpannya ke `:MySQL`. Jika salah satu syarat tidak terpenuhi (`[Validasi Gagal]`), sistem menolak pengajuan dan menampilkan pesan kegagalan.

### Kode PlantUML (Skenario 1)

Salin kode berikut ke **draw.io** melalui menu **Arrange > Insert > Advanced > PlantUML**:

```plantuml
@startuml
skinparam shadowing false
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true
skinparam participant {
    BackgroundColor #F8FAFC
    BorderColor #334155
}

title Sequence Diagram 1 - Pengajuan Lamaran Pekerjaan (User)
autonumber

actor "User" as user
participant ":MainApp" as ui
participant ":LamaranService" as service
participant ":LowonganDAOImpl" as lokerDao
participant ":LamaranDAOImpl" as lamaranDao
database ":MySQL" as db

user -> ui : pilih_dan_lamar(id_lowongan)
activate ui

ui -> service : ajukan_lamaran(user, id_lowongan)
activate service

service -> service : cek_cv_tersedia(user.cv_path)

service -> lokerDao : find_by_id(id_lowongan)
activate lokerDao
lokerDao -> db : SELECT * FROM lowongan WHERE id = ?
activate db
db --> lokerDao : data_lowongan
deactivate db
lokerDao --> service : lowongan
deactivate lokerDao

service -> lamaranDao : cek_sudah_melamar(user.id_pengguna, id_lowongan)
activate lamaranDao
lamaranDao -> db : SELECT COUNT(*) FROM lamaran WHERE id_user = ? AND id_lowongan = ?
activate db
db --> lamaranDao : jumlah_riwayat
deactivate db
lamaranDao --> service : sudah_melamar (bool)
deactivate lamaranDao

alt Validasi Berhasil [CV Ada & Lowongan TERBUKA & Belum Pernah Melamar]
    service -> service : buat_objek_lamaran(user, lowongan, status=MENUNGGU_REVIEW)
    service -> lamaranDao : insert(lamaran)
    activate lamaranDao
    lamaranDao -> db : INSERT INTO lamaran (...) VALUES (...)
    activate db
    db --> lamaranDao : status_sukses
    deactivate db
    lamaranDao --> service : True
    deactivate lamaranDao
    service --> ui : hasil(True, "Lamaran terkirim (Menunggu Review)")
    ui --> user : tampilkan_pesan_sukses()
else Validasi Gagal [CV Kosong / Lowongan Ditutup / Sudah Melamar]
    service --> ui : hasil(False, pesan_alasan_gagal)
    ui --> user : tampilkan_pesan_error(pesan_alasan_gagal)
end

deactivate service
deactivate ui
@enduml
```

---

## Skenario 2: Seleksi & Keputusan Status Lamaran oleh HRD

### Alur Singkat
1. **HRD** meninjau detail lamaran dan CV pelamar, lalu menetapkan keputusan akhir (`DITERIMA` atau `DITOLAK`) beserta catatan evaluasi melalui `:MainApp`.
2. `:MainApp` memanggil `:LamaranService` untuk memproses keputusan tersebut.
3. `:LamaranService` mengambil objek `Lamaran` dari database melalui `:LamaranDAOImpl` dan memverifikasi bahwa lowongan tersebut memang milik perusahaan tempat HRD bekerja (**BR-08**) serta status lamaran masih `MENUNGGU_REVIEW`.
4. Jika valid (`[Status Masih MENUNGGU_REVIEW]`), service memanggil *method* terenkapsulasi `ubah_status()` pada entitas `:Lamaran`, lalu memperbarui data di `:MySQL` (**BR-14**).
5. Jika status lamaran sudah final (`DITERIMA` atau `DITOLAK`), sistem menolak perubahan karena keputusan akhir tidak dapat diubah kembali (**BR-15**).

### Kode PlantUML (Skenario 2)

Salin kode berikut ke **draw.io** melalui menu **Arrange > Insert > Advanced > PlantUML**:

```plantuml
@startuml
skinparam shadowing false
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true
skinparam participant {
    BackgroundColor #F8FAFC
    BorderColor #334155
}

title Sequence Diagram 2 - Seleksi & Keputusan Lamaran (HRD)
autonumber

actor "HRD" as hrd
participant ":MainApp" as ui
participant ":LamaranService" as service
participant ":Lamaran" as lamaran
participant ":LamaranDAOImpl" as lamaranDao
database ":MySQL" as db

hrd -> ui : input_keputusan_lamaran(id_lamaran, status_baru, catatan)
activate ui

ui -> service : proses_keputusan(hrd, id_lamaran, status_baru, catatan)
activate service

service -> lamaranDao : find_by_id(id_lamaran)
activate lamaranDao
lamaranDao -> db : SELECT * FROM lamaran WHERE id = ?
activate db
db --> lamaranDao : baris_lamaran
deactivate db
lamaranDao --> service : lamaran
deactivate lamaranDao

service -> service : validasi_wewenang_dan_status(hrd, lamaran)

alt Valid [Perusahaan Sesuai & Status == MENUNGGU_REVIEW]
    service -> lamaran : ubah_status(status_baru, catatan)
    activate lamaran
    lamaran --> service : status_terbarui
    deactivate lamaran

    service -> lamaranDao : update_status(lamaran)
    activate lamaranDao
    lamaranDao -> db : UPDATE lamaran SET status = ?, catatan_hrd = ? WHERE id = ?
    activate db
    db --> lamaranDao : status_sukses
    deactivate db
    lamaranDao --> service : True
    deactivate lamaranDao

    service --> ui : hasil(True, "Keputusan lamaran berhasil disimpan")
    ui --> hrd : tampilkan_pesan_sukses()
else Tidak Valid [Status Sudah Final / Akses Ditolak]
    service --> ui : hasil(False, "Status akhir tidak dapat diubah kembali")
    ui --> hrd : tampilkan_pesan_error()
end

deactivate service
deactivate ui
@enduml
```

---

## Skenario 3: Verifikasi Pengajuan Perusahaan oleh AdminSistem

### Alur Singkat
1. **AdminSistem** memeriksa detail berkas pengajuan pendaftaran perusahaan yang masuk dan menentukan keputusan (`disetujui = True` atau `False`) melalui `:MainApp`.
2. `:MainApp` meneruskan keputusan ke `:VerifikasiService`.
3. `:VerifikasiService` mengambil objek `PengajuanPerusahaan` melalui `:PerusahaanDAOImpl`.
4. Jika disetujui (`[Pengajuan Disetujui]`):
   * Entitas `:PengajuanPerusahaan` mengeksekusi `setujui(admin_sistem)` yang menghasilkan objek entitas `Perusahaan` baru.
   * `:PerusahaanDAOImpl` menyimpan data `Perusahaan` baru dan mengubah status pengajuan menjadi `DISETUJUI` di `:MySQL`.
   * `:PenggunaDAOImpl` memperbarui *role* akun pemohon dari `User` menjadi `AdminPerusahaan` (**BR-03, BR-04, BR-05**) tanpa menghapus riwayat lamaran sebelumnya (**BR-17**).
5. Jika ditolak (`[Pengajuan Ditolak]`):
   * Entitas `:PengajuanPerusahaan` mengeksekusi `tolak(admin_sistem, alasan)` dan menyimpan status `DITOLAK` ke `:MySQL` (akun pemohon tetap berstatus `User`).

### Kode PlantUML (Skenario 3)

Salin kode berikut ke **draw.io** melalui menu **Arrange > Insert > Advanced > PlantUML**:

```plantuml
@startuml
skinparam shadowing false
skinparam sequenceMessageAlign center
skinparam responseMessageBelowArrow true
skinparam participant {
    BackgroundColor #F8FAFC
    BorderColor #334155
}

title Sequence Diagram 3 - Verifikasi Pengajuan Perusahaan (AdminSistem)
autonumber

actor "AdminSistem" as admin
participant ":MainApp" as ui
participant ":VerifikasiService" as service
participant ":PengajuanPerusahaan" as pengajuan
participant ":PerusahaanDAOImpl" as ptDao
participant ":PenggunaDAOImpl" as userDao
database ":MySQL" as db

admin -> ui : verifikasi_pengajuan(id_pengajuan, disetujui, alasan)
activate ui

ui -> service : proses_verifikasi(admin, id_pengajuan, disetujui, alasan)
activate service

service -> ptDao : find_pengajuan_by_id(id_pengajuan)
activate ptDao
ptDao -> db : SELECT * FROM pengajuan_perusahaan WHERE id = ?
activate db
db --> ptDao : data_pengajuan
deactivate db
ptDao --> service : pengajuan
deactivate ptDao

alt Pengajuan Disetujui [disetujui == True]
    service -> pengajuan : setujui(admin)
    activate pengajuan
    pengajuan --> service : perusahaan_baru
    deactivate pengajuan

    service -> ptDao : simpan_perusahaan_dan_pengajuan(perusahaan_baru, pengajuan)
    activate ptDao
    ptDao -> db : INSERT INTO perusahaan (...) & UPDATE pengajuan_perusahaan
    activate db
    db --> ptDao : status_sukses
    deactivate db
    ptDao --> service : True
    deactivate ptDao

    service -> userDao : update_role(pengajuan.pemohon.id_pengguna, "ADMIN_PERUSAHAAN")
    activate userDao
    userDao -> db : UPDATE pengguna SET role = 'ADMIN_PERUSAHAAN' WHERE id = ?
    activate db
    db --> userDao : status_sukses
    deactivate db
    userDao --> service : True
    deactivate userDao

    service --> ui : hasil(True, "Perusahaan disetujui & role pemohon diperbarui")
    ui --> admin : tampilkan_pesan_sukses()
else Pengajuan Ditolak [disetujui == False]
    service -> pengajuan : tolak(admin, alasan)
    activate pengajuan
    pengajuan --> service : status_ditolak
    deactivate pengajuan

    service -> ptDao : update_status_pengajuan(pengajuan)
    activate ptDao
    ptDao -> db : UPDATE pengajuan_perusahaan SET status = 'DITOLAK', alasan = ?
    activate db
    db --> ptDao : status_sukses
    deactivate db
    ptDao --> service : True
    deactivate ptDao

    service --> ui : hasil(True, "Pengajuan perusahaan ditolak")
    ui --> admin : tampilkan_pesan_info()
end

deactivate service
deactivate ui
@enduml
```