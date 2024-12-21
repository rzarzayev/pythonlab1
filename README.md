# pythonlab1
Lab 1
'''
Nəticə etibarilə
verilən:
server_logs.txt
tapşırıqda istənilən:
failed_logins.json          - Bu fayl 5-dən çox uğursuz giriş cəhdi olan IP ünvanlarını saxlamalıdır.

threat_ips.json             - Bu fayl veb server log və təhdid kəşfiyyatı arasında uyğun gələn IP ünvanlarını saxlamalıdır.

combined_security_data.json - Bu fayl uğursuz girişləri və təhdid kəşfiyyatı IP-lərini birləşdirməlidir.

log_analysis.txt            - Bu faylda çıxarılan IP ünvanları və onların uğursuz cəhdləri olmalıdır.

log_analysis.csv            - Bu fayl cədvəl formatında çıxarılan məlumatları özündə saxlamalıdır.
'''

--------------READ  ME -------------
### README: Log Təhlili Proqramı

Bu layihə bir log faylını analiz etmək, uğursuz girişləri və təhlükəli IP-ləri müəyyən etmək, nəticələri müxtəlif formatlarda saxlamaq məqsədilə hazırlanmışdır. Kod Python proqramlaşdırma dilində yazılmışdır və bir `Lab1` adlı sinif daxilində strukturlaşdırılmışdır.

---

### Proqramın Təsviri
Proqram aşağıdakı əsas əməliyyatları yerinə yetirir:
1. Log fayllarını analiz edir (`server_logs.txt` faylından oxuyur).
2. Uğursuz giriş cəhdlərini (HTTP status kodu 400-499 aralığında olan) müəyyən edir.
3. Təhlükəli IP-ləri siyahıya alır və JSON formatında saxlayır.
4. Çoxsaylı uğursuz giriş edən IP-ləri müəyyən edir (5-dən çox uğursuz giriş edənlər).
5. Bütün məlumatları müxtəlif formatlarda (JSON, TXT, CSV) saxlayır.

---

### Quraşdırma və İşlətmə
#### Tələblər:
- Python 3.7 və ya daha yüksək versiya
- Aşağıdakı kitabxanalar quraşdırılmış olmalıdır:
  - `re`
  - `json`
  - `csv`
  - `collections`

#### İşlətmə:
1. **Log faylı**: `server_logs.txt` adlı faylı proqramın yerləşdiyi qovluğa yerləşdirin.
2. **Proqramı çalışdırın**:
   ```bash
   python log_analysis.py
   ```
3. Çıxış faylları aşağıdakı formatlarda yaradılacaq:
   - `ugursuz_giris.txt` - Uğursuz girişlərin siyahısı.
   - `threat_ips.json` - Təhlükəli IP-lərin JSON formatında siyahısı.
   - `combined_security_data.json` - Birləşdirilmiş məlumatlar.
   - `log_analysis.csv` - CSV formatında detallı log məlumatları.

---

 Funksiyalar
Kod aşağıdakı funksiyalara bölünüb:

 **`loq_analiz`**
Log faylını oxuyur, HTTP sorğularını analiz edir və:
- Uğursuz girişləri (`ugursuz_cehd`) müəyyən edir.
- 5-dən çox uğursuz giriş edən IP-ləri (`frequent_failed_logins`) siyahıya alır.

**`ugursuz_girisleri_goster`**
Uğursuz girişləri (`ugursuz_cehd`) siyahıya alır və:
- Bu məlumatları `ugursuz_giris.txt` adlı fayla yazır.
- Siyahını qaytarır.

 **`yaz_threat_ips_json`**
- Təhlükəli IP-ləri (`threat_matches`) analiz edir.
- Onları `threat_ips.json` faylına yazır.
- Təhlükəli IP-lərin siyahısını JSON formatında saxlayır.

 **`combine_data`**
- Uğursuz girişlər və təhlükəli IP-ləri birləşdirir.
- Bu məlumatları `combined_security_data.json` faylına yazır.

**`loglari_yaz_csv`**
- Log məlumatlarını CSV formatında (`log_analysis.csv`) saxlayır.
- Hər bir log girişi haqqında məlumat (IP ünvanı, tarix, HTTP metodu, uğursuz cəhd sayı) fayla yazılır.

---

 Fayl Strukturu
Çıxış faylları:
1. **`ugursuz_giris.txt`**: Hər bir IP ünvanı və onun uğursuz giriş sayı (mətn formatında).
2. **`threat_ips.json`**: Təhlükəli IP-lərin siyahısı (JSON formatında).
3. **`combined_security_data.json`**: Uğursuz girişlər və təhlükəli IP-lərin birləşdirilmiş məlumatı (JSON formatında).
4. **`log_analysis.csv`**: Log məlumatlarının təhlilinin CSV faylı.

---

 Tətbiq Edilə Biləcək Yeniləmələr
- HTTP status kodlarının analizini fərqli qruplar üzrə genişləndirmək (məsələn, 500-599 arası server xətaları üçün əlavə hesabat).
- Qrafik interfeys (GUI) əlavə edərək nəticələri daha vizual hala gətirmək.
- Log faylının formatını fərqli strukturlarda da dəstəkləmək.

---

 Əlaqə
Proqramla bağlı suallarınız və ya problemləriniz varsa, mənimlə əlaqə saxlayın:
**[Turan Rzayev](turanrzali13@gmail.com)**
Uğurlar!
