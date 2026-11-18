from __future__ import annotations

from typing import TYPE_CHECKING

from models.pengguna import Pengguna

if TYPE_CHECKING:
    from models.hrd import HRD
    from models.perusahaan import Perusahaan


class AdminPerusahaan(Pengguna):
    def __init__(
        self,
        id_pengguna: int,
        nama: str,
        email: str,
        password_hash: str,
        perusahaan: Perusahaan,
        status_aktif: bool = True,
    ) -> None:
        pass

    @property
    def perusahaan(self) -> Perusahaan:
        pass

    def kelola_profil_perusahaan(
        self, nama: str, alamat: str, deskripsi: str, email: str
    ) -> None:
        pass

    def buat_akun_hrd(
        self, nama: str, email: str, password: str, jabatan: str
    ) -> HRD:
        pass

    def ubah_akun_hrd(self, hrd: HRD, jabatan: str) -> None:
        pass

    def nonaktifkan_hrd(self, hrd: HRD) -> None:
        pass

    def get_role(self) -> str:
        pass

    def tampilkan_dashboard(self) -> None:
        pass
