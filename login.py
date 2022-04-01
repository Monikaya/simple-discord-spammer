import os
import undetected_chromedriver as uc
token = input("Token: ")

_options = uc.ChromeOptions()

_options.add_argument("--disable-logging")
_options.add_argument("--no-sandbox")
_options.add_argument("--disable-dev-shm-usage")
_options.add_argument("--incognito")
_options.add_argument("--lang=en")
_options.add_argument("--FontRenderHinting[none]")
print("4mog")
driver = uc.Chrome(options=_options)
print("deez")
driver.get("https://discord.com/login")
driver.execute_script('''
function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 150);
  }
login("''' + token + '''");
''')

input("Click enter to exit")
driver.quit()