import requests
from bs4 import BeautifulSoup

def bs4_all_desire_element(url, elements_1, elements_2):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_= elements_2)
    print(elements)

    return elements

def get_specific_element(url, elements_1, elements_2, numero_posicion_elemento):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(elements_1, class_= elements_2)

    return elements[numero_posicion_elemento].get_text()


#### EURO - DOLLAR

#bs4_all_desire_element('https://es.investing.com/currencies/eur-usd', "div", "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]")
euro_dollar = get_specific_element('https://es.investing.com/currencies/eur-usd', "div", "text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]",0)

#### TIEMPO MADRID

#bs4_all_desire_element('https://www.tiempoyradar.es/tiempo/madrid/11298643', "span", "air-temp")
temperature_degree_celsius = get_specific_element('https://www.tiempoyradar.es/tiempo/madrid/11298643', "span", "air-temp", 0)

##### Message box temperature

#bs4_all_desire_element('https://www.tiempoyradar.es/tiempo/madrid/11298643', "div", "weather-text") # Frase tiempo
temperature_information = get_specific_element('https://www.tiempoyradar.es/tiempo/madrid/11298643', "div", "weather-text", 0) # Frase tiempo


#### HIPOTECA y TIPO INTERES

## Interest rates
#bs4_all_desire_element('https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736170236&menu=ultiDatos&idp=1254735576757#:~:text=%C3%9Altima%20Nota%20de%20prensa&text=El%20tipo%20de%20inter%C3%A9s%20medio,en%20el%203%2C38%25.', "td", "derecha sdG")
mean_interest_rates_mortage = get_specific_element('https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736170236&menu=ultiDatos&idp=1254735576757#:~:text=%C3%9Altima%20Nota%20de%20prensa&text=El%20tipo%20de%20inter%C3%A9s%20medio,en%20el%203%2C38%25.', "td", "derecha sdG", 5)


## Hipoteca de 300.000 - VALOR CASA 375.000 - 30 años - mensualidades
mean_interest_rate_float_mortage = float(mean_interest_rates_mortage.replace(",",".")) / 100

cuota_mensual = round((300000 * (mean_interest_rate_float_mortage/12)) / ( 1 - (1/( 1 + (mean_interest_rate_float_mortage/12)) ** 360)), 2)

print(cuota_mensual)


import smtplib

email = "r49652495@gmail.com"
receiver = "victormerida55@gmail.com"

subject = "DAILY IMPORTANT INFORMATION"
message = input("Enter")

text = f"Subject: {subject}\n\n{message}"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email, "kobtjteeystqqqbz")

server.sendmail(email, receiver, text)
