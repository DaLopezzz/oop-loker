from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from models.enums import StatusLowongan

if TYPE_CHECKING:
    from models.hrd import HRD
    from models.perusahaan import Perusahaan


class Lowongan:
    def __init__(
        self,
        id_lowongan: int,
        perusahaan: Perusahaan,
        dibuat_oleh: HRD,
        posisi: str,
        deskripsi: str,
        persyaratan: str,
        lokasi: str,
        gaji_min: float,
        gaji_max: float,
        status: StatusLowongan = StatusLowongan.DRAFT,
        tanggal_dibuat: Optional[datetime] = None,
        tanggal_tutup: Optional[datetime] = None,
    ) -> None:
        pass

    @property
    def id_lowongan(self) -> int:
        pass

    @property
    def perusahaan(self) -> Perusahaan:
        pass

    @property
    def dibuat_oleh(self) -> HRD:
        pass

    @property
    def posisi(self) -> str:
        pass

    @posisi.setter
    def posisi(self, nilai: str) -> None:
        pass

    @property
    def deskripsi(self) -> str:
        pass

    @deskripsi.setter
    def deskripsi(self, nilai: str) -> None:
        pass

    @property
    def persyaratan(self) -> str:
        pass

    @persyaratan.setter
    def persyaratan(self, nilai: str) -> None:
        pass

    @property
    def lokasi(self) -> str:
        pass

    @lokasi.setter
    def lokasi(self, nilai: str) -> None:
        pass

    @property
    def gaji_min(self) -> float:
        pass

    @gaji_min.setter
    def gaji_min(self, nilai: float) -> None:
        pass

    @property
    def gaji_max(self) -> float:
        pass

    @gaji_max.setter
    def gaji_max(self, nilai: float) -> None:
        pass

    @property
    def status(self) -> StatusLowongan:
        pass

    @property
    def tanggal_dibuat(self) -> datetime:
        pass

    @property
    def tanggal_tutup(self) -> Optional[datetime]:
        pass

    def ubah_detail(
        self,
        posisi: str,
        deskripsi: str,
        persyaratan: str,
        lokasi: str,
        gaji_min: float,
        gaji_max: float,
    ) -> None:
        pass

    def buka(self) -> None:
        pass

    def tutup(self) -> None:
        pass

    def sesuai_kriteria(self, kriteria: str) -> bool:
        pass
