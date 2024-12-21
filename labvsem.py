import re,json,csv
from collections import defaultdict
loq_fayl='server_logs.txt'
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<tarix>[^\]]+)\] "(?P<method>GET|POST|PUT|DELETE) .+ HTTP/1\.\d" (?P<status>\d{3})'
class Lab1:
    def __init__(self):
        self.log_detalları = []
        self.ugursuz_cehd=defaultdict(int)
        self.frequent_failed_logins={}
        self.threat_matches={}
    def loq_analiz(self):
        with open(loq_fayl,'r',encoding='UTF-8') as fayl:
            loq_data=fayl.readlines()
            for line in loq_data:
                axtar=re.search(pattern,line)
                if axtar:
                    self.log_detalları.append(axtar.groupdict())
                    if 400 <= int(axtar.group("status")) < 500:
                        ip=axtar.group("ip")
                        self.ugursuz_cehd[ip]+=1
        self.frequent_failed_logins = {ip: count for ip, count in self.ugursuz_cehd.items() if count > 5}
    def ugursuz_girisleri_goster(self):
        ugursuz_girisler={ip: count for ip, count in self.ugursuz_cehd.items() if count > 0}
        with open("ugursuz_giris.txt","w",encoding='utf-8') as fayl:
            for ip, count in ugursuz_girisler.items():
                fayl.write(f'{ip}: {count} defe ugursuz giris cehdi\n')
        return ugursuz_girisler
    def yaz_threat_ips_json(self, threat_ips):
        self.threat_matches = {ip: count for ip, count in self.ugursuz_cehd.items() if ip in threat_ips}
        with open("threat_ips.json", "w", encoding="utf-8") as file:
            json.dump(self.threat_matches, file, indent=4)
    def combine_data(self):
        combined_data = {
            "frequent_failed_logins": self.frequent_failed_logins,
            "threat_matches": self.threat_matches,
        }
        with open("combined_security_data.json", "w", encoding="utf-8") as file:
            json.dump(combined_data, file, indent=4)
    def loglari_yaz_csv(self):
        with open("log_analysis.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["IP ünvanı", "Tarix", "HTTP metodu", "Uğursuz cəhdlər"])
            for log in self.log_detalları:
                csv_writer.writerow([log["ip"], log["tarix"], log["method"], self.ugursuz_cehd.get(log["ip"], 0)])
ob = Lab1()
ob.loq_analiz()
# Faylları yaratmaq üçün metodları çağırın
ugursuz_girisler = ob.ugursuz_girisleri_goster()
ob.yaz_threat_ips_json(threat_ips=["192.168.1.11", "10.0.0.15"])
ob.combine_data()
ob.loglari_yaz_csv()

