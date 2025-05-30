# Basit Web Log Analiz Aracı

Bu Python projesi, basit bir `access.log` dosyasını analiz ederek SQL injection, XSS gibi saldırıları tespit etmeyi amaçlar.

Bu proje, bir web sunucusuna yapılan ziyaretlerin kayıtlarını içeren log dosyalarını inceleyerek, web sitesine yapılan bazı zararlı saldırı girişimlerini tespit etmeyi amaçlar.
Örneğin, kötü niyetli kişiler sitenize zararlı kodlar göndermeye veya veri tabanına zarar vermeye çalışabilir. Bu araç, bu tür saldırı denemelerini bulup size raporlar.

## Log Dosyası Nedir?
Web sitenizi ziyaret eden herkesin yaptığı isteklerin, tarih, saat, IP adresi, yapılan işlem gibi bilgilerin kaydedildiği dosyadır.

Projede kullanılan örnek log dosyası access.log adında ve içinde bazı ziyaret kayıtları bulunuyor.

## Bu Proje Ne Yapar?
Log dosyasını okur, her satırı analiz eder.

İçindeki IP adreslerini, tarih ve saat bilgilerini, ziyaret edilen sayfaları alır.

Sayfalarda şüpheli ifadeler (örneğin <script> veya SQL sorgusu içeren kelimeler) varsa onları tespit eder.

Bulduğu bu şüpheli durumları bir liste halinde raporlar.

Örnek Şüpheli Durumlar
Web sayfasına zararlı kod enjekte etmeye çalışma (XSS saldırısı)

Veri tabanına zarar vermeye çalışma (SQL Enjeksiyonu)

## Kullanımı
1. Proje Dosyalarını İndirin
main.py — Projenin ana çalışma dosyası

log_parser.py — Log dosyasını okuyup satırları parçalayan dosya

detector.py — Şüpheli durumları tespit eden dosya

reporter.py — Bulunan şüpheli durumları raporlayan dosya

access.log — Analiz edilecek örnek log dosyası

2. Python Yüklü Olduğundan Emin Olun
Bu proje Python adlı programlama diliyle yazılmıştır.

3. Komut Satırından Çalıştırın
python main.py

4. Sonuçlar
Program çalıştıktan sonra aynı klasörde findings.json adlı dosya oluşur.Bu dosya, bulunan şüpheli ziyaretlerin ve saldırı girişimlerinin listesini içerir.


## access.log dosyası bu projede kullanılan örnek bir dosyadır.Gerçek sunuculardan farklı olarak, burada sadece örnek olması için birkaç ziyaret kaydı ve saldırı denemesi yer almaktadır.

## Neden Önemli?
Web siteleri saldırılara karşı savunmasız olabilir.

Bu tür bir analiz, site yöneticilerine nereden ve nasıl saldırı yapıldığını göstererek önlem almalarını sağlar.

Proje, temel seviyede böyle bir güvenlik analizi yapmayı kolaylaştırır.
