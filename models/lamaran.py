from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from models.enums import StatusLamaran

if TYPE_CHECKING:
    from models.lowongan import Lowongan
    from models.user import User


class Lamaran:
    def __init__(
        self,
        id_lamaran: int,
        pelamar: User,
        lowongan: Lowongan,
        tanggal_lamaran: Optional[datetime] = None,
        status: StatusLamaran = StatusLamaran.MENUNGGU_REVIEW,
        catatan_hrd: str = "",
    ) -> None:
        pass

    @property
    def id_lamaran(self) -> int:
        pass

    @property
    def pelamar(self) -> User:
        pass

    @property
    def lowongan(self) -> Lowongan:
        pass

    @property
    def tanggal_lamaran(self) -> datetime:
        pass

    @property
    def status(self) -> StatusLamaran:
        pass

    @property
    def catatan_hrd(self) -> str:
        pass

    def ubah_status(self, status: StatusLamaran, catatan: str) -> None:
        pass

    def tambah_catatan(self, catatan: str) -> None:
        pass
