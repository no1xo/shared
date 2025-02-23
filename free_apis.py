import pandas as pd

data = [
    # Animals
    {"API Adı": "Cat Facts", "URL": "https://alexwohlbruck.github.io", "Açıklama": "Günlük kedi bilgileri"},
    {"API Adı": "Cataas", "URL": "https://cataas.com", "Açıklama": "Kedi servisi: kedi resimleri ve gif'leri"},
    {"API Adı": "Dog API", "URL": "https://dogapi.dog", "Açıklama": "Köpek ırkları ve grupları hakkında eğlenceli bilgiler"},
    {"API Adı": "Dogs", "URL": "https://dog.ceo", "Açıklama": "Stanford Köpek Veri Seti'ne dayalı"},
    {"API Adı": "Foxes", "URL": "https://foxes.cool", "Açıklama": "Farklı etiketlere sahip rastgele tilki resimleri"},
    {"API Adı": "HTTPCat", "URL": "https://http.cat", "Açıklama": "Her HTTP durum kodu için kedi görseli"},
    {"API Adı": "HTTP Dogs", "URL": "https://http.dog", "Açıklama": "Her HTTP durum kodu için köpek görseli"},
    {"API Adı": "Meow Facts", "URL": "https://meowfacts.herokuapp.com", "Açıklama": "Basit bir API; kedi gerçeği döndürür"},
    {"API Adı": "Movebank", "URL": "https://www.movebank.org", "Açıklama": "Hayvanların hareket ve göç verileri"},
    {"API Adı": "Petfinder", "URL": "https://www.petfinder.com", "Açıklama": "Köpek ırkları hakkında bilgi ve resimler"},
    {"API Adı": "RandomBigCat", "URL": "https://randombig.cat", "Açıklama": "Büyük kedilerin rastgele resimleri"},
    {"API Adı": "RandomDog", "URL": "https://random.dog", "Açıklama": "Köpeklerin rastgele resimleri"},
    {"API Adı": "RandomFox", "URL": "https://randomfox.ca", "Açıklama": "Tilkilerin rastgele resimleri"},
    {"API Adı": "RescueGroups", "URL": "https://userguide.rescuegroups.org", "Açıklama": "Evlat edinme"},
    
    # Anime
    {"API Adı": "AnimeNewsNetwork", "URL": "https://www.animenewsnetwork.com", "Açıklama": "Anime sektörü haberleri"},
    {"API Adı": "AOT quotes", "URL": "https://attackontitanquotes.vercel.app", "Açıklama": "Attack on Titan alıntıları API'si"},
    {"API Adı": "Jikan", "URL": "https://jikan.moe", "Açıklama": "Resmi olmayan MyAnimeList API'si"},
    {"API Adı": "Mangadex", "URL": "https://api.mangadex.org", "Açıklama": "Reklamsız manga okuyucu; yüksek kaliteli resimler sunar"},
    {"API Adı": "Nekosia API", "URL": "https://nekosia.cat", "Açıklama": "Sevimli rastgele resimlere sahip anime API'si"},
    
    # Anti-Malware
    {"API Adı": "FishFish", "URL": "https://fishfish.gg", "Açıklama": "Discord güvenliği için gönüllü siber güvenlik projesi"},
    
    # Art & Design
    {"API Adı": "Metropolitan Museum of Art", "URL": "https://metmuseum.github.io", "Açıklama": "Sanat koleksiyonu"},
    
    # Books
    {"API Adı": "British National Bibliography", "URL": "https://bnb.data.bl.uk", "Açıklama": "Kitaplarla ilgili bilgiler"},
    {"API Adı": "Harry Potter API", "URL": "https://harrypotterapi.com", "Açıklama": "Harry Potter kitapları, filmleri, karakterleri ve büyüleri verisi"},
    {"API Adı": "Open Library", "URL": "https://openlibrary.org", "Açıklama": "Kitaplar, kapak resimleri ve ilgili veriler"},
    {"API Adı": "Penguin Publishing", "URL": "https://www.penguinrandomhouse.biz", "Açıklama": "Kitaplar, kapak resimleri ve ilgili veriler"},
    {"API Adı": "Rig Veda", "URL": "https://aninditabasu.github.io", "Açıklama": "Tanrılar ve şairler; vezin ölçüleri, mandal ve sukta numarası"},
    {"API Adı": "Vedic Society", "URL": "https://aninditabasu.github.io", "Açıklama": "Vedik edebiyattaki isimlerin açıklamaları"},
    
    # Business
    {"API Adı": "Domainsdb.info", "URL": "https://domainsdb.info", "Açıklama": "Kayıtlı alan adları araması"},
    {"API Adı": "Favicon.im", "URL": "https://favicon.im", "Açıklama": "Herhangi bir web sitesinin favicon'unu getirir"},
    {"API Adı": "markerapi", "URL": "https://www.markerapi.com", "Açıklama": "Tescil edilmiş marka araması"},
    {"API Adı": "Valid Email", "URL": "https://validemail.io", "Açıklama": "E-posta adreslerini spam ve teslimat için doğrular"},
    
    # Calendar
    {"API Adı": "Byabbe", "URL": "https://byabbe.se", "Açıklama": "Belirli bir gün için Wikipedia tarihlerini arar"},
    {"API Adı": "Church Calendar", "URL": "https://calapi.inadiutorium.cz", "Açıklama": "Katolik litürjik takvimi"},
    {"API Adı": "Czech Namedays Calendar", "URL": "https://svatky.adresa.info", "Açıklama": "Bir ismi arar; isim gününü döndürür"},
    {"API Adı": "Hebrew Calendar", "URL": "https://www.hebcal.com", "Açıklama": "Gregoryen ve İbrani takvim arasında dönüşüm; Şabat ve tatil zamanlarını getirir"},
    {"API Adı": "Non-working Days", "URL": "https://isdayoff.ru", "Açıklama": "Rusya, Ukrayna, Beyaz Rusya ve Kazakistan için çalışma/tatil günlerini kontrol eder"},
    {"API Adı": "Nager.Date", "URL": "https://date.nager.at", "Açıklama": "90'dan fazla ülke için resmi tatiller"},
    {"API Adı": "Namedays Calendar", "URL": "https://api.abalin.net", "Açıklama": "Çeşitli ülkeler için isim günleri sağlar"},
    {"API Adı": "Non-Working Days (ICS)", "URL": "N/A", "Açıklama": "Çalışma günleri olmayan ICS dosyaları veri tabanı"},
    {"API Adı": "Russian Calendar", "URL": "N/A", "Açıklama": "Bir tarihin Rusya tatili olup olmadığını kontrol eder"},
    {"API Adı": "TimeZones iCal Library", "URL": "https://tz.add-to-calendar-technology.com", "Açıklama": "Resmi zaman dilimleri ve iCal VTIMEZONE blokları veri tabanı"},
    
    # Cloud Storage & File Sharing
    {"API Adı": "AnonFiles", "URL": "https://anonfiles.com", "Açıklama": "Dosya paylaşımı ve depolama"},
    {"API Adı": "Mega.nz", "URL": "https://mega.nz", "Açıklama": "Dosya paylaşımı ve depolama"},
    
    # Cryptocurrency
    {"API Adı": "BitcoinCharts", "URL": "https://bitcoincharts.com", "Açıklama": "Bitcoin ağı için finansal ve teknik veriler"},
    {"API Adı": "Blockchain", "URL": "https://www.blockchain.info", "Açıklama": "Bitcoin ödemeleri, cüzdan ve işlem verileri"},
    {"API Adı": "CoinDesk", "URL": "https://www.coindesk.com", "Açıklama": "Bitcoin Fiyat Endeksi"},
    {"API Adı": "Coinlore", "URL": "https://www.coinlore.com", "Açıklama": "Kripto para fiyatları, hacim ve daha fazlası"},
    {"API Adı": "Coinpaprika", "URL": "https://api.coinpaprika.com", "Açıklama": "Kripto para fiyatları, hacim ve daha fazlası"},
    {"API Adı": "CoinRanking", "URL": "https://docs.coinranking.com", "Açıklama": "Canlı kripto para verileri"},
    {"API Adı": "CryptoCompare", "URL": "https://www.cryptocompare.com", "Açıklama": "Kripto paraların karşılaştırılması"},
    {"API Adı": "Cryptonator", "URL": "https://www.cryptonator.com", "Açıklama": "Kripto para döviz kurları"},
    {"API Adı": "Gates.io", "URL": "https://www.gate.io", "Açıklama": "Blockchain varlık değişim platformu"},
    {"API Adı": "Gemini", "URL": "https://docs.gemini.com", "Açıklama": "Kripto para borsası"},
    {"API Adı": "Nexchange", "URL": "https://nexchange2.docs.apiary.io", "Açıklama": "Otomatik kripto para borsa servisi"},
    
    # Currency Exchange
    {"API Adı": "Czech National Bank", "URL": "https://www.cnb.cz", "Açıklama": "Döviz kurlarının derlemesi"},
    {"API Adı": "Frankfurter", "URL": "https://www.frankfurter.app", "Açıklama": "Döviz kurları, para birimi dönüşümü ve zaman serisi verileri"},
    {"API Adı": "ratesapi", "URL": "https://ratesapi.io", "Açıklama": "Ücretsiz döviz kurları ve tarihsel veriler"},
    
    # Data Validation
    {"API Adı": "languagelayer", "URL": "https://languagelayer.com", "Açıklama": "Dil tespiti"},
    {"API Adı": "mailboxlayer", "URL": "https://mailboxlayer.com", "Açıklama": "E-posta adresi doğrulama"},
    {"API Adı": "NumValidate", "URL": "https://numvalidate.com", "Açıklama": "Açık kaynaklı telefon numarası doğrulama"},
    {"API Adı": "numverify", "URL": "https://numverify.com", "Açıklama": "Telefon numarası doğrulama"},
    {"API Adı": "PurgoMalum", "URL": "https://www.purgomalum.com", "Açıklama": "Küfür ve argo içeriğe karşı içerik doğrulaması"},
    {"API Adı": "vatlayer", "URL": "https://vatlayer.com", "Açıklama": "KDV numarası doğrulama"},
    
    # Development
    {"API Adı": "0ms DNS Accelerator", "URL": "https://0ms.dev", "Açıklama": "Herhangi bir DoH sağlayıcısını test edip hızlandırır"},
    {"API Adı": "0ms Get IP", "URL": "https://0ms.dev", "Açıklama": "IP, ISS ve konum bilgisi verir"},
    {"API Adı": "0ms Mirrors", "URL": "https://0ms.dev", "Açıklama": "Web siteleri için önbellek proxy API'si"},
    {"API Adı": "24 Pull Requests", "URL": "https://24pullrequests.com", "Açıklama": "Açık kaynak iş birliği projesi"},
    {"API Adı": "Abacus", "URL": "https://abacus.jasoncameron.dev", "Açıklama": "Olayları takip etmek için basit sayaç servisi"},
    {"API Adı": "Agify.io", "URL": "https://agify.io", "Açıklama": "Bir isme göre tahmini yaş hesaplar"},
    {"API Adı": "APIs.guru", "URL": "https://apis.guru", "Açıklama": "Web API'leri ve OpenAPI şemaları için bir Wikipedia"},
    {"API Adı": "CDNJS", "URL": "https://api.cdnjs.com", "Açıklama": "CDNJS üzerindeki kütüphane bilgileri"},
    {"API Adı": "DigitalOcean Status", "URL": "https://status.digitalocean.com", "Açıklama": "DigitalOcean hizmetlerinin durumu"},
    {"API Adı": "ExtendsClass", "URL": "https://extendsclass.com", "Açıklama": "Basit JSON depolama API'si"},
    {"API Adı": "FontDownloader", "URL": "https://fontdownloader.org", "Açıklama": "Google Fonts'tan web fontlarını yönetir"},
    {"API Adı": "Form2Channel", "URL": "https://form2channel.com", "Açıklama": "Form gönderimlerini Google Sheets, E-posta, Slack veya Telegram'a iletir"},
    {"API Adı": "Genderize.io", "URL": "https://genderize.io", "Açıklama": "Bir isme göre cinsiyet tahmini yapar"},
    {"API Adı": "HTTP2.Pro", "URL": "https://http2.pro", "Açıklama": "HTTP/2 protokol desteğini test eder"},
    {"API Adı": "Image-Charts", "URL": "https://www.image-charts.com", "Açıklama": "Grafik, QR kod ve çizelge üretir"},
    {"API Adı": "ipapi.is", "URL": "https://ipapi.is", "Açıklama": "Şirket ve ASN bilgilerine sahip halka açık IP API'si"},
    {"API Adı": "IPGEO", "URL": "https://api.techniknews.net", "Açıklama": "Kullanışlı bilgilerle ücretsiz IP API'si"},
    {"API Adı": "IPify", "URL": "https://www.ipify.org", "Açıklama": "Basit IP adresi API'si"},
    {"API Adı": "IPinfo", "URL": "https://ipinfo.io", "Açıklama": "Bir başka basit IP adresi API'si"},
    {"API Adı": "ArulJohn.com", "URL": "https://api.aruljohn.com", "Açıklama": "JSON formatında basit IP API'si"},
    {"API Adı": "jsDelivr", "URL": "https://www.jsdelivr.com", "Açıklama": "Paket bilgileri ve indirme istatistikleri"},
    {"API Adı": "JSON 2 JSONP", "URL": "https://json2jsonp.com", "Açıklama": "JSON'u anında JSONP'ye dönüştürür"},
    {"API Adı": "Judge0", "URL": "https://api.judge0.com", "Açıklama": "Kaynak kodu derleyip çalıştırır"},
    {"API Adı": "Let's Validate", "URL": "N/A", "Açıklama": "Web sitelerinde kullanılan teknolojileri ortaya çıkarır ve küçük resim oluşturur"},
    {"API Adı": "License-API", "URL": "N/A", "Açıklama": "choosealicense.com için resmi olmayan REST API'si"},
    {"API Adı": "Nationalize.io", "URL": "https://nationalize.io", "Açıklama": "Bir isme göre milliyeti tahmin eder"},
    {"API Adı": "OOPSpam", "URL": "https://oopspam.com", "Açıklama": "Çoklu spam filtreleme servisi"},
    {"API Adı": "Public APIs", "URL": "N/A", "Açıklama": "Web geliştirme için ücretsiz JSON API'lerin toplu listesi"},
    {"API Adı": "QR code (qrtag.net)", "URL": "https://qrtag.net", "Açıklama": "QR kod ve URL kısaltıcı oluşturur"},
    {"API Adı": "QR code (goqr.me)", "URL": "https://goqr.me", "Açıklama": "QR kod grafiklerini üretir ve çözer"},
    {"API Adı": "QuickChart", "URL": "https://quickchart.io", "Açıklama": "Grafik ve çizelge resimleri üretir"},
    {"API Adı": "ReqRes", "URL": "https://reqres.in", "Açıklama": "AJAX istekleri için barındırılan REST API'si"}
]

df = pd.DataFrame(data)
print(df)
