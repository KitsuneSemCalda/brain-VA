import wikipedia
import html2text
from bs4 import BeautifulSoup

def sanitize(content):
    sanitized_content = BeautifulSoup(content, 'html.parser').get_text()
    convert = html2text.HTML2Text()
    content = convert.handle(sanitized_content)
    return content

class WikipediaSearch:
    def __init__(self, term) -> None:
        self.term = term
        pass

    def search(self):
        wikipedia.set_lang("pt")
        results = wikipedia.search(self.term)
        print(f"Encontrados {len(results)} resultados para {self.term}: ")
        for i, result in enumerate(results):
            print(f"{i + 1}. {result}")
        choice = input("Selecione o número do artigo desejado (ou pressione ENTER para o primeiro resultado): ")
        try:
            index = int(choice) - 1
            if (index < 0 or index >= len(results)):
                index = 0
        except ValueError:
            index = 0
        page = wikipedia.page(results[index])
        return page
pass

class Gpt3:
    def __init__(self, prompt) -> None:
        pass

    def generate(self):
        pass
pass

class PrologFile:
    def __init__(self, term, content):
        pass

    def create(self):
        pass
pass

class ChatBotFactory:
    def create_chatbot(self, term):
        wikipedia_search = WikipediaSearch(term)
        page = wikipedia_search.search()
        content = sanitize(page.content)
        print(content)
        pass
pass
