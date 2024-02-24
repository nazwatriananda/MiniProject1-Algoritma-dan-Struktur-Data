from prettytable import PrettyTable
import os

print("======================================================")
print("Nama        : Nazwa Tri Ananda")
print("NIM         : 2309116018")
print("Kelas       : Sistem Informasi A")
print("Mata Kuliah : Praktikum Algoritma dan Struktur Data")
print("======================================================\n")

def clear_screen():
    # Bersihkan layar konsol berdasarkan sistem operasi
    os.system('cls' if os.name == 'nt' else 'clear')

class JadwalKelas:
    def __init__(self, kelas_terdaftar):
        self.Matkul = {}
        self.kelas_terdaftar = kelas_terdaftar

    def pilih_kelas_tersedia(self):
        print("-- Kelas Tersedia --")
        for nomor, kelas_info in self.kelas_terdaftar.items():
            print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")

        nomor_kelas = int(input("Masukkan nomor kelas yang tersedia: "))

        if nomor_kelas in self.kelas_terdaftar and self.kelas_terdaftar[nomor_kelas]['available']:
            return nomor_kelas
        else:
            print("--Kelas tidak tersedia atau tidak valid--")
            return None

    def Pembuatan_Jadwal(self, Nomor, Jurusan, Matakuliah, Date, Ruangan):
        nomor_kelas = self.pilih_kelas_tersedia()

        if nomor_kelas is not None:
            self.Matkul[nomor_kelas] = {
                'Nomor Pendaftaran': Nomor,
                'Jurusan': Jurusan,
                'Mata Kuliah': Matakuliah,
                'Hari/Tanggal': Date,
                'Ruangan': Ruangan,
            }
            print("--Jadwal Kelas Berhasil Dibuat!--")
            self.kelas_terdaftar[nomor_kelas]['available'] = False
        else:
            print("--Gagal membuat jadwal, coba lagi dengan memilih kelas yang tersedia--")
        
    def Membaca_Jadwal(self):
        if not self.Matkul:
            return "-----Jadwal Kosong-----"
        table = PrettyTable()
        table.field_names = ["Nomor", "Jurusan", "Mata Kuliah", "Hari/Tanggal", "Ruangan"]
        for nomor_kelas, jadwal in self.Matkul.items():
            ruangan_info = self.kelas_terdaftar.get(nomor_kelas, {}).get('Kelas', 'Tidak Tersedia')
            table.add_row([nomor_kelas, jadwal['Jurusan'], jadwal['Mata Kuliah'], jadwal['Hari/Tanggal'], f"{jadwal['Ruangan']} ({ruangan_info})"])
        return str(table)

    def Pembaruan_Jadwal(self, Kelas_Terdaftar, Jurusan=None, Matakuliah=None, Date=None, Ruangan=None, Keterangan = None):
        if Kelas_Terdaftar in self.Matkul:
            if Jurusan:
                self.Matkul[Kelas_Terdaftar]['Jurusan'] = Jurusan
            if Matakuliah:
                self.Matkul[Kelas_Terdaftar]['Mata Kuliah'] = Matakuliah
            if Date:
                self.Matkul[Kelas_Terdaftar]['Hari/Tanggal'] = Date
            if Ruangan:
                self.Matkul[Kelas_Terdaftar]['Ruangan'] = Ruangan
            if Keterangan:
                self.Matkul[Kelas_Terdaftar]['Keterangan'] = Keterangan
                print("--Jadwal Kelas Telah Diperbarui!--")
        else:
            print("-- Jadwal Kelas Tidak Bisa Diperbarui!--")


    def Menghapus_Jadwal(self, Kelas_Terdaftar):
        if Kelas_Terdaftar in self.Matkul:
            del self.Matkul[Kelas_Terdaftar]
            print("--Jadwal Kelas Telah Dihapus!--")
        else:
            print("--Tidak Bisa Menghapus Jadwal!--")

def main():
    Kelas_Terdaftar = {
        1: {'Kelas': 'D403', 'available': True},
        2: {'Kelas': 'C302', 'available': True},
        3: {'Kelas': 'C304', 'available': True},
        4: {'Kelas': 'C402', 'available': True},
        5: {'Kelas': 'C404', 'available': True}
    }
    
    Sistem_Pemilihan = JadwalKelas(Kelas_Terdaftar)
    while True:
        clear_screen()
        print("\n======================================================")
        print("==================== Menu Utama ========================")
        print("===              1. Memeriksa Kelas                  ===")
        print("===              2. Membuat Jadwal Baru              ===")
        print("===              3. Memeriksa Jadwal Terdaftar       ===")
        print("===              4. Memperbarui Jadwal               ===")
        print("===              5. Menghapus Jadwal                 ===")
        print("===              6. Keluar                           ===")
        print("========================================================")
        Pilih = input("Masukkan Pilihan Yang Tersedia Pada Menu: ")

        if Pilih == '1':
            print("\n----------Kelas Terdaftar----------")
            for nomor, kelas_info in Kelas_Terdaftar.items():
                print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")
            input("\nTekan Enter untuk kembali ke Menu Utama")

        elif Pilih == '2':
            clear_screen()
            Nomor_Pendaftaran = int(input("Masukkan Nomor Pendaftaran Anda: "))
            Jurusan = input("Masukkan Jurusan: ")
            Matakuliah = input("Masukkan Mata Kuliah: ")
            Date = input("Masukkan Hari Untuk Kelas: ")
            Ruangan = input("Tekan Enter Untuk Memilih Kelas")
            Sistem_Pemilihan.Pembuatan_Jadwal(Nomor_Pendaftaran, Jurusan, Matakuliah, Date, Ruangan)
            input("\nTekan Enter untuk kembali ke Menu Utama")

        elif Pilih == '3':
            clear_screen()
            print(Sistem_Pemilihan.Membaca_Jadwal())
            input("\nTekan Enter untuk kembali ke Menu Utama")

        elif Pilih == '4':
            clear_screen()
            Kelas = int(input("Masukkan Nomor Kelas: "))
            Jurusan = input("Masukkan Nama Jurusan: ")
            Matakuliah = input("Masukkan Nama Matakuliah: ")
            Date = input("Masukkan Hari/Tanggal Pembaruan: ")
            Ruangan = input("Tekan Enter Untuk Memilih Kelas Baru (kosongkan jika tidak ingin mengganti): ")
            Keterangan = input("Masukkan Keterangan Pembaruan: ")
            Sistem_Pemilihan.Pembaruan_Jadwal(Kelas, Jurusan, Matakuliah, Date, Ruangan, Keterangan)
            input("\nTekan Enter untuk kembali ke Menu Utama")

        elif Pilih == '5':
            clear_screen()
            Kelas = int(input("Masukkan Nomor Kelas: "))
            Sistem_Pemilihan.Menghapus_Jadwal(Kelas)
            input("\nTekan Enter untuk kembali ke Menu Utama")

        elif Pilih == '6':
            print("Keluar Menu...")
            break

        else:
            print("Pilihan Anda Tidak Valid. Silahkan Masukkan Pilihan Sesuai Angka Yang Tersedia")
            input("\nTekan Enter untuk kembali ke Menu Utama")

if __name__ == "__main__":
    main()
