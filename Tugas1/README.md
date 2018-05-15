# Shodan.io Scraper

A simple scraper made with Python 3. This scraper is able to collect data of various services available from hosts according to your search keyword. Maximum result limit is 2000 as shodan only allows free user to view 200 page at most.

### Specification

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan data scraping pada spreadsheet berikut: [Topik Data Scraping](http://bit.ly/TopikDataScraping). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal 10 Mei 2018 pukul 20.00 WIB

3. Dalam mengerjakan tugas 1, calon warga basdat terlebih dahulu melakukan fork project github pada link berikut: https://github.com/wargabasdat/Seleksi-2018/tree/master/Tugas1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan pull request dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada repository tersebut, calon warga basdat harus mengumpulkan file script dan json hasil data scraping. Repository terdiri dari folder src dan data dimana folder src berisi file script/kode yang __WELL DOCUMENTED dan CLEAN CODE__ sedangkan folder data berisi file json hasil scraper.

5. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

    ``` Makefile
    all: clean build run

    clean: # remove data and binary folder

    build: # compile to binary (if you use interpreter, then do not implement it)

    run: # run your binary

    ```

6. Deadline pengumpulan tugas adalah __15 Mei 2018 Pukul 23.59__

7. Tugas 1 akan didemokan oleh masing-masing calon warga basdat

8. Demo tugas mencakup keseluruhan proses data scraping hingga memeroleh data sesuai dengan yang dikumpulkan pada Tugas 1

9. Hasil data scraping ini nantinya akan digunakan sebagai bahan tugas analisis dan visualisasi data

10. Sebagai referensi untuk mengenal data scraping, asisten menyediakan dokumen "Short Guidance To Data Scraping" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

11. Tambahkan juga gitignore pada file atau folder yang tidak perlu di upload, __NB : BINARY TIDAK DIUPLOAD__

12. JSON harus dinormalisasi dan harus di-_preprocessing_
    ```
    Preprocessing contohnya :
    - Cleaning
    - Parsing
    - Transformation
    - dan lainnya
    ```

13. Berikan README yang __WELL DOCUMENTED__ dengan cara __override__ file README.md ini. README harus memuat minimal konten :
    ```
    - Description
    - Specification
    - How to use
    - JSON Structure
    - Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
    - Reference (Library used, etc)
    - Author
    ```
### Usage
1. Configure config file (config.txt)
    ```{
        "username" : "username",
        "password" : "secret",
        "use_proxy" : true,
        "proxy" : "http://username:password@host:port",
        "filename" : "data.json",
        "search_config" :
        {
            "keyword1" :
            {
                "limit" : 2000,
                "start_from" : 0
            },
            "keyword2" :
            {
                "limit" : 100,
                "start_from" : 1
            }
        }
    }
2. run ```make build``` to install dependency (first time only)
3. run ```make run``` to start the scraper

### Result
* The result will be saved to ```data.json``` and ```autosave-keyword.json``` with the following format :
    ```javascript
    {
    "city": CITY,
    "country": COUNTRY,
    "host": IPv4/IPv6,
    "organization": ORGANIZATION_NAME,
    "services":
    [
      {
        "detail": SERVICE_HEADER,
        "name": (ssh, http, etc),
        "port": PORT_NUMBER,
        "protocol": tcp/udp
      },
      ...
    ]

### Screenshot
![](screenshot/ss1.jpg?raw=true)

### Reference
* Library used :
    * Requests (http://docs.python-requests.org/en/master/)
    * BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Author
* Name : Gabriel Bentara Raphael
* Contact : gabriel.bentara@gmail.com
