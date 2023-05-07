def sanitize(content):
    import html2text
    from bs4 import BeautifulSoup
    sanitized_content = BeautifulSoup(content, 'html.parser').get_text()
    convert = html2text.HTML2Text()
    content = convert.handle(sanitized_content)
    content = content.replace("\n\n", "")
    return content

class WikipediaSearch:
    def __init__(self, term) -> None:
        self.term = term
        pass

    def search(self):
        import wikipedia
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
        self.prompt = prompt
        pass

    def generate(self):
        from dotenv import load_dotenv
        import openai
        import os
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.organization = os.getenv("ORG_ID")
        
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = self.prompt,
            max_tokens=1024
        )
        return str(response)
pass

class PrologFile:
    def __init__(self, term, content):
        self.filename = str(term) + ".pl"
        self.content = content
        pass

    def create(self):
        with open(self.filename, 'w') as file:
            file.write(self.content)
        pass
pass

class ChatBotFactory:
    def create_chatbot(self, term):
        wikipedia_search = WikipediaSearch(term)
        page = wikipedia_search.search()
        content = sanitize(page.content)
        prompt = f"gere um código em prolog definindo regras e fatos sobre o texto a seguir:\n" + content
        gpt3 = Gpt3(prompt)
        prolog = gpt3.generate()
        prolog_file = PrologFile(term, prolog)
        prolog_file.create()
        pass
pass
