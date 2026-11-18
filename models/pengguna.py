from __future__ import annotations

from abc import ABC, abstractmethod


class Pengguna(ABC):
    def __init__(
        self,
        id_pengguna: int,
        nama: str,
        email: str,
        password_hash: str,
        status_aktif: bool = True,
    ) -> None:
        pass

    @property
    def id_pengguna(self) -> int:
        pass

    @property
    def nama(self) -> str:
        pass

    @nama.setter
    def nama(self, nilai: str) -> None:
        pass

    @property
    def email(self) -> str:
        pass

    @email.setter
    def email(self, nilai: str) -> None:
        pass

    @property
    def status_aktif(self) -> bool:
        pass

    def ubah_profil(self, nama: str, email: str) -> None:
        pass

    def ubah_password(self, password_lama: str, password_baru: str) -> bool:
        pass

    def verifikasi_password(self, password: str) -> bool:
        pass

    def aktifkan_akun(self) -> None:
        pass

    def nonaktifkan_akun(self) -> None:
        pass

    @abstractmethod
    def get_role(self) -> str:
        pass

    @abstractmethod
    def tampilkan_dashboard(self) -> None:
        pass
