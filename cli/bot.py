# Memasukkan library yang dibutuhkan
import nltk
from nltk.chat.util import Chat, reflections

# Menyiapkan data yang akan digunakan
# Variabel pairs merupakan daftar pertanyaan dan jawaban yang akan digunakan oleh chatbot
pairs = [
    ["siapa nama saya", "Nama Anda tidak diketahui oleh saya"],
    ["apa yang bisa Anda lakukan", "Saya adalah sebuah chatbot yang dapat memahami pertanyaan yang diajukan"],
]

# Membuat sebuah objek Chat
chatbot = Chat(pairs, reflections)

# Memulai chat
chatbot.converse()
