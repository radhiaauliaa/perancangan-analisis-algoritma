# Perancangan-dan-Analisis-Algoritma <img src="https://www.thedataschool.com.au/wp-content/uploads/2022/01/logo-data-structures-algorithms.png" width="34" height="34">

Repositori ini berisi penjelasan mengenai materi dari tugas yang dikerjakan oleh mahasiswa. Penjelasan beserta link setiap tugas telah tertera di bawah.

Dosen : Randi Proska Sandra, M.Sc<br>
Kode Kelas : INF1.62.4001 <br>
Seksi : 202423430075<br>
Mahasiswa : Radhia Aulia Nisa (23343049)<br><br>

Algoritma Prim adalah salah satu algoritma untuk mencari Minimum Spanning Tree (MST) dari sebuah graf berbobot dan tidak berarah. Minimum Spanning Tree adalah pohon merentang yang memiliki bobot total minimum dari semua sisi dalam graf. Algoritma ini ditemukan oleh matematikawan Czech, Vojtěch Jarník, dan kemudian dikembangkan lebih lanjut oleh Robert C. Prim dan Edsger W. Dijkstra.<br>
Algoritma Prim bekerja dengan pendekatan greedy, yang berarti pada setiap langkahnya, algoritma memilih sisi dengan bobot terkecil yang menghubungkan simpul yang sudah tergabung dalam MST dengan simpul yang belum tergabung. Proses ini diulang hingga semua simpul dalam graf sudah dimasukkan ke dalam MST.<br>

Langkah-langkah algoritma Prim adalah sebagai berikut:
1.	Pilih sembarang simpul sebagai simpul awal.
2.	Tandai simpul tersebut sebagai bagian dari MST.
3.	Pilih sisi dengan bobot minimum yang menghubungkan simpul dalam MST dengan simpul di luar MST.
4.	Tambahkan simpul yang terhubung ke MST.
5.	Ulangi langkah 3 dan 4 sampai semua simpul telah dimasukkan ke dalam MST.

