from enum import Enum


class StatusVerifikasi(Enum):
    DIAJUKAN = "DIAJUKAN"
    DISETUJUI = "DISETUJUI"
    DITOLAK = "DITOLAK"


class StatusLowongan(Enum):
    DRAFT = "DRAFT"
    TERBUKA = "TERBUKA"
    DITUTUP = "DITUTUP"


class StatusLamaran(Enum):
    MENUNGGU_REVIEW = "MENUNGGU_REVIEW"
    DITERIMA = "DITERIMA"
    DITOLAK = "DITOLAK"


class StatusPengajuan(Enum):
    DIAJUKAN = "DIAJUKAN"
    DISETUJUI = "DISETUJUI"
    DITOLAK = "DITOLAK"
