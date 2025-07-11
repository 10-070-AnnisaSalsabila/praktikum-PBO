import tkinter as tk
from tkinter import messagebox, scrolledtext, Menu

class DailyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catatan Harian")
        
        # Struktur data untuk menyimpan catatan
        self.notes = {}
        
        # Membuat menu bar
        self.menu_bar = Menu(root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Keluar", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Tentang", command=self.show_about)
        self.menu_bar.add_cascade(label="Bantuan", menu=self.help_menu)
        
        root.config(menu=self.menu_bar)
        
        # Widget untuk input judul
        self.title_label = tk.Label(root, text="Judul:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Tombol untuk menambah catatan
        self.add_button = tk.Button(root, text="Tambah Catatan", command=self.add_note)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Tombol untuk menghapus catatan
        self.delete_button = tk.Button(root, text="Hapus Catatan", command=self.delete_note)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)
        
        # Listbox untuk menampilkan daftar catatan
        self.notes_listbox = tk.Listbox(root, width=50)
        self.notes_listbox.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.notes_listbox.bind('<<ListboxSelect>>', self.display_note)
        
        # Scrollbar untuk Listbox
        self.scrollbar = tk.Scrollbar(root)
        self.scrollbar.grid(row=1, column=4, sticky='ns')
        self.notes_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.notes_listbox.yview)
        
        # Text area untuk input isi catatan
        self.note_text = scrolledtext.ScrolledText(root, width=60, height=15)
        self.note_text.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
        
    def add_note(self):
        title = self.title_entry.get().strip()
        content = self.note_text.get("1.0", tk.END).strip()
        
        if not title or not content:
            messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong.")
            return
        
        if title in self.notes:
            messagebox.showerror("Error", "Judul catatan sudah ada.")
            return
        
        self.notes[title] = content
        self.notes_listbox.insert(tk.END, title)
        self.title_entry.delete(0, tk.END)
        self.note_text.delete("1.0", tk.END)
        
    def display_note(self, event):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            title = self.notes_listbox.get(selected_index)
            content = self.notes[title]
            self.note_text.delete("1.0", tk.END)
            self.note_text.insert(tk.END, content)
        
    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if not selected_index:
            return
        
        title = self.notes_listbox.get(selected_index)
        confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus catatan '{title}'?")
        if confirm:
            del self.notes[title]
            self.notes_listbox.delete(selected_index)
            self.note_text.delete("1.0", tk.END)
        
    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Catatan Harian\nVersi 1.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyNotesApp(root)
    root.mainloop()