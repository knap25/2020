import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# Dane testowe - ("lamerski" hardcode)

class WizzairRegistration(unittest.TestCase):
    """
    Scenariusz testowy: Rejestracja nowego użytkownika na stronie wizzair.com
    """
    def setUp(self):
        """
        Warunki wstępne:
        Przeglądarka otwarta na https://wizzair.com/pl-pl/main-page#/
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")

    def tearDown(self):
        """ Sprzątanie po teście """
        self.driver.quit()


    def test_invalid_email(self):
        """
        Rejestracja nowego użytkownika
        używając adresu email - dane niepoprawne
        (niekompletny email brak '@')
        """
        driver = self.driver
        # KROKI:
        # ======================
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        # Czekam maks. 15 sekund, aż będzie można kliknąć przycisk ZALOGUJ
        # ======================
        zaloguj_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="navigation-menu-signin"]')))
        #zaloguj_btn = driver.find_element_by_css_selector('button[data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        # ======================
        rejestracja_btn = driver.find_element_by_xpath('//button[text()=" Rejestracja "]')
        rejestracja_btn.click()
        # 3. Wprowadź imię
        # ======================
        # 4. Wprowadź nazwisko
        # 5.Wybierz płeć
        # ======================
        # ======================
	    # 6.a Wpipsz kod kraju
        # 6.b. Wpisz nr telefonu
        # ======================
        # 7. Wpisz niepoprawny e-mail (brak '@')
        # ======================
        # 8. Wpisz hasło
        # ======================
        # 9. Wybierz narodowość
        # ======================
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"

        """TEST: SPRAWDZAMY OCZEKIWANY REZULTAT"""

        # Wyszukuję wszystkie błędy
        # Zapisuję widoczne błędy do listy visible_error_notices
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        # Sprawdzam treść widocznego błędu
        sleep(4)

if __name__ == '__main__':
    unittest.main(verbosity=2)