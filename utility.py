import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Utility:

    @staticmethod
    def file_downloader(default_download_folder, download_dir, prefix_text):
        def wait_for_download(download_dir, timeout=180):
            seconds = 0
            downloaded_file = None
            while seconds < timeout:
                try:
                    files = os.listdir(download_dir)
                    entries_with_time = [(entry, os.path.getmtime(os.path.join(download_dir, entry))) for entry in files]
                    # Sort the list by modification time in descending order
                    last_date_sorted_files = sorted(entries_with_time, key=lambda x: x[1], reverse=True)
                    # print(last_date_sorted_files)
                    if files:
                        downloaded_file = last_date_sorted_files[0][0]
                        if downloaded_file:
                            if downloaded_file.endswith('.crdownload') or downloaded_file.endswith('.tmp'):
                                time.sleep(1)
                                seconds += 1
                            else:
                                return downloaded_file
                        else:
                            time.sleep(1)
                            seconds += 1
                    else:
                        time.sleep(1)
                        seconds += 1
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(1)
                    seconds += 1
            return None

        # Wait for the download to complete
        downloaded_file = wait_for_download(default_download_folder)
        try:
            if downloaded_file:
                prefix = prefix_text+"."
                new_filename = prefix + downloaded_file
                old_file_path = os.path.join(default_download_folder, downloaded_file)
                new_file_path = os.path.join(download_dir, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"File downloaded: {new_filename}")
            else:
                print("Download timed out or failed.")
        except Exception as e:
            print(f"Error: {e}")
    





