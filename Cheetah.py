class Cheetah:
    def __init__(self, ten, gioi_tinh, tuoi):
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.tuoi = tuoi

    def can_thiet(self):
        return 60

    def __repr__(self):
        return f"Ten: {self.ten}, Tuoi: {self.tuoi}, Gioi tinh: {self.gioi_tinh}"
