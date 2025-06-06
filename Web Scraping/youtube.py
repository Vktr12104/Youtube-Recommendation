from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = Options()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--no-first-run")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

service = Service("C:/Users/vsrng/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com/feed/history")
input("Login dan tekan ENTER setelah halaman history terbuka...")

try:
    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]")
        accept_button.click()
        print("Popup consent cookies ditutup")
    except:
        print("Tidak ada popup consent cookies")

    for i in range(10):
        if len(driver.window_handles) == 0:
            print("Window sudah tertutup, berhenti.")
            break
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)

    # Ambil semua elemen dalam urutan
    content_elements = driver.find_elements(By.CSS_SELECTOR, "ytd-item-section-renderer")

    data_list = []

    for section in content_elements:
        try:
            # Ambil tanggal dari header jika ada
            date_element = section.find_element(By.ID, "title")
            current_date = date_element.text.strip()
        except:
            current_date = "Unknown"

        videos = section.find_elements(By.TAG_NAME, "ytd-video-renderer")

        for video in videos:
            try:
                title = video.find_element(By.CSS_SELECTOR, "yt-formatted-string.style-scope.ytd-video-renderer").text
                creator = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a.yt-simple-endpoint").text
                views_elements = video.find_elements(By.CSS_SELECTOR, "span.inline-metadata-item.style-scope.ytd-video-meta-block")
                views = views_elements[0].text if views_elements else "N/A"

                data_list.append({
                    "Date": current_date,
                    "Title": title,
                    "Creator": creator,
                    "Views": views
                })
            except Exception as e:
                print(f"Error parsing video: {e}")
                continue

    # Buat DataFrame
    df = pd.DataFrame(data_list)

    print(df)
    df.to_csv("youtube_history_with_date.csv", index=False)
    print("Data berhasil disimpan ke youtube_history_with_date.csv")

except Exception as e:
    print(f"Error during scraping: {e}")

finally:
    driver.quit()
