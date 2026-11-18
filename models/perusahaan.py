from __future__ import annotations

from typing import TYPE_CHECKING

from models.enums import StatusVerifikasi

if TYPE_CHECKING:
    from models.hrd import HRD
    from models.lowongan import Lowongan


class Perusahaan:
    def __init__(
        self,
        id_perusahaan: int,
        nama: str,
        alamat: str,
        deskripsi: str,
        email: str,
        status_verifikasi: StatusVerifikasi = StatusVerifikasi.DIAJUKAN,
    ) -> None:
        pass

    @property
    def id_perusahaan(self) -> int:
        pass

    @property
    def nama(self) -> str:
        pass

    @nama.setter
    def nama(self, nilai: str) -> None:
        pass

    @property
    def alamat(self) -> str:
        pass

    @alamat.setter
    def alamat(self, nilai: str) -> None:
        pass

    @property
    def deskripsi(self) -> str:
        pass

    @deskripsi.setter
    def deskripsi(self, nilai: str) -> None:
        pass

    @property
    def email(self) -> str:
        pass

    @email.setter
    def email(self, nilai: str) -> None:
        pass

    @property
    def status_verifikasi(self) -> StatusVerifikasi:
        pass

    @status_verifikasi.setter
    def status_verifikasi(self, nilai: StatusVerifikasi) -> None:
        pass

    @property
    def daftar_hrd(self) -> list[HRD]:
        pass

    @property
    def daftar_lowongan(self) -> list[Lowongan]:
        pass

    def ubah_profil(
        self, nama: str, alamat: str, deskripsi: str, email: str
    ) -> None:
        pass

    def tambah_hrd(self, hrd: HRD) -> None:
        pass

    def tambah_lowongan(self, lowongan: Lowongan) -> None:
        pass
