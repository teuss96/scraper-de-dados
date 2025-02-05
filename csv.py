import csv

def salvar_em_csv(titulos):
    with open('titulos_artigos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título'])
        for titulo in titulos:
            writer.writerow([titulo])

def scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Página acessada com sucesso!")
        soup = BeautifulSoup(response.text, 'html.parser')
        titulos = soup.find_all('h2', class_='post-title')
        
        titulos_lista = [titulo.get_text() for titulo in titulos]
        
        salvar_em_csv(titulos_lista)
        print("\nTítulos salvos em 'titulos_artigos.csv'")
    else:
        print(f"Erro ao acessar o site. Código de status: {response.status_code}")
