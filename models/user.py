from __future__ import annotations

from typing import TYPE_CHECKING

from models.pengguna import Pengguna

if TYPE_CHECKING:
    from models.lamaran import Lamaran
    from models.lowongan import Lowongan
    from models.pengajuan_perusahaan import PengajuanPerusahaan


class User(Pengguna):
    def __init__(
        self,
        id_pengguna: int,
        nama: str,
        email: str,
        password_hash: str,
        nomor_telepon: str = "",
        alamat: str = "",
        cv_path: str = "",
        status_aktif: bool = True,
    ) -> None:
        pass

    @property
    def nomor_telepon(self) -> str:
        pass

    @nomor_telepon.setter
    def nomor_telepon(self, nilai: str) -> None:
        pass

    @property
    def alamat(self) -> str:
        pass

    @alamat.setter
    def alamat(self, nilai: str) -> None:
        pass

    @property
    def cv_path(self) -> str:
        pass

    @cv_path.setter
    def cv_path(self, nilai: str) -> None:
        pass

    def unggah_cv(self, path: str) -> None:
        pass

    def cari_lowongan(self, kriteria: str) -> list[Lowongan]:
        pass

    def kirim_lamaran(self, lowongan: Lowongan) -> Lamaran:
        pass

    def pantau_lamaran(self) -> list[Lamaran]:
        pass

    def ajukan_perusahaan(
        self, nama: str, alamat: str, email: str, deskripsi: str
    ) -> PengajuanPerusahaan:
        pass

    def get_role(self) -> str:
        pass

    def tampilkan_dashboard(self) -> None:
        pass
