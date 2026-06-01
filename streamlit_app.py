import streamlit as st

st.title("Perpustakaan Linked List")

st.write("Selamat datang di aplikasi perpustakaan")

# ==========================
# LINKED LIST PERPUSTAKAAN
# ==========================

class Node:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Tambah Buku
    def tambah_buku(self, judul, penulis, tahun):
        buku_baru = Node(judul, penulis, tahun)

        if self.head is None:
            self.head = buku_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = buku_baru

        print("Buku berhasil ditambahkan!")

    # Tampilkan Buku
    def tampilkan_buku(self):
        if self.head is None:
            print("\nPerpustakaan kosong.")
            return

        current = self.head
        nomor = 1

        print("\n=== DAFTAR BUKU ===")
        while current:
            print(f"{nomor}. {current.judul}")
            print(f"   Penulis : {current.penulis}")
            print(f"   Tahun   : {current.tahun}")
            print("-" * 25)

            current = current.next
            nomor += 1

    # Cari Buku
    def cari_buku(self, judul):
        current = self.head

        while current:
            if current.judul.lower() == judul.lower():
                print("\nBuku ditemukan!")
                print("Judul   :", current.judul)
                print("Penulis :", current.penulis)
                print("Tahun   :", current.tahun)
                return

            current = current.next

        print("Buku tidak ditemukan.")

    # Hapus Buku
    def hapus_buku(self, judul):
        current = self.head
        prev = None

        while current:
            if current.judul.lower() == judul.lower():

                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                print("Buku berhasil dihapus!")
                return

            prev = current
            current = current.next

        print("Buku tidak ditemukan.")


# ==========================
# PROGRAM UTAMA
# ==========================

perpustakaan = LinkedList()

while True:
    print("\n===== PERPUSTAKAAN =====")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Cari Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        judul = input("Judul Buku   : ")
        penulis = input("Nama Penulis : ")
        tahun = input("Tahun Terbit : ")

        perpustakaan.tambah_buku(judul, penulis, tahun)

    elif pilihan == "2":
        perpustakaan.tampilkan_buku()

    elif pilihan == "3":
        judul = input("Masukkan judul buku: ")
        perpustakaan.cari_buku(judul)

    elif pilihan == "4":
        judul = input("Masukkan judul buku yang akan dihapus: ")
        perpustakaan.hapus_buku(judul)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")