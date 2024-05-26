from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1800,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()


# FUNCAO DE ESCRITA HUMANIZADA
def digitar_naturalmente(text,element):
    for letter in text:
        element.send_keys(letter)
        sleep(random.randint(1,5)/30)



# NAVEGAR ATÉ O SITE
driver.get('https://www.facebook.com')
sleep(random.randint(1,3))

# DIGITAR E-MAIL
campo_email = driver.find_element(By.XPATH, "//input[@id='email']")
text = 'email@email.com'
digitar_naturalmente(text,campo_email)
sleep(random.randint(1,3))

# DIGITAR SENHA
campo_senha = driver.find_element(By.XPATH, "//input[@id='pass']")
password = 'senha123'
digitar_naturalmente(password,campo_senha)
sleep(random.randint(1,3))

# REALIZAR LOGIN
realizar_login = driver.find_element(By.XPATH, "//button[@name='login']")
realizar_login.click()
sleep(8)

# ENCONTRAR E CLICAR NO CAMPO DE POSTAGEM
campo_postagem = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
campo_postagem.click()
sleep(random.randint(1,3))

# DIGITAR NO CAMPO DE STATUS
campo_status = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
status = 'Postagem de exemplo para ver como funciona a automação.'
digitar_naturalmente(status,campo_status)
sleep(random.randint(1,3))

# CLICAR EM PUBLICAR
btn_publicar = driver.find_element(By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
btn_publicar.click()
input('')