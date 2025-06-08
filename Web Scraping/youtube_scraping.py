from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService # Explicit import
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
import undetected_chromedriver as uc
# --- Chrome WebDriver Setup for Linux ---
options = ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")

options.add_argument("--disable-infobars") # Good to keep
options.add_argument("--start-maximized") # Often helpful


try:
    # driver = webdriver.Chrome(options=options)
    driver = uc.Chrome(
    options=options,
    version_main = None,
    driver_executable_path = None
)
except Exception as e:
    print(f"Error starting ChromeDriver. Ensure it's in your PATH or specify the path.")
    print(f"Details: {e}")
    print("You might need to install chromedriver. On Fedora, you can try:")
    print("1. If you installed Google Chrome via DNF: sudo dnf install chromedriver")
    print("2. Or download it from https://googlechromelabs.github.io/chrome-for-testing/ and place it in your PATH.")
    exit()

# --- End Chrome WebDriver Setup ---

driver.get("https://www.youtube.com/feed/history")
input("Please login to your Google account in the Chrome window, navigate to your YouTube history page if necessary, and then press ENTER here to continue...")

try:
    # Attempt to close cookie consent pop-up (using your friend's original selector)
    try:
        wait = WebDriverWait(driver, 10)
        # Using your friend's original XPath, but you can also use the more generic one if this fails:
        # //button[contains(.,'Accept all') or contains(.,'Accept') or contains(.,'Setuju')]
        accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept')]")))
        accept_button.click()
        print("Cookie consent pop-up closed.")
    except Exception as e_cookie:
        print(f"Could not close cookie consent pop-up or it was not found: {e_cookie}")

    print("Scrolling to load history...")
    for i in range(10): # Your friend used 10 scrolls
        if not driver.window_handles:
            print("Browser window closed, stopping scroll.")
            break
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        print(f"Scroll attempt {i+1}/10")
        time.sleep(2) # Your friend used 2s, stick with that for Chrome

    print("Finished scrolling. Now extracting data...")
    content_elements = driver.find_elements(By.CSS_SELECTOR, "ytd-item-section-renderer")

    data_list = []

    if not content_elements:
        print("No content sections (ytd-item-section-renderer) found. Page structure might have changed or no history loaded.")

    for section in content_elements:
        current_date = "Unknown Date"
        try:
            # Original selector for date
            date_element = section.find_element(By.ID, "title")
            current_date = date_element.text.strip()
        except Exception:
            # Fallback if the primary ID 'title' for date isn't directly under section
            # This could happen if the structure is slightly different or the date is nested deeper.
            # You might need to refine this if dates are consistently missed.
            try:
                date_element = section.find_element(By.CSS_SELECTOR, ".ytd-item-section-header-renderer #title, #header #title")
                current_date = date_element.text.strip()
            except:
                 pass # Keep "Unknown Date" or previous date if not found

        videos = section.find_elements(By.TAG_NAME, "ytd-video-renderer")

        if not videos:
            print(f"No videos (ytd-video-renderer) found in section with supposed date: {current_date}")

        for video in videos:
            try:
                # Using your friend's original selectors for Chrome
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
            except Exception as e_video:
                print(f"Error parsing a video entry: {e_video}")
                try:
                    # Attempt to get at least the title as a fallback
                    title_attempt = video.find_element(By.CSS_SELECTOR, "a#video-title").get_attribute("title")
                    if title_attempt:
                        data_list.append({
                            "Date": current_date,
                            "Title": title_attempt,
                            "Creator": "N/A (error parsing)",
                            "Views": "N/A (error parsing)"
                        })
                except:
                    print(f"Could not retrieve basic info for a problematic video entry in section: {current_date}")
                continue

    if not data_list:
        print("No data was extracted. Please check the selectors and page content after login.")
    else:
        df = pd.DataFrame(data_list)
        print("\n--- Scraped Data ---")
        print(df.head())
        print(f"\nTotal videos scraped: {len(df)}")

        df.to_csv("youtube_history_chrome_linux.csv", index=False)
        print("\nData successfully saved to youtube_history_chrome_linux.csv")

except Exception as e:
    print(f"An error occurred during the scraping process: {e}")

finally:
    if 'driver' in locals() and driver:
        print("Closing the browser...")
        driver.quit()
