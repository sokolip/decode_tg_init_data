import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()


raw_init_data = os.getenv("RAW_INIT_DATA")
def extract_init_data(raw_data: str):
    # Убираем префикс
    if raw_data.startswith("tgWebAppData="):
        raw_data = raw_data[len("tgWebAppData="):]

    # Декодируем
    decoded = urllib.parse.unquote(raw_data)

    return decoded


if __name__ == "__main__":
    
    init_data = extract_init_data(raw_data=raw_init_data)

    print("\nInitData for header:")
    print(init_data)
    print("+++++++++++++++++++++++++++++++++++++++++++")

    print("\nHeader for Postman/curl:")
    print(f"x-telegram-init-data: {init_data}")
