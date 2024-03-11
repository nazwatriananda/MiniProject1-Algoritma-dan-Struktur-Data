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

    def merge_sort(self, head, key, descending=False):
        if head is None or head.next is None:
            return head

        left, right = self.split(head)
        left = self.merge_sort(left, key, descending)
        right = self.merge_sort(right, key, descending)
        return self.merge(left, right, key, descending)

    def split(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        return head, middle

    def merge(self, left, right, key, descending=False):
        if left is None:
            return right
        if right is None:
            return left

        if key in left.data and key in right.data:
            if descending:
                if left.data[key] > right.data[key]:
                    left, right = right, left
            else:
                if left.data[key] < right.data[key]:
                    left, right = right, left

        left.next = self.merge(left.next, right, key, descending)
        left.next.prev = left
        left.prev = None
        return left

    def sort(self, key, descending=False):
        self.head = self.merge_sort(self.head, key, descending)

class JadwalKelas:
    def __init__(self):
        self.Matkul = DoubleLinkedList()

    def pilih_kelas_tersedia(self, kelas_terdaftar):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
        print("---------------Kelas Tersedia----------------")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
        for nomor, kelas_info in enumerate(kelas_terdaftar, 1):
            print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")

        nomor_kelas = int(input("Masukkan nomor kelas yang tersedia: "))

        if 1 <= nomor_kelas <= len(kelas_terdaftar) and kelas_terdaftar[nomor_kelas - 1]['available']:
            return nomor_kelas - 1
        else:
            print("--Kelas tidak tersedia atau tidak valid--")
            return None
        
    def get_jadwal_data(self):
        jadwal_data = []
        current = self.Matkul.head
        while current:
            jadwal_data.append(current.data)
            current = current.next
        return jadwal_data

    def Membaca_Jadwal(self, parameters=None, key='Nomor Pendaftaran', descending=False):
        table = PrettyTable()
        table.field_names = ["Nomor", "Jurusan", "Mata Kuliah", "Hari/Tanggal", "Ruangan"]

        if parameters is None:
            parameters = self.get_jadwal_data()

        parameters = self.Sorting_Parameters(parameters, key, descending)

        for current_data in parameters:
            table.add_row([
                current_data['Nomor Pendaftaran'],
                current_data['Jurusan'],
                current_data['Mata Kuliah'],
                current_data['Hari/Tanggal'],
                current_data['Ruangan'],
            ])

        print(str(table))

    def Pembuatan_Jadwal(self, Nomor_Pendaftaran, Jurusan, Matakuliah, Date, Ruangan, Kelas_Terdaftar):
        nomor_kelas = self.pilih_kelas_tersedia(Kelas_Terdaftar)

        if nomor_kelas is not None:
            new_data = {
                'Nomor Pendaftaran': Nomor_Pendaftaran,
                'Jurusan': Jurusan,
                'Mata Kuliah': Matakuliah,
                'Hari/Tanggal': Date,
                'Ruangan':  Kelas_Terdaftar[nomor_kelas]['Kelas']
            }
            
            self.Matkul.Tambah_Akhir(new_data)
            print("--Jadwal Kelas Berhasil Dibuat!--")
            Kelas_Terdaftar[nomor_kelas]['available'] = False
        else:
            print("--Gagal membuat jadwal, coba lagi dengan memilih kelas yang tersedia--")

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

                print("\n-- Pembaruan Jadwal --")
                print("Nomor Pendaftaran:", current.data['Nomor Pendaftaran'])
                print("Jurusan:", current.data['Jurusan'])
                print("Mata Kuliah:", current.data['Mata Kuliah'])
                print("Hari/Tanggal:", current.data['Hari/Tanggal'])
                print("Ruangan:", current.data['Ruangan'])

                break
            current = current.next
        else:
            print("-- Jadwal Kelas Tidak Bisa Diperbarui!--")

    def Sorting_Parameters(self, parameters, key, descending=False):
        if descending:
            sorted_params = sorted(parameters, key=lambda x: x[key], reverse=True)
        else:
            sorted_params = sorted(parameters, key=lambda x: x[key])
        return sorted_params
    
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
        {'Kelas': 'D302', 'available': True},
        {'Kelas': 'C302', 'available': True},
        {'Kelas': 'C304', 'available': True},
        {'Kelas': 'C402', 'available': True},
        {'Kelas': 'C404', 'available': True}
    ]

    Sistem_Pemilihan = JadwalKelas()
    while True:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("-------------------- Menu Utama ------------------------")
        print("~" * 56)
        print("---              1. Memeriksa Kelas                  ---")
        print("---              2. Membuat Jadwal                   ---")
        print("---              3. Memeriksa Jadwal Terdaftar       ---")
        print("---              4. Memperbarui Jadwal               ---")
        print("---              5. Mengurutkan Jadwal Terdaftar     ---")
        print("---              6. Menghapus Jadwal                 ---")
        print("---              7. Keluar                           ---")
        print("~" * 56)
        Pilih = input("Masukkan Pilihan Yang Tersedia Pada Menu: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if Pilih == '1':
            print("~" * 45 )
            print("---------------Kelas Terdaftar---------------")
            print("~" * 45 )
            for nomor, kelas_info in enumerate(Kelas_Terdaftar, 1):
                print(f"{nomor}. Kelas {kelas_info['Kelas']} {'(Tersedia)' if kelas_info['available'] else '(Tidak Tersedia)'}")
            print("~" * 45)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '2':
            print("-" * 45)
            Nomor_Pendaftaran = int(input("Masukkan Nomor Pendaftaran Anda: "))
            Jurusan = input("Masukkan Jurusan: ")
            Matakuliah = input("Masukkan Mata Kuliah: ")
            Date = input("Masukkan Hari Untuk Kelas: ")
            print("-" * 45)
            Ruangan = input("Tekan Enter Untuk Memilih Kelas")
            Sistem_Pemilihan.Pembuatan_Jadwal(Nomor_Pendaftaran, Jurusan, Matakuliah, Date, Ruangan, Kelas_Terdaftar)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '3':
            print("\n``````````````Berikut ini adalah tabel dari kelas terdaftar``````````````\n")
            Sistem_Pemilihan.Membaca_Jadwal()
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '4':
            print("-" * 45)
            Kelas = int(input("Masukkan Nomor Kelas: "))
            Jurusan = input("Masukkan Nama Jurusan: ")
            Matakuliah = input("Masukkan Nama Matakuliah: ")
            Date = input("Masukkan Hari/Tanggal Pembaruan: ")
            Ruangan = input("Tekan Enter Untuk Memilih Kelas Baru (kosongkan jika tidak ingin mengganti): ")
            Keterangan = input("Masukkan Keterangan Pembaruan: ")
            print("-" * 45)
            Sistem_Pemilihan.Pembaruan_Jadwal(Kelas, Jurusan, Matakuliah, Date, Ruangan, Keterangan)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '5':
            print("~" * 45)
            print("---------------Sorting Jadwal----------------")
            print("~" * 45)
            print("~~              1. Ascending               ~~")
            print("~~              2. Descending              ~~")
            print("~" * 45)
            Pilih_Sorting = input("Pilih metode sorting (1/2): ")

            if Sistem_Pemilihan.Matkul.head:
                if Pilih_Sorting == '1' or Pilih_Sorting == '2':
                    print("\n")
                    print("~" * 45)
                    print("-----Atribut yang tersedia untuk sorting-----")
                    print("~" * 45)
                    print("1. Nomor Pendaftaran")
                    print("2. Jurusan")
                    print("3. Mata Kuliah")
                    print("4. Hari/Tanggal")
                    print("5. Ruangan")
                    print("~" * 45)
                    sorting_attr = int(input("Masukkan nomor atribut untuk sorting: "))

                    attr_mapping = {
                        1: "Nomor Pendaftaran",
                        2: "Jurusan",
                        3: "Mata Kuliah",
                        4: "Hari/Tanggal",
                        5: "Ruangan"
                    }

                    sorting_attr_name = attr_mapping.get(sorting_attr)

                    if Pilih_Sorting == '1':
                        descending = False
                    else:
                        descending = True

                    parameters = Sistem_Pemilihan.get_jadwal_data()
                    parameters = Sistem_Pemilihan.Sorting_Parameters(parameters, sorting_attr_name, descending)

                    table = PrettyTable()
                    table.field_names = ["Nomor Pendaftaran", "Jurusan", "Mata Kuliah", "Hari/Tanggal", "Ruangan"]

                    for current_data in parameters:
                        table.add_row([
                            current_data['Nomor Pendaftaran'],
                            current_data['Jurusan'],
                            current_data['Mata Kuliah'],
                            current_data['Hari/Tanggal'],
                            current_data['Ruangan'],
                        ])

                    print(str(table))
                else:
                    print("Pilihan tidak valid. Kembali ke Menu Utama.")
            else:
                print("Belum ada jadwal yang terdaftar.")

        elif Pilih == '6':
            print("-" * 45)
            Kelas = int(input("Masukkan Nomor Kelas: "))
            print("-" * 45)
            Sistem_Pemilihan.Menghapus_Jadwal(Kelas)
            input("\nTekan Enter untuk kembali ke Menu Utama")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif Pilih == '7':
            print("Keluar Menu...")
            break

        else:
            print("Pilihan Anda Tidak Valid. Silahkan Masukkan Pilihan Sesuai Angka Yang Tersedia")
            input("\nTekan Enter untuk kembali ke Menu Utama")

if __name__ == "__main__":
    main()