class Zoo:
    def __init__(self, ten, ngan_sach, suc_chua_dong_vat, suc_chua_nhan_vien):
        self.ten = ten
        self.ngan_sach = ngan_sach
        self.suc_chua_dong_vat = suc_chua_dong_vat
        self.suc_chua_nhan_vien = suc_chua_nhan_vien
        self.dong_vat = []
        self.nhan_vien = []

    def them_dong_vat(self, dong_vat, gia):
        if len(self.dong_vat) < self.suc_chua_dong_vat:
            if self.ngan_sach >= gia:
                self.dong_vat.append(dong_vat)
                self.ngan_sach -= gia
                return f"{dong_vat.ten} loai {type(dong_vat).__name__} da duoc them vao so thu"
            else:
                return "Khong du ngan sach"
        return "Khong du suc chua cho dong vat"

    def them_nhan_vien(self, nhan_vien):
        if len(self.nhan_vien) < self.suc_chua_nhan_vien:
            self.nhan_vien.append(nhan_vien)
            return f"{nhan_vien.ten} loai {type(nhan_vien).__name__} da duoc tuyen dung"
        return "Khong du suc chua cho nhan vien"

    def sa_thai_nhan_vien(self, ten_nhan_vien):
        for nhan_vien in self.nhan_vien:
            if nhan_vien.ten == ten_nhan_vien:
                self.nhan_vien.remove(nhan_vien)
                return f"{ten_nhan_vien} da bi sa thai"
        return f"Khong co {ten_nhan_vien} trong so thu"

    def tra_luong_nhan_vien(self):
        tong_luong = sum(nhan_vien.luong for nhan_vien in self.nhan_vien)
        if self.ngan_sach >= tong_luong:
            self.ngan_sach -= tong_luong
            return f"Ban da tra luong cho nhan vien. Ho rat vui. Ngan sach con lai: {self.ngan_sach}"
        return "Ban khong du ngan sach de tra luong cho nhan vien. Ho rat buon"

    def cham_soc_dong_vat(self):
        tong_nhu_cau = sum(dong_vat.can_thiet() for dong_vat in self.dong_vat)
        if self.ngan_sach >= tong_nhu_cau:
            self.ngan_sach -= tong_nhu_cau
            return f"Ban da cham soc tat ca dong vat. Chung rat vui. Ngan sach con lai: {self.ngan_sach}"
        return "Ban khong du ngan sach de cham soc dong vat. Chung rat buon"

    def loi_nhuan(self, so_tien):
        self.ngan_sach += so_tien

    def trang_thai_dong_vat(self):
        su_tu = [dong_vat for dong_vat in self.dong_vat if isinstance(dong_vat, Lion)]
        ho = [dong_vat for dong_vat in self.dong_vat if isinstance(dong_vat, Tiger)]
        bao = [dong_vat for dong_vat in self.dong_vat if isinstance(dong_vat, Cheetah)]

        ket_qua = f"So thu co {len(self.dong_vat)} dong vat\n"
        ket_qua += f"----- {len(su_tu)} Su tu:\n" + '\n'.join([repr(su_tu) for su_tu in su_tu]) + '\n'
        ket_qua += f"----- {len(ho)} Ho:\n" + '\n'.join([repr(ho) for ho in ho]) + '\n'
        ket_qua += f"----- {len(bao)} Bao:\n" + '\n'.join([repr(bao) for bao in bao])
        return ket_qua

    def trang_thai_nhan_vien(self):
        nguoi_trong_su_tu = [nhan_vien for nhan_vien in self.nhan_vien if isinstance(nhan_vien, Keeper)]
        nguoi_cham_soc = [nhan_vien for nhan_vien in self.nhan_vien if isinstance(nhan_vien, Caretaker)]
        bac_si_thu_y = [nhan_vien for nhan_vien in self.nhan_vien if isinstance(nhan_vien, Vet)]

        ket_qua = f"So thu co {len(self.nhan_vien)} nhan vien\n"
        ket_qua += f"----- {len(nguoi_trong_su_tu)} Nguoi giu su tu:\n" + '\n'.join([repr(nguoi_trong_su_tu) for nguoi_trong_su_tu in nguoi_trong_su_tu]) + '\n'
        ket_qua += f"----- {len(nguoi_cham_soc)} Nguoi cham soc:\n" + '\n'.join([repr(nguoi_cham_soc) for nguoi_cham_soc in nguoi_cham_soc]) + '\n'
        ket_qua += f"----- {len(bac_si_thu_y)} Bac si thu y:\n" + '\n'.join([repr(bac_si_thu_y) for bac_si_thu_y in bac_si_thu_y])
        return ket_qua
