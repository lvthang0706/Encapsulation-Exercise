class Keeper:
    def __init__(self, ten, tuoi, luong):
        self.ten = ten
        self.tuoi = tuoi
        self.luong = luong

    def __repr__(self):
        return f"Ten: {self.ten}, Tuoi: {self.tuoi}, Luong: {self.luong}"
