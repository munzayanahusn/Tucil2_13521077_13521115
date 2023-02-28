# Tucil2_Stima
Tugas Kecil II IF2211 Strategi Algoritma Semester II Tahun 2022/2023 Pemanfaatan Algoritma Divide And Conquer dalam Closest P

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-tugas)
* [Strategi Divide and Conquer Program](#strategi-divideandconquer-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Kompilasi Program](#cara-kompilasi-program)
* [Hal Yang Harus DIperhatikan](#hal-yang-harus-diperhatikan)
* [Author Program](#author-program)

## Deskripsi Singkat Tugas
Mencari sepasang titik terdekat dapat dilakukan dengan Algoritma Divide and Conquer. Hanya saja yang telah dipelajari adalah mencari jarak titik terdekat di bidang 2D. Pada Tucil 2 kali ini diminta mengembangkan algoritma mencari sepasang titik terdekat pada bidang 3D. Misalkan terdapat n buah titik pada ruang 3D. Setiap titik P di dalam ruang dinyatakan dengan koordinat P = (x, y, z). Carilah sepasang titik yang mempunyai jarak terdekat satu sama lain. 

## Strategi Divide And Conquer Program
Tujuan dari strategi dibuat untuk mendapatkan pasangan titik yang jaraknya paling dekat di 3D. Pada dasarnya hal ini dapat dicari dengan menggunakan algoritma brute force dengan meng-check satu persatu jarak antar titik. Hanya kompleksitas waktu pengerjaannya cukup buruk. Sehingga diimplementasikan dengan strategi divide and conquer. Strategi yang dilakukan adalah dengan membagi 2 wilayah yaitu kanan dan kiri kemudian di cek mana jaraknya paling dekat. Titik yang jaraknya paling dekat di kanan dan titik yang jaraknya paling dekat dikiri kemudian dibandingkan. Hasil akhirnya dibandingkan dengan jarak antar titik dengan titik yang ada disekitar garis pembagi. Langkah-langkah ini dilakukan secara rekursif. 

## Struktur Program
```bash
.
├───doc
│       Tucil2_13521077_13521115.pdf
│
└───src
|    └───calculateBruteForce.py
|        └───calculateDC.py
|            └───main.py
|                └───plot.py
|                    └───quickSortSbX.py
|                        └───tools.py
│   .gitignore       
│    README.md                           
```

## Requirement Program
* Python3
* instalasi library bisa menggunakan "pip install <nama labrary>"
* Visual Studio Code (opsional bisa dijalankan di terminal juga atau dengan IDE lain)

## Cara Menjalankan Program
* Program dapat dijalankan dengan cara pertama download program pada link [berikut](https://github.com/munzayanahusn/Tucil2_13521077_13521115.git) atau bisa clone reponya
* Unzip file hasil download pada mesin eksekusi jika memilih mendownload file.
* Jika menggunakan IDE seperti visual studio code bisa klik file main.py kemudian run code, atau bisa dengan menekan F5
* Jika menggunakan terminal maka cd ke tempat disimpannya main.py kemudian tuliskan perintah "python -u main.py"
* Setelah langkah-langkah tersebut sudah dilakukan maka program dapat dijalankan 

## Hal Yang Harus Diperhatikan 
* Saat menjalankan program dan sudah muncul gambar visualisasi dari titik maka tab visualisasi harus di close terlebih dahulu sebelum menjalankan ulang program 

## Author Program
* Husnia Munzayana - 13521077
* Shelma Salsabila - 13521115