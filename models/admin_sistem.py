from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from models.pengguna import Pengguna

if TYPE_CHECKING:
    from models.enums import StatusVerifikasi
    from models.lowongan import Lowongan
    from models.pengajuan_perusahaan import PengajuanPerusahaan
    from models.perusahaan import Perusahaan


class AdminSistem(Pengguna):
    def __init__(
        self,
        id_pengguna: int,
        nama: str,
        email: str,
        password_hash: str,
        status_aktif: bool = True,
    ) -> None:
        pass

    def verifikasi_pengajuan(
        self, pengajuan: PengajuanPerusahaan, disetujui: bool, alasan: str
    ) -> Optional[Perusahaan]:
        pass

    def kelola_pengguna(self, pengguna: Pengguna, status_aktif: bool) -> None:
        pass

    def kelola_perusahaan(
        self, perusahaan: Perusahaan, status: StatusVerifikasi
    ) -> None:
        pass

    def pantau_lowongan_global(self) -> list[Lowongan]:
        pass

    def get_role(self) -> str:
        pass

    def tampilkan_dashboard(self) -> None:
        pass
