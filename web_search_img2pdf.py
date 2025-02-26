#Web image Search Grid 


# Gerekli paketleri yükleyin (Eğer henüz yüklemediyseniz)
#!pip install playwright nest_asyncio
# Playwright tarayıcılarını yükleyin (ilk kullanımda çalıştırın)
#!python -m playwright install

import asyncio
import nest_asyncio
from playwright.async_api import async_playwright

# Mevcut asyncio döngüsüne uyum sağlamak için nest_asyncio uyguluyoruz
nest_asyncio.apply()

async def scroll_to_bottom(page, scroll_delay=100, max_scrolls=30):
    """Sayfayı yavaşça en alta kadar kaydırır."""
    for _ in range(max_scrolls):
        await page.evaluate("window.scrollBy(0, window.innerHeight);")
        await page.wait_for_timeout(scroll_delay)
        current_height = await page.evaluate("document.documentElement.scrollTop + window.innerHeight")
        total_height = await page.evaluate("document.documentElement.scrollHeight")
        if current_height >= total_height:
            break

async def save_page_as_pdf(url, output_pdf):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        # Sayfaya git ve tüm ağ isteklerinin tamamlanmasını bekle
        await page.goto(url, wait_until="networkidle")

        # İstenmeyen öğeleri gizlemek için CSS ekle
        await page.add_style_tag(content="""
            /* Üst kısımdaki header, arama formu, hesap ve logo */
            #gb, .gb_g, .gb_1, .gb_R,
            form[role="search"],
            a[href*="https://accounts.google.com"],
            img[alt="Google"],
            /* Gezinme çubuğu (All, Görseller, Haberler, Alışveriş vb.) */
            #hdtb, .hdtb-mitem,
            /* Alt kısımda bulunan footer/gölge div */
            #foot,
            /* Ayarlar (dişli) simgesi: 'Ayarlar' veya 'Settings' içeren aria-label */
            a[aria-label*="Ayarlar"],
            a[aria-label*="Settings"],
            /* 'More results' yazısı ve dişli simgesi içeren öğe */
            g-section-with-header,
            /* Gölge efekti veren div'ler */
            div[style*="box-shadow"] {
                display: none !important;
            }
        """)

        # Sayfanın en altına kadar kaydırarak tüm içeriklerin yüklenmesini sağla
        await scroll_to_bottom(page, scroll_delay=150, max_scrolls=50)
        await page.wait_for_timeout(2000)

        # PDF ayarları
        pdf_options = {
            "path": output_pdf,
            "format": "A4",
            "margin": {"top": "10mm", "right": "1mm", "bottom": "1mm", "left": "1mm"},
            "print_background": True,
            "display_header_footer": False,
        }

        # Sayfayı PDF olarak kaydet
        await page.pdf(**pdf_options)
        print(f"PDF oluşturuldu: {output_pdf}")
        await browser.close()

# Örnek kullanım
url = "https://www.google.com/search?q=helicopter&udm=2"
output_pdf = "output.pdf"

asyncio.run(save_page_as_pdf(url, output_pdf))
