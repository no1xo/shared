import os
import subprocess
import sys
import json

def run_command(command, cwd=None, shell=True):
    """Bir komutu çalıştırır ve çıktıları ekrana yazdırır."""
    result = subprocess.run(command, shell=shell, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode

def main():
    # Sistem güncellemelerini yap
    print("Sistem güncellemelerini yapılıyor...")
    run_command("sudo apt-get update -y")
    run_command("sudo apt-get upgrade -y")

    # Gerekli paketleri yükle
    print("Gerekli paketler yükleniyor...")
    run_command("sudo apt-get install -y git python3-pip python3-venv")

    # Çalışma dizinini oluştur
    work_dir = os.path.expanduser("~/ollama_openwebui")
    os.makedirs(work_dir, exist_ok=True)

    # Dizine geç
    os.chdir(work_dir)

    # Ollama ve OpenWebUI'yi GitHub'dan klonla
    print("Ollama ve OpenWebUI projeleri GitHub'dan çekiliyor...")
    run_command("git clone https://github.com/ollama/ollama.git")
    run_command("git clone https://github.com/open-webui/open-webui.git")

    # Her iki proje dizinine gidip bağımlılıkları yükle
    for project in ["ollama", "openwebui"]:
        project_dir = os.path.join(work_dir, project)

        if not os.path.isdir(project_dir):
            print(f"{project_dir} dizini mevcut değil.")
            continue

        print(f"{project} dizinine gidiliyor ve sanal ortam oluşturuluyor...")
        os.chdir(project_dir)

        # Python sanal ortamı oluştur ve aktifleştir
        run_command("python3 -m venv env")

        # `source` komutu `bash` shell ile çalıştırılır
        activate_script = os.path.join(project_dir, "env", "bin", "activate")
        
        # Bağımlılıkları yükle
        print(f"{project} bağımlılıkları yükleniyor...")
        run_command(f"bash -c 'source {activate_script} && pip install --upgrade pip && pip install -r requirements.txt'")

        # Konfigürasyon dosyasını oluştur
        config_content = {
            "api_url": "https://api.example.com",
            "api_key": "your_api_key"
        }
        with open("config.json", "w") as config_file:
            json.dump(config_content, config_file, indent=4)

        # Projeyi başlat
        print(f"{project} başlatılıyor...")
        run_command(f"bash -c 'source {activate_script} && nohup python app.py > ../{project}_log.txt 2>&1 &'")

        # Sanal ortamdan çıkış yap
        os.chdir(work_dir)

    print("Ollama ve OpenWebUI başarıyla kuruldu ve başlatıldı.")

if __name__ == "__main__":
    main()
