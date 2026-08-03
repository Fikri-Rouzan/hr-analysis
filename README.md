# Human Resources (HR) Analysis

## 📌 Deskripsi

Analisis data sumber daya manusia ini berfokus pada evaluasi tingkat kepuasan, kinerja, dan pola retensi karyawan di lingkungan perusahaan. Pemetaan dilakukan berdasarkan berbagai indikator kerja dan informasi personalia untuk membantu pihak manajemen memahami faktor utama yang memengaruhi dinamika kerja serta keputusan karyawan untuk bertahan atau keluar dari organisasi.

---

## 💾 Dataset

Dataset sumber daya manusia ini memuat informasi kunci mengenai profil dan riwayat kerja karyawan di perusahaan. Data terstruktur ini mencakup parameter penting seperti tingkat kepuasan kerja, evaluasi kinerja, rata-rata jam kerja bulanan, masa kerja, serta status retensi karyawan. Informasi pendukung seperti divisi kerja dan tingkat kelompok gaji juga disertakan untuk memberikan gambaran menyeluruh mengenai kondisi tenaga kerja.

---

## 💼 Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan. Meskipun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju menghadapi tantangan serius pada aspek operasional Human Resources (HR), khususnya terkait tingginya angka attrition rate (rasio pergantian karyawan) yang melampaui **10%**. Tingginya attrition ini memicu biaya rekrutmen ulang yang membengkak, penurunan efisiensi kerja tim, serta potensi hilangnya bakat-bakat potensial perusahaan.

---

## 🚩 Permasalahan Bisnis

1. Seberapa besar pengaruh tingkat lembur dan frekuensi perjalanan bisnis terhadap tingkat attrition karyawan?
2. Seberapa signifikan faktor pendapatan bulanan dan struktur kompensasi finansial dalam memicu keputusan pengunduran diri karyawan?
3. Departemen dan peran pekerjaan mana yang memiliki tingkat attrition paling tinggi dan tergolong kritis?
4. Bagaimana faktor demografi (seperti usia) dan akumulasi pengalaman kerja memengaruhi kecenderungan karyawan untuk melakukan attrition?
5. Bagaimana membangun model machine learning dengan sensitivitas (Recall) dan daya pemisah (ROC-AUC) yang tinggi untuk mendeteksi karyawan berisiko attrition secara dini?

---

## 📊 Business Dashboard

Business Dashboard interaktif ini dirancang menggunakan Data Studio untuk membantu manajemen dan tim Human Resources (HR) Jaya Jaya Maju memantau serta menganalisis berbagai pemicu pengunduran diri karyawan (attrition) secara komprehensif.

Dashboard ini mengintegrasikan seluruh modul analisis data ke dalam tampilan visual yang intuitif, dilengkapi metrik real-time serta filter interaktif:

1. **Metrik Utama (Scorecard KPI)**
   Di bagian atas dashboard, ditampilkan 4 indikator kinerja utama:
   - **Total Employees:** 1,470 Karyawan
   - **Total Attrition:** 179 Karyawan
   - **Attrition Rate:** 12,18%
   - **Avg Monthly Income:** $6.502,93
2. **Komponen Visualisasi & Pemetaan Data**
   - **Gambaran Umum & Demografi Karyawan:**
     - Menampilkan bahwa **Research & Development** (107 orang / 59,8%) dan **Sales** (66 orang / 36,9%) merupakan penyumbang terbesar attrition yang secara akumulatif mencakup **96,7%** dari total pengunduran diri.
     - Mengidentifikasi bahwa puncak attrition didominasi oleh kelompok usia produktif muda (**20–34 tahun**), dengan titik tertinggi pada usia 31 tahun (14 orang) dan 29 tahun (12 orang).
   - **Faktor Beban Kerja & Stres Kerja:**
     - Memvisualisasikan bahwa **54,7%** karyawan yang mengundurkan diri (98 orang) berada dalam kelompok yang mengambil lembur.
     - Menunjukkan bahwa karyawan yang melakukan perjalanan dinas (Rarely & Frequently) menyumbang **93,9%** (168 orang) dari total kasus pengunduran diri.
   - **Peran Pekerjaan & Struktur Kompensasi:**
     - Memaparkan 3 posisi dengan angka pengunduran diri tertinggi, yaitu **Laboratory Technician** (49 orang), **Sales Executive** (39 orang), dan **Research Scientist** (38 orang) yang secara akumulatif menyumbang **70,4%** dari total attrition.
     - Mengungkapkan bahwa **76,0%** attrition (136 orang) menumpuk pada karyawan dengan tingkat kompensasi di bawah $6.000/bulan (kategori Low < $3.000 sebanyak 82 orang dan Mid $3.000–$6.000 sebanyak 54 orang).
   - **Rangkuman Eksekutif & Rekomendasi Strategis:**
     - Menyajikan rangkuman Key Conclusions serta Strategic Recommended Actions berbasis data untuk memudahkan eksekutif dalam mengambil keputusan retensi secara cepat.
3. **Fitur Interaktif & Tautan Akses**
   - **Filter Interaktif:** Dashboard dilengkapi kontrol penyaringan dinamis berdasarkan **Department**, **Gender**, dan **Marital Status** untuk memudahkan eksplorasi data secara lebih spesifik.
   - **Link Dashboard:** [Executive HR Dashboard: Attrition Analysis](https://datastudio.google.com/reporting/516a86d1-dadf-4d39-8ae2-fe69833d44e9)

---

## 🎯 Conclusion

Secara keseluruhan, tingkat attrition karyawan berlabel di perusahaan mencapai **16,9%** (179 dari 1.058 karyawan), yang melampaui ambang batas toleransi ideal sebesar **10%**. Berdasarkan analisis data dan pemodelan yang dilakukan, berikut adalah kesimpulan utama proyek ini:

1. Lembur dan perjalanan dinas terbukti menjadi pendorong utama attrition. Karyawan yang mengambil lembur memiliki attrition rate mencapai **32,0%** (jauh melampaui yang tidak lembur sebesar **10,8%**). Sementara itu, kelompok karyawan yang sering bepergian dinas mencatatkan attrition rate tertinggi sebesar **24,7%**.
2. Pendapatan bulanan dan struktur kompensasi memegang peranan krusial. Karyawan yang mengundurkan diri memiliki median pendapatan jauh lebih rendah (**$3.388**) dibandingkan karyawan yang bertahan (**$5.210**). Analisis feature importance juga menempatkan Monthly Income dan Stock Option Level sebagai faktor finansial utama penentu retensi.
3. Departemen **Sales** menjadi area kerja paling kritis dengan tingkat attrition **20,6%**. Secara spesifik, peran **Sales Representative** mencatatkan attrition rate tertinggi hingga **43,6%**, disusul oleh **Laboratory Technician** (**26,0%**) dan **Human Resources** (**20,7%**).
4. Karyawan berusia lebih muda (**31 tahun**) dan akumulasi pengalaman kerja yang lebih singkat memiliki kecenderungan berpindah kerja yang jauh lebih tinggi dibandingkan karyawan berusia lebih matang (**36 tahun**).
5. Algoritma **Support Vector Machine (SVM)** terpilih sebagai early warning engine terbaik dengan nilai **Recall 75,0%** dan **ROC-AUC 0,8635**. Hasil inferensi pada 412 karyawan unlabeled berhasil mengidentifikasi **90 karyawan (21,8%)** yang berisiko tinggi mengundurkan diri untuk dapat segera diberikan intervensi program retensi secara proaktif.

---

## 💡 Strategic Recommended Actions

1. Melakukan evaluasi dan pembatasan alokasi jam lembur pada departemen dengan tingkat attrition tinggi. Selain itu, terapkan kebijakan cuti pemulihan atau hybrid working bagi kelompok karyawan yang sering bepergian dinas guna mencegah timbulnya burnout.
2. Melakukan salary benchmarking terhadap standar pasar industri, terutama untuk kelompok karyawan dengan batas median pendapatan di bawah $3.500. Tingkatkan juga alokasi Stock Option Level dan insentif berbasis kinerja sebagai pilar retensi finansial jangka panjang.
3. Memberikan perhatian khusus pada peran **Sales Representative** (attrition 43,6%) dengan merestrukturisasi skema komisi dan target penjualan agar lebih realistis. Untuk **Laboratory Technician** (26,0%), tingkatkan fasilitas lingkungan kerja dan jalur apresiasi performa.
4. Menyusun jalur karir yang transparan dan program mentorship khusus bagi karyawan kelompok usia muda (< 35 tahun) serta karyawan dengan masa kerja awal. Langkah ini bertujuan meningkatkan engagement dan loyalitas di tahun-tahun awal karir mereka.
5. Mengintegrasikan model **Support Vector Machine (SVM)** ke dalam alur kerja bulanan HR menggunakan skrip inferensi `predict.py`. Berikan prioritas intervensi proaktif (seperti stay interview, penawaran program pengembangan, atau penyesuaian fasilitas) kepada **90 karyawan unlabeled** yang telah teridentifikasi dalam kategori High Risk berdasarkan Attrition Risk Score.

---

## 🛠️ Tech Stack

| Kategori                    | Teknologi yang Digunakan                                             |
| :-------------------------- | :------------------------------------------------------------------- |
| 🌐 **Programming Language** | `Python`                                                             |
| 🌱 **Environment**          | `Jupyter Notebook`                                                   |
| ⚛️ **Libraries**            | `NumPy`, `pandas`, `Matplotlib`, `seaborn`, `scikit-learn`, `Joblib` |
| ⚡ **Tools**                | `Google Colab`, `Data Studio`                                        |

---

## ⚙️ Petunjuk Pengaturan

1. **Prasyarat**
   - Python 3.11 atau lebih baru.
   - Git terinstal di komputer.

2. **Clone Repositori**

```bash
git clone https://github.com/Fikri-Rouzan/hr-analysis.git
cd hr-analysis
```

3. **Buat Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependensi**

```bash
pip install -r requirements.txt
```

5. **Menjalankan Program**

```bash
python predict.py
```
