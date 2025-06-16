import re
import os
import requests
from playwright.sync_api import sync_playwright

def print_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            print("Instruction")
            print(f.read())
    except FileNotFoundError:
        print("README.md did not found")

print_readme()

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.ing.pl/")
    page.get_by_role("heading", name="ING Bank Śląski (my) korzysta").click()
    page.get_by_role("button", name="Dostosuj").click()
    page.wait_for_timeout(1500)
    page.screenshot(path="wejscie_w_dostosuj.png", full_page=True)

    switch_locator = page.locator('role=switch[name="Cookies analityczne"]')
    switch_locator.wait_for()
    switch_locator.click()
    page.wait_for_timeout(1500)
    page.screenshot(path="Ustawienie_cookie_analitycznych.png", full_page=True)
    page.get_by_role("button", name="Zaakceptuj zaznaczone").click()
    page.get_by_role("link", name="Premium").click()
    page.get_by_role("link", name="Przejdź do kontaktu i pomocy").click()

    cookies_analityczne = context.cookies()
    print("Sprawdzenie ustawień cookie")
    for cookie in cookies_analityczne:
        print(f" - {cookie['name']}")
    assert any(c['name'].startswith('_ga') for c in cookies_analityczne), "Błędne ustawienie cookies, sprawdź test"
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

