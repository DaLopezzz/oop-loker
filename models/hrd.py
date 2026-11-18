from __future__ import annotations

from typing import TYPE_CHECKING

from models.pengguna import Pengguna

if TYPE_CHECKING:
    from models.enums import StatusLamaran
    from models.lamaran import Lamaran
    from models.lowongan import Lowongan
    from models.perusahaan import Perusahaan


class HRD(Pengguna):
    def __init__(
        self,
        id_pengguna: int,
        nama: str,
        email: str,
        password_hash: str,
        perusahaan: Perusahaan,
        jabatan: str,
        status_aktif: bool = True,
    ) -> None:
        pass

    @property
    def perusahaan(self) -> Perusahaan:
        pass

    @property
    def jabatan(self) -> str:
        pass

    @jabatan.setter
    def jabatan(self, nilai: str) -> None:
        pass

    def buat_lowongan(
        self,
        posisi: str,
        deskripsi: str,
        persyaratan: str,
        lokasi: str,
        gaji_min: float,
        gaji_max: float,
    ) -> Lowongan:
        pass

    def ubah_lowongan(
        self,
        lowongan: Lowongan,
        posisi: str,
        deskripsi: str,
        persyaratan: str,
        lokasi: str,
        gaji_min: float,
        gaji_max: float,
    ) -> None:
        pass

    def buka_lowongan(self, lowongan: Lowongan) -> None:
        pass

    def tutup_lowongan(self, lowongan: Lowongan) -> None:
        pass

    def review_lamaran(self, lamaran: Lamaran) -> dict:
        pass

    def putuskan_status(
        self, lamaran: Lamaran, status: StatusLamaran, catatan: str
    ) -> None:
        pass

    def get_role(self) -> str:
        pass

    def tampilkan_dashboard(self) -> None:
        pass
