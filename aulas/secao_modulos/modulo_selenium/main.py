from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time

# Driver chrome https://googlechromelabs.github.io/chrome-for-testing/


ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER.joinpath("drivers\chromedriver-win64\chromedriver.exe")


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # especificando qual driver será utilizado
    chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)

    # definindo propriedades do nosso navegador
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    chrome = make_chrome_browser()
    chrome.get("https://www.google.com.br/")

    # WebDriverWait nos permite executar comandos no navegador apenas quando certas condições forem respeitadas
    search_input = WebDriverWait(chrome, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "APjFqb"))
    )

    search_input.send_keys("Hello!")
    search_input.send_keys(Keys.ENTER)

    time.sleep(TIME_TO_WAIT)
