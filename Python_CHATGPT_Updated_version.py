from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
from datetime import date
import smtplib

def bs4_all_desire_element(url, elements_1, elements_2):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_=elements_2)
    return elements

def get_specific_element(url, elements_1, elements_2, numero_posicion_elemento):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_=elements_2)
    return elements[numero_posicion_elemento].get_text()

def main():
    # FECHA HOY
    today = date.today()
    todays_date = today.strftime("%B %d, %Y")
    print("FECHA HOY ... CORRECTO")

    # EURO - DOLLAR
    euro_dollar = get_specific_element('https://es.investing.com/currencies/eur-usd', "div", "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]", 0)
    print("CAMBIO EURO - DOLLAR ... CORRECTO")

    # TIEMPO MADRID
    temperature_information = get_specific_element('https://www.tiempoyradar.es/tiempo/madrid/11298643', "div", "weather-text", 0)
    temperature_information = unidecode(temperature_information)
    print("TEMPERATURA HOY ... CORRECTO")

    # HIPOTECA y TIPO INTERES
    mean_interest_rates_mortage = get_specific_element('https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736170236&menu=ultiDatos&idp=1254735576757#:~:text=%C3%9Altima%20Nota%20de%20prensa&text=El%20tipo%20de%20inter%C3%A9s%20medio,en%20el%203%2C38%25.', "td", "derecha sdG", 5)
    mean_interest_rates_mortage = ''.join(mean_interest_rates_mortage.split())
    mean_interest_rate_float_mortage = float(mean_interest_rates_mortage.replace(",", ".")) / 100
    cuota_mensual = round((300000 * (mean_interest_rate_float_mortage / 12)) / (1 - (1 / (1 + (mean_interest_rate_float_mortage / 12)) ** 360)), 2)
    print("TIPO INTERES MEDIO HIPOTECA ... CORRECTO")
    print("MENSUALIDAD HIPOTECA ... CORRECTO")

    # NOTICIAS DESTACADAS DEL DIA
    noticia_1 = get_specific_element('https://okdiario.com/', "h2", "segmento-title", 0)
    noticia_2 = get_specific_element('https://okdiario.com/', "h2", "segmento-title", 1)
    noticia_1 = unidecode(noticia_1).strip()
    noticia_2 = unidecode(noticia_2).strip()
    print("NOTICIAS DEL DIA ... CORRECTO")

    # Preparar y enviar el correo electrónico
    email = "r49652495@gmail.com"
    receiver = "victormerida55@gmail.com"
    subject = "DAILY INFORMATION"
    message = (
        f"\nDAILY INFORMATION at {todays_date}\n\n"
        f"TIEMPO: {temperature_information}\n\n"
        f"TIPO MEDIO INTERES HIPOTECA: {mean_interest_rates_mortage} % anual; "
        f"CUOTA MENSUAL HIPOTECA 300.000 EUROS CON TIPOS DE INTERES ACTUALES: {cuota_mensual} euros al mes\n\n"
        f"EURO/DOLLAR EXCHANGE: {euro_dollar} euros por dollar\n\n"
        f"NOTICIAS DEL DIA: 1.: {noticia_1}; 2.: {noticia_2}"
    )

    print("MENSAJE EMAIL ... CORRECTO")

    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, "kobtjteeystqqqbz")
    server.sendmail(email, receiver, text)
    server.quit()
    print("EMAIL ENVIADO")

if __name__ == "__main__":
    main()
