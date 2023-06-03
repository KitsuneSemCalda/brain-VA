# Brain - VA

Este é um programa Python que utiliza a biblioteca GPT-3 da OpenAI juntamente com a Wikipedia para criar um chatbot capaz de gerar código em Prolog com base em um termo de pesquisa.

## Requisitos

- Python 3.x
- Bibliotecas Python: `html2text`, `beautifulsoup4`, `wikipedia-api`, `python-dotenv`, `openai`

## Como executar

1. Instale as bibliotecas necessárias executando o seguinte comando no terminal:

```bash
pip install -r "requirements.txt"
```

2. Crie um arquivo `.env` no mesmo diretório do código Python e adicione suas chaves de API da OpenAI da seguinte forma:

```bash
cp .env.example > .env

# Modifique com 
OPENAI_API_KEY=SuaChaveAPI
ORG_ID=SuaOrganizacaoID
```
3. Execute o código Python:

```bash
python main.py "termo_de_pesquisa"
```

Substitua `"termo_de_pesquisa"` pelo termo de pesquisa desejado.

## Funcionalidades

- A classe `WikipediaSearch` permite buscar termos na Wikipedia em português e obter informações sobre os resultados encontrados.

- A classe `Gpt3` utiliza a API do GPT-3 para gerar texto com base em um prompt fornecido.

- A classe `PrologFile` cria um arquivo em Prolog com base em um termo e conteúdo fornecidos.

- A classe `FortranFile` cria um arquivo em Fortran com base nos calculos de cada conteudo que foi fornecido.

- A classe `ChatBotFactory` utiliza as classes anteriores para criar um chatbot que busca informações na Wikipedia, gera código em Prolog e Fortran e cria um arquivo correspondente.

- O arquivo `main.py` é responsável por receber o termo de pesquisa como argumento de linha de comando, criar o chatbot e executar as etapas necessárias.

## Limitações e Aviso Legal

Este programa é apenas um exemplo e pode não funcionar corretamente em todas as situações. Além disso, o uso da API GPT-3 pode estar sujeito a restrições e políticas da OpenAI. Certifique-se de seguir as diretrizes e políticas de uso da OpenAI ao utilizar este programa.


