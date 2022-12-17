#../Baphonate-AI/cli/materi/main.materi.py
#../this is program materi in CLI
import os,sys,time,random
def main():
   
    #../clear/bersih sebersih hatiku untuk mu :)
    def clear():
        os.system('clear')
        
    #batas suci cintaku padamu
    
    #../color warnanya
    class col:
        red="\033[1;31m" #/kebaya merah
        grn="\033[1;32m" #/warna kesukaan aing
        ylw="\033[1;33m" #/warna caduk
        blu="\033[1;34m" #/viking nih bosss 
        pop="\033[1;35m" #/janda syemock rasa perawan
        cyn="\033[1;36m" #/warna langit cerah secerah hatiku anjay serepetetetetett
        de="\033[0m" #/bawaan
            
    
    #../lumpat    
    def lumpat(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            #kecepatan lumpat secepat dia meninggalkan ku pas lagi sange sanage nya
            time.sleep(random.random() * 0.1)
            #andai saja sikap ku tidak membuat diri nya pergi :')
    #../batas pemisah antara aku dan dia
    
    def welcome():
        clear()
        lumpat("> Selamat datang di Materi kami ^_^\n> Agan akan Di pandu oleh Baphomate Bot.")
    #../done welcome
    
   
    def banner():
        welcome()
        time.sleep(2)
        clear()
        print(col.de + "     +--------------------------------+")
        print("     |" + col.cyn + "     Welcome to Materi Kit" + col.de + "      |")
        print("     +--------------------------------+")
    #../done banner
    
    def login():
        lumpat("🤖: Hallo Perkenalkan Nama saya Baphomate Bot\n🤖: Saya akan memandu anda untuk mempelajari materi kami\n🤖: Ketikan atau masukan kata kunci menu untuk melihat list materi kami")
    banner()  
    login()
    jawab = ("menu")
    jawab2 = ("Menu")

    agan = str(input("👤: "))
    if agan == jawab or jawab2: 
        def main(): #../main for menu
            #materi hacking
            def hacking():
                lumpat(col.de + "🤖: Sebelum melangkah kepembelajaran mari kita comli dulu agar otak gak rujad ^_^")
                time.sleep(3)
                lumpat("🤖: ...... crotttt")
                lumpat("🤖: Selesai.")
                time.sleep(1)
                lumpat("🤖: Baik lah sesudah comli mari kita masuk kepembelajaran dasar tentang etichal hacking part 1.")
                #./isi artikelnya mek
                lumpat("🤖: Baik, disini saya akan menjelas kan materi awal tentang hacking.")
                lumpat("🤖: Namun sebelum melangkah ke beberapa metode hacking adakalanya kalian mengenal dulu apa itu hacking.")
                lumpat("🤖: Apa itu hacking?\n🤖: Hacking adalah proses mengidentifikasi dan mengeksploitasi kelemahan dalam sistem atau jaringan. untuk mendapatkan akses tidak sah ke data dan sumber daya sistem. Hal ini juga dapat didefinisikan sebagai intrusi tidak sah ke dalam sistem informasi / jaringan oleh penyerang dengan mengorbankan keamanan. Contoh Hacking: Memanfaatkan kelemahan password default untuk mendapatkan akses ke data yang tersimpan di dalam sistem. Nah, ada beberapa metode peretasan mulai dari bruteforce,phising,dan lainnya.\n🤖: Sebelum lanjut ke tahap itu mari kita simak tentang peretasan etis.")
                lumpat("🤖: Apa itu peretas etis\n🤖: Peretasan Etis kadang-kadang disebut sebagai Pengujian Penetrasi. adalah tindakan penyusupan/penetrasi ke dalam sistem atau jaringan untuk mengetahui ancaman, kerentanan dalam sistem yang mungkin ditemukan dan dieksploitasi oleh penyerang jahat yang menyebabkan hilangnya data, kerugian finansial, atau kerusakan besar lainnya. Tujuan dari peretasan etis adalah untuk meningkatkan keamanan jaringan atau sistem dengan memperbaiki kerentanan yang ditemukan selama pengujian. Peretas etis dapat menggunakan metode dan alat yang sama yang digunakan oleh peretas jahat tetapi dengan izin dari orang yang berwenang untuk tujuan meningkatkan keamanan dan mempertahankan sistem dari serangan pengguna jahat. Peretas etis diharapkan untuk melaporkan semua kerentanan dan kelemahan yang ditemukan selama proses kepada manajemen.\n🤖: Nah, Jadi siapakah peretas etis?")
                lumpat("🤖: Peretas terbagi bari berbagai golongan Diantaranya yaitu sebagai berikut.")
                lumpat("🤖: Balck Hat Hacker (peretas topi hitam)")
                lumpat("🤖: Hitam sering diidentifikasi dengan hal-hal negatif. Termasuk saat mengklasifikasikan peretas. Peretas yang masuk dalam kategori hitam atau Topi Hitam adalah mereka yang melakukan hacking dengan sistem atau program yang ilegal. Tujuannya tidak terlalu bagus karena mereka melakukan hacking untuk mengambil data pribadi pengguna internet seperti password ke nomor telepon. Mereka juga kadang-kadang menyebarkan virus pada perangkat lain. Dari data pribadi yang dicuri mereka bisa mendapatkan keuntungan yang besar. Data-data ini kalau dijual bisa sangat mahal karena banyak yang menginginkannya. Tindakan seperti itu jelas-jelas merugikan dan membahayakan sistem yang diretas.")
                lumpat("""🤖: White Hat Hacker (topi putih)\n🤖: Selain peretas Topi Hitam, ada juga peretas Topi Putih. Anda bisa mengatakan Topi Putih adalah lawan dari Topi Hitam. Sementara Black Hat menggunakan kemampuan hackingnya untuk mencuri data pribadi dan tindakan kriminal lainnya, White Hat melakukan yang sebaliknya. Mereka mencoba meretas sistem atau program untuk menemukan lubang keamanan. White Hat juga bekerja sesuai peraturan dan melalui metode hukum. Dengan tujuan "mulia" ini, White Hat sering disebut sebagai hacker yang baik. Secara umum, Topi Putih dikontrak oleh perusahaan untuk bekerja sama dengan tim pengembangan mereka. White Hat akan mencari kerentanan dalam sistem yang dibuat oleh pengembang. Sehingga, sistem yang dibuat bisa lebih aman dan risiko kebocoran data bisa diminimalkan.
🤖: Gray Hat Hacker (topi abu-abu)\n
🤖: Ternyata di antara Black Hat dan White Hat ada juga kelompok peretas yang terpisah. Mereka disebut Topi Abu-abu. Topi Abu-abu tidak dapat dikategorikan sebagai Topi Hitam atau Topi Putih karena mereka beroperasi dengan menggabungkan kedua metode. Gray Hat menerapkan metode peretas Black Hat, tetapi pada saat yang sama mereka juga menggunakan metode yang mirip dengan peretas White Hat. Misalnya, ketika mereka meretas sistem atau program, Gray Hat melakukannya secara ilegal seperti peretas Black Hat. Namun, tidak seperti peretas Black Hat yang meninggalkan kerusakan pada sistem, Gray Hat memulihkan sistem seperti biasa seperti peretas White Hat sehingga tampaknya seolah-olah tidak ada yang terjadi pada sistem. Dalam istilah sederhana, dapat disimpulkan bahwa tujuan Gray Hat meretas sebuah sistem hanyalah untuk menguji kemampuannya. Setelah mengetahui jenis-jenis peretas, Anda dapat menyimpulkan bahwa tidak semua peretas adalah penjahat. Ada juga peretas yang bekerja secara legal dan memiliki izin khusus untuk meretas sistem, yaitu peretas White Hat. Di sisi lain, ada peretas yang tidak terlalu baik, tetapi juga bukan penjahat. Mereka adalah peretas Gray Hat.
🤖: Di antara ketiga peretas itu ada juga yang peretas lain Ya, peretas amatir dapat disebut script kidde's Mereka mengandalkan metode hacking dari tiga kelompok peretas, mereka hanya menggunakan program copy paste atau menggunakan program orang lain untuk keperluan hacking. Seperti DDoS umum, bruteforce dll.\n
🤖: Semoga ulasan ini dapat mengubah persepsi Anda terhadap peretas yang selalu identik dengan gambar negatif.

                """)
                
                
            #../done hacking
            
            #materi programing
            #def programing():
            
            #.//menu materi
            def menu():
                clear()
                banner()
                print("┌───[MENU]")
                print("│")
                print("├──• 1.Materi For basic etichal hacking")
                print("├──• 2.Materi For basic programing")
                print("├──• 0.back ")
                print("│")
            menu()  
            pil = int(input("└──╼  "))
            if pil == 1:
                hacking()
                input("[Enter untuk kembali]")
                main()
            elif pil == 2:
                lumpat("🤖: Sayang nya menu yang agan pilih sedang di buat oleh Majikan saya\n🤖: Mohon Tunggu update selanjutnya ya")
                time.sleep(1)
                main()
            elif pil == 0: 
                os.system("bash main.sh")
            else:
                lumpat("🤖: " + col.red + "Wrong Input !")
                time.sleep(1)
                main()
                
            #../done menu
        main() #/done main for menu
    else:
        lumpat("🤖: " + col.red + ("Wrong input !"))
        time.sleep(2)
        os.system("python cli/materi/main.materi.py")
if __name__ == '__main__':
    main()