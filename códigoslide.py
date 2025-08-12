# Importa os módulos necessários do Selenium e o módulo time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurações do navegador Chrome
options = webdriver.ChromeOptions()  # Cria um objeto de opções para o Chrome,
options.add_argument("--start-maximized")  # Inicia o navegador maximizado
options.add_experimental_option("detach", True)  # Mantém o navegador aberto após o script terminar

# Inicializa o driver do Chrome com as opções definidas
driver = webdriver.Chrome(options=options)

# 1. Acessa o site do SENAI-SP
driver.get("https://www.sp.senai.br/")  # Abre a página inicial do SENAI-SP
time.sleep(3)  # Aguarda 3 segundos para garantir que a página carregue

# 2. Clica na aba "Unidades"
try:
    # Localiza o link que contém o texto "Unidades" usando XPath
    unidades_link = driver.find_element(By.XPATH, "//a[contains(text(),'Unidades')]")
    
    # Executa um clique via JavaScript (mais confiável em elementos dinâmicos)
    driver.execute_script("arguments[0].click();", unidades_link)
except Exception as e:
    # Caso ocorra algum erro ao tentar clicar, imprime a mensagem de erro
    print("Erro ao clicar em 'Unidades':", e)

# Aguarda 4 segundos para a página de "Unidades" carregar completamente
time.sleep(4)

# 3. Rola suavemente até o final da página
scroll_pause = 0.5  # Define o tempo de pausa entre os scrolls (meio segundo)
last_height = driver.execute_script("return document.body.scrollHeight")  # Obtém a altura total da página

# Loop para rolar a página até o final
while True:
    driver.execute_script("window.scrollBy(0, 300);")  # Rola 300 pixels para baixo
    time.sleep(scroll_pause)  # Aguarda um pouco para simular rolagem suave
    
    # Calcula a nova posição da rolagem (altura visível + posição atual)
    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
    
    # Se a nova altura for maior ou igual à altura total da página, encerra o loop
    if new_height >= last_height:
        break

import random  # Importa o módulo para gerar números aleatórios

# 4. Localiza todos os botões "Site" das unidades
try:
    botoes_site = driver.find_elements(By.XPATH, "//a[contains(text(),'Site')]")
    total_botoes = len(botoes_site)
    print(f"Encontrados {total_botoes} botões 'Site'.")

    if total_botoes > 0:
        # Escolhe um índice aleatório
        indice_aleatorio = random.randint(0, total_botoes - 1)
        botao_escolhido = botoes_site[indice_aleatorio]

        # Clica no botão aleatório
        driver.execute_script("arguments[0].click();", botao_escolhido)
        print(f"Acessando o site da unidade aleatória #{indice_aleatorio + 1}...")
    else:
        print("Nenhum botão 'Site' encontrado.")
except Exception as e:
    print("Erro ao tentar acessar o site da unidade aleatória:", e)

