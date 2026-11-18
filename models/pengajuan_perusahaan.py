from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from models.enums import StatusPengajuan

if TYPE_CHECKING:
    from models.admin_sistem import AdminSistem
    from models.perusahaan import Perusahaan
    from models.user import User


class PengajuanPerusahaan:
    def __init__(
        self,
        id_pengajuan: int,
        pemohon: User,
        nama_perusahaan: str,
        alamat_perusahaan: str,
        email_perusahaan: str,
        deskripsi_perusahaan: str,
        tanggal_pengajuan: Optional[datetime] = None,
        status: StatusPengajuan = StatusPengajuan.DIAJUKAN,
        alasan_penolakan: str = "",
        diverifikasi_oleh: Optional[AdminSistem] = None,
    ) -> None:
        pass

    @property
    def id_pengajuan(self) -> int:
        pass

    @property
    def pemohon(self) -> User:
        pass

    @property
    def nama_perusahaan(self) -> str:
        pass

    @property
    def tanggal_pengajuan(self) -> datetime:
        pass

    @property
    def status(self) -> StatusPengajuan:
        pass

    @property
    def alasan_penolakan(self) -> str:
        pass

    @property
    def diverifikasi_oleh(self) -> Optional[AdminSistem]:
        pass

    def setujui(self, admin: AdminSistem) -> Perusahaan:
        pass

    def tolak(self, admin: AdminSistem, alasan: str) -> None:
        pass
