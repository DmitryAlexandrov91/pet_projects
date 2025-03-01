"""Бот py - скриптом."""
from bot_classes import DriverManager, HaddanBot
from constants import FIRST_CHAR, PASSWORD


if __name__ == '__main__':
    manager = DriverManager()
    manager.start_driver()

    SwordS = HaddanBot(
        char=FIRST_CHAR,
        password=PASSWORD,
        driver=manager.driver)
    SwordS.login_to_game()

    # Nordman = HaddanBot(
    # char=SECOND_CHAR,
    # password=PASSWORD,
    # driver=driver)
    # Nordman.login_to_game()

    manager.glade_farm()
