import requests
from bs4 import BeautifulSoup


def scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Página acessada com sucesso!")

        soup = BeautifulSoup(response.text, 'html.parser')

        titulos = soup.find_all('h2', class_='post-title')

        print("\nTítulos encontrados:")
        for titulo in titulos:
            print(titulo.get_text())

    else:
        print(f"Erro ao acessar o site. Código de status: {response.status_code}")


def main():
    url = 'https://exemplo-de-site.com/blog'  # Substitua com o URL do site que deseja fazer o scraping
    scraper(url)


if __name__ == '__main__':
    main()

