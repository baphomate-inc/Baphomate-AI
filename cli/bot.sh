#!/bin/bash

# Mengambil input dari user
echo -n "Masukkan pertanyaan Anda: "
read input

# Menentukan jawaban yang akan diberikan
if [[ $input == *"siapa"* ]]; then
  echo "Saya adalah sebuah program AI yang dibuat menggunakan bash"
elif [[ $input == *"apa"* ]]; then
  echo "Saya adalah sebuah program AI yang dapat memahami pertanyaan yang diajukan"
else
  echo "Maaf, saya tidak dapat menjawab pertanyaan tersebut"
fi
