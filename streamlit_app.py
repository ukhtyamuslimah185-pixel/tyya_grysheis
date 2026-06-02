import streamlit as st

# ==========================
# LINKED LIST
# ==========================

class Node:
    def __init__(self, id_buku, judul, pengarang):
        self.id_buku = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.next = None


class LinkedListPerpustakaan:
    def __init__(self):
        self.head = None

    # Tambah buku di akhir
    def tambah_buku(self, id_buku, judul, pengarang):
        buku_baru = Node(id_buku, judul, pengarang)

        if self.head is None:
            self.head = buku_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = buku_baru

        return f"Buku '{judul}' berhasil ditambahkan."

    # Tampilkan semua buku
    def tampilkan_buku(self):
        hasil = []

        current = self.head

        while current:
            hasil.append(
                f"ID: {current.id_buku} | "
                f"Judul: {current.judul} | "
                f"Pengarang: {current.pengarang}"
            )
            current = current.next

        return hasil

    # Cari buku
    def cari_buku(self, id_buku):
        current = self.head

        while current:
            if current.id_buku == id_buku:
                return (
                    f"ID        : {current.id_buku}\n"
                    f"Judul     : {current.judul}\n"
                    f"Pengarang : {current.pengarang}"
                )

            current = current.next

        return "Buku tidak ditemukan."

    # Hapus buku
    def hapus_buku(self, id_buku):
        current = self.head
        prev = None

        while current:
            if current.id_buku == id_buku:

                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                return f"Buku ID {id_buku} berhasil dihapus."

            prev = current
            current = current.next

        return "Buku tidak ditemukan."


# ==========================
# SESSION STATE
# ==========================

if "perpustakaan" not in st.session_state:
    st.session_state.perpustakaan = LinkedListPerpustakaan()

perpustakaan = st.session_state.perpustakaan

# ==========================
# TAMPILAN MENU
# ==========================

st.title("📚 SISTEM PERPUSTAKAAN")

st.markdown("""
### MENU
1. Tambah Buku  
2. Tampilkan Buku  
3. Cari Buku  
4. Hapus Buku  
5. Keluar
""")

pilihan = st.selectbox(
    "Pilih Menu",
    [
        "1. Tambah Buku",
        "2. Tampilkan Buku",
        "3. Cari Buku",
        "4. Hapus Buku",
        "5. Keluar"
    ]
)

# ==========================
# MENU 1
# ==========================

if pilihan == "1. Tambah Buku":

    st.subheader("Tambah Buku")

    id_buku = st.text_input("ID Buku")
    judul = st.text_input("Judul Buku")
    pengarang = st.text_input("Nama Pengarang")

    if st.button("Tambah"):
        pesan = perpustakaan.tambah_buku(
            id_buku,
            judul,
            pengarang
        )
        st.success(pesan)

# ==========================
# MENU 2
# ==========================

elif pilihan == "2. Tampilkan Buku":

    st.subheader("Daftar Buku")

    data = perpustakaan.tampilkan_buku()

    if len(data) == 0:
        st.warning("Perpustakaan kosong.")
    else:
        for buku in data:
            st.write(buku)

# ==========================
# MENU 3
# ==========================

elif pilihan == "3. Cari Buku":

    st.subheader("Cari Buku")

    id_buku = st.text_input("Masukkan ID Buku")

    if st.button("Cari"):
        hasil = perpustakaan.cari_buku(id_buku)
        st.text(hasil)

# ==========================
# MENU 4
# ==========================

elif pilihan == "4. Hapus Buku":

    st.subheader("Hapus Buku")

    id_buku = st.text_input(
        "Masukkan ID Buku yang akan dihapus"
    )

    if st.button("Hapus"):
        hasil = perpustakaan.hapus_buku(id_buku)
        st.info(hasil)

# ==========================
# MENU 5
# ==========================

elif pilihan == "5. Keluar":

    st.success("Program selesai.")