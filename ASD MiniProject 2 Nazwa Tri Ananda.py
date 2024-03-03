from prettytable import PrettyTable
import os

print("-------------------------------------------------------")
print("Nama        : Nazwa Tri Ananda")
print("NIM         : 2309116018")
print("Kelas       : Sistem Informasi A")
print("Mata Kuliah : Praktikum Algoritma dan Struktur Data")
print("-------------------------------------------------------\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def Tambah_Akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def Hapus_Node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                del current
                return
            current = current.next

    def Menemukan_Data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def display(self):
        if not self.head:
            print("Double Linked List is empty.")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next

class JadwalKelas:
    def __init__(self):
        self.Matkul = DoubleLinkedList()

    def pilih_kelas_tersedia(self, kelas_terdaftar):
        print("-- Kelas Tersedia --")
        for nomor, kelas_info in enumerate(kelas_terdaftar, 1):
            print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")

        nomor_kelas = int(input("Masukkan nomor kelas yang tersedia: "))

        if 1 <= nomor_kelas <= len(kelas_terdaftar) and kelas_terdaftar[nomor_kelas - 1]['available']:
            return nomor_kelas - 1
        else:
            print("--Kelas tidak tersedia atau tidak valid--")
            return None

    def Pembuatan_Jadwal(self, Nomor, Jurusan, Matakuliah, Date, Ruangan, kelas_terdaftar):
        nomor_kelas = self.pilih_kelas_tersedia(kelas_terdaftar)

        if nomor_kelas is not None:
            self.Matkul.Tambah_Akhir({
                'Nomor Pendaftaran': Nomor,
                'Jurusan': Jurusan,
                'Mata Kuliah': Matakuliah,
                'Hari/Tanggal': Date,
                'Ruangan':  kelas_terdaftar[nomor_kelas]['Kelas']
            })
            print("--Jadwal Kelas Berhasil Dibuat!--")
            kelas_terdaftar[nomor_kelas]['available'] = False
        else:
            print("--Gagal membuat jadwal, coba lagi dengan memilih kelas yang tersedia--")

    def Membaca_Jadwal(self):
        table = PrettyTable()
        table.field_names = ["Nomor", "Jurusan", "Mata Kuliah", "Hari/Tanggal", "Ruangan"]  # Menambahkan kolom Ruangan Dipilih
        current = self.Matkul.head
        while current:
            table.add_row([
                current.data['Nomor Pendaftaran'],
                current.data['Jurusan'],
                current.data['Mata Kuliah'],
                current.data['Hari/Tanggal'],
                current.data['Ruangan'],
            ])
            current = current.next
        return str(table)

    def Pembaruan_Jadwal(self, Kelas_Terdaftar, Jurusan=None, Matakuliah=None, Date=None, Ruangan=None, Keterangan=None):
        current = self.Matkul.head
        while current:
            if current.data['Nomor Pendaftaran'] == Kelas_Terdaftar:
                if Jurusan:
                    current.data['Jurusan'] = Jurusan
                if Matakuliah:
                    current.data['Mata Kuliah'] = Matakuliah
                if Date:
                    current.data['Hari/Tanggal'] = Date
                if Ruangan:
                    current.data['Ruangan'] = Ruangan
                if Keterangan:
                    current.data['Keterangan'] = Keterangan
                    print("--Jadwal Kelas Telah Diperbarui!--")
                break
            current = current.next_node
        else:
            print("-- Jadwal Kelas Tidak Bisa Diperbarui!--")

    def Menghapus_Jadwal(self, Kelas_Terdaftar):
        current = self.Matkul.head
        while current:
            if current.data['Nomor Pendaftaran'] == Kelas_Terdaftar:
                self.Matkul.Hapus_Node(current.data)
                print("--Jadwal Kelas Telah Dihapus!--")
                return
            current = current.next
        else:
            print("--Jadwal Kelas Tidak Ditemukan!--") 

def main():
    Kelas_Terdaftar = [
        {'Kelas': 'D403', 'available': True},
        {'Kelas': 'C302', 'available': True},
        {'Kelas': 'C304', 'available': True},
        {'Kelas': 'C402', 'available': True},
        {'Kelas': 'C404', 'available': True}
    ]
    
    Sistem_Pemilihan = JadwalKelas()
    while True:
        print("\n========================================================")
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
            for nomor, kelas_info in enumerate(Kelas_Terdaftar, 1):
                print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '2':
            Nomor_Pendaftaran = int(input("Masukkan Nomor Pendaftaran Anda: "))
            Jurusan = input("Masukkan Jurusan: ")
            Matakuliah = input("Masukkan Mata Kuliah: ")
            Date = input("Masukkan Hari Untuk Kelas: ")
            Ruangan = input("Tekan Enter Untuk Memilih Kelas")
            Sistem_Pemilihan.Pembuatan_Jadwal(Nomor_Pendaftaran, Jurusan, Matakuliah, Date, Ruangan, Kelas_Terdaftar)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '3':
            print(Sistem_Pemilihan.Membaca_Jadwal())
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '4':
            Kelas = int(input("Masukkan Nomor Kelas: "))
            Jurusan = input("Masukkan Nama Jurusan: ")
            Matakuliah = input("Masukkan Nama Matakuliah: ")
            Date = input("Masukkan Hari/Tanggal Pembaruan: ")
            Ruangan = input("Tekan Enter Untuk Memilih Kelas Baru (kosongkan jika tidak ingin mengganti): ")
            Keterangan = input("Masukkan Keterangan Pembaruan: ")
            Sistem_Pemilihan.Pembaruan_Jadwal(Kelas, Jurusan, Matakuliah, Date, Ruangan, Keterangan)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '5':
            Kelas = int(input("Masukkan Nomor Kelas: "))
            Sistem_Pemilihan.Menghapus_Jadwal(Kelas)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '6':
            print("Keluar Menu...")
            break

        else:
            print("Pilihan Anda Tidak Valid. Silahkan Masukkan Pilihan Sesuai Angka Yang Tersedia")
            input("\nTekan Enter untuk kembali ke Menu Utama")

if __name__ == "__main__":
    main()
