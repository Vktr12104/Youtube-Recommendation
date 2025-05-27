# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# # 1. Konfigurasi Chrome Driver
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)  # biar browser gak langsung ketutup
# service = Service("C:/Users/vsrng/Documents/chromedriver-win64/chromedriver.exe")

# driver = webdriver.Chrome(service=service, options=chrome_options)

# # 2. Buka halaman YouTube History
# driver.get("https://myactivity.google.com/product/youtube")

# # 3. Tunggu user login
# print("✅ Silakan login ke akun Google di browser yang muncul.")
# input("⏳ Tekan ENTER di sini SETELAH kamu login dan halaman histori YouTube muncul...")

# # 4. Scroll ke bawah biar semua data loaded
# for _ in range(10):
#     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#     time.sleep(2)

# # 5. Contoh: Ambil semua item video yang muncul
# items = driver.find_elements(By.TAG_NAME, "a")
# for item in items:
#     print(item.get_attribute("href"))


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# chrome_options = Options()
# # chrome_options.add_experimental_option("detach", True)  # coba comment dulu
# service = Service("C:/Users/vsrng/Documents/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get("https://www.youtube.com/feed/history")
# print("✅ Silakan login ke akun Google di browser...")
# time.sleep(30)  # kasih waktu login tanpa input()

# # scroll untuk load data
# for _ in range(10):
#     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#     time.sleep(2)

# # lanjut ambil data
# videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")

# for video in videos:
#     try:
#         title = video.find_element(By.ID, "video-title").text
#         creator = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a").text
#         watched_time = video.find_element(By.CSS_SELECTOR, "div#metadata-line span:nth-child(2)").text

#         print(f"Judul: {title}")
#         print(f"Creator: {creator}")
#         print(f"Ditonton: {watched_time}")
#         print("-" * 40)
#     except:
#         pass

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# options = Options()
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--disable-extensions")
# options.add_argument("--no-first-run")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-infobars")
# options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# service = Service("C:/Users/vsrng/Documents/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.youtube.com/feed/history")

# # Tunggu user login manual
# input("Login dan tekan ENTER setelah halaman history terbuka...")

# # Coba tutup popup consent cookie jika ada
# try:
#     accept_button = driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]")
#     accept_button.click()
#     print("Popup consent cookies ditutup")
# except:
#     print("Tidak ada popup consent cookies")

# try:
#     for i in range(10):
#         if len(driver.window_handles) == 0:
#             print("Window sudah tertutup, berhenti.")
#             break
#         driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#         time.sleep(2)

#     videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")
#     for video in videos:
#         title = video.find_element(By.CSS_SELECTOR, "yt-formatted-string.style-scope.ytd-video-renderer").text
#         creator = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a.yt-simple-endpoint").text
#         views_elements = video.find_elements(By.CSS_SELECTOR, "span.inline-metadata-item.style-scope.ytd-video-meta-block")
#         views = views_elements[0].text if views_elements else "N/A"
#         print(f"Title: {title}\nCreator: {creator}\nViews: {views}\n---")

# except Exception as e:
#     print(f"Error during scraping: {e}")

# finally:
#     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd  # import pandas

# options = Options()
# options.add_argument("--disable-popup-blocking")
# options.add_argument("--disable-extensions")
# options.add_argument("--no-first-run")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-infobars")
# options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# service = Service("C:/Users/vsrng/Documents/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.youtube.com/feed/history")

# input("Login dan tekan ENTER setelah halaman history terbuka...")

# try:
#     try:
#         accept_button = driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]")
#         accept_button.click()
#         print("Popup consent cookies ditutup")
#     except:
#         print("Tidak ada popup consent cookies")

#     for i in range(10):
#         if len(driver.window_handles) == 0:
#             print("Window sudah tertutup, berhenti.")
#             break
#         driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#         time.sleep(2)

#     videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")

#     data_list = []  # tampung data video disini

#     for video in videos:
#         title = video.find_element(By.CSS_SELECTOR, "yt-formatted-string.style-scope.ytd-video-renderer").text
#         creator = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a.yt-simple-endpoint").text
#         views_elements = video.find_elements(By.CSS_SELECTOR, "span.inline-metadata-item.style-scope.ytd-video-meta-block")
#         views = views_elements[0].text if views_elements else "N/A"

#         # Tambahkan ke list sebagai dict
#         data_list.append({
#             "Title": title,
#             "Creator": creator,
#             "Views": views
#         })

#     # Buat DataFrame dari list dict
#     df = pd.DataFrame(data_list)

#     # Print dataframe
#     print(df)

#     # Simpan ke CSV (opsional)
#     df.to_csv("youtube_history.csv", index=False)
#     print("Data berhasil disimpan ke youtube_history.csv")

# except Exception as e:
#     print(f"Error during scraping: {e}")

# finally:
#     driver.quit()


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
