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
