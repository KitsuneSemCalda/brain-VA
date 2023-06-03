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

class FortranFile:
    def __init__(self, term, content):
        self.filename = str(term) + ".f"
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
        
        prompt1 = f"gere um código em prolog definindo regras e fatos sobre o texto a seguir:\n" + content
        gpt3_prolog = Gpt3(prompt1)
        prolog = gpt3_prolog.generate()
        prolog_file = PrologFile(term, prolog)
        prolog_file.create()
        
        prompt2 = f"gere um código em fortran definindo códigos de calculos de forma geral sobre o texto a seguir:\n" + content
        gpt3_fortran = Gpt3(prompt2)
        fortran  = gpt3_fortran.generate()
        gpt3_fortran = Gpt3(f"verifique se o código anterior está completo se não estiver complete: {fortran}")
        fortran = gpt3_fortran.generate()
        fortran_file = FortranFile(term, fortran)
        fortran_file.create()
        pass
pass
