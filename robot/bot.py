from codecs import encode


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
"""
class Gpt3:
    def __init__(self, prompt) -> None:
        self.prompt = prompt
        pass
    
    def generate(self):
        response = ""
        try:
            from gpt4all import GPT4All
            messages = [
                {
                    "role": "user",
                    "content": self.prompt
                }
            ]
            gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
            full_prompt = gptj._build_prompt(messages, default_prompt_footer=False, default_prompt_header=False)
            response = gptj.generate(full_prompt)
        except Exception:
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
        finally:
            return str(response)
pass
"""

class Gpt3:
    import sys
    def __init__(self):
        try:
            from gpt4all import GPT4All
            self.gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
        except ImportError:
            try:
                from dotenv import load_dotenv
                import openai
                import os
                load_dotenv()
                openai.api_key = os.getenv("OPENAI_API_KEY")
                openai.organization = os.getenv("ORG_ID")
            except ImportError:
                raise ImportError("Nenhuma biblioteca GPT-3 encontrada e as chaves de API do OpenAI não foram configuradas.")

    def generate(self, prompt):
        try:
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            gptj = self.gptj
            full_prompt = gptj._build_prompt(messages, default_prompt_footer=False, default_prompt_header=False)

            response = gptj.generate(full_prompt)

            return str(response)
        except Exception:
            import sys
            sys.exit(1)
    
    def generate_responses(self, prompt):
        import nltk
        nltk.download('punkt')
        from nltk.tokenize import sent_tokenize
        prompt = encode(prompt, "utf-8")
        sentences = sent_tokenize(prompt)
        responses = []

        for sentence in sentences:
            response = self.generate(sentence)
            responses.append(response)

        return responses

class PrologFile:
    def __init__(self, term, content):
        self.filename = str(term).removesuffix(" ").replace(" ", "_") + ".pl"
        self.content = content
        pass

    def create(self):
        with open(self.filename, 'w') as file:
            file.write(self.content)
        pass
pass

class FortranFile:
    def __init__(self, term, content):
        self.filename = str(term).removesuffix(" ").replace(" ", "_")+ ".f"
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

        gpt3 = Gpt3()
        
        prompt1 = f"gere um código em prolog definindo regras e fatos sobre o texto a seguir:\n" + content
        prolog_responses = gpt3.generate_responses(prompt1)
        prolog = '\n'.join(prolog_responses)
        prolog_file = PrologFile(term, prolog)
        prolog_file.create()

        prompt2 = f"gere um código em fortran definindo códigos de cálculos de forma geral sobre o texto a seguir:\n" + content
        fortran_responses = gpt3.generate_responses(prompt2)
        fortran = '\n'.join(fortran_responses)
        gpt3_fortran = Gpt3()
        fortran_check_response = gpt3_fortran.generate(f"verifique se o código anterior está completo. Se não estiver, complete: {fortran}")
        fortran_check_responses = gpt3.generate_responses(fortran_check_response)
        fortran_check = '\n'.join(fortran_check_responses)
        fortran_file = FortranFile(term, fortran_check)
        fortran_file.create()
pass
