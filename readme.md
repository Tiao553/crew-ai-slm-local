# crew-ai-slm-local

**crew-ai-slm-local** é um projeto para orquestração de agentes autônomos utilizando o framework CrewAI e modelos de linguagem locais (SLMs), como Ollama ou servidores compatíveis com a API OpenAI. O objetivo é criar pipelines colaborativos de IA, com agentes especializados, rodando totalmente offline ou em ambientes controlados, garantindo privacidade e flexibilidade.

---

## ✨ Visão Geral

Este repositório demonstra como estruturar uma equipe ("crew") de agentes inteligentes, cada um com papéis e tarefas específicas, utilizando modelos de linguagem hospedados localmente. É ideal para experimentação, pesquisa, automação de geração de conteúdo e integração de SLMs em fluxos de trabalho reais.

---

## 📁 Estrutura do Projeto

```
├── agents/               # Definição dos agentes autônomos (ex: pesquisador, escritor)
│   ├── researcher.py
│   └── writer.py
├── docs/                 # Documentação adicional
│   └── readme-select-models-for-use.md
├── main.py               # Script principal para orquestração dos agentes e execução das tarefas
├── models/               # Scripts utilitários para setup dos modelos locais
│   ├── setup-models.sh
│   └── setup_install_ollama.sh
├── outputs/              # Saídas geradas (ex: artigos finais)
│   └── final_article.md
├── requirements.txt      # Dependências do projeto
├── tasks/                # Definição das tarefas para os agentes
│   ├── research_task.py
│   ├── structure_task.py
│   └── writing_task.py
└── utils/                # Utilitários e wrappers para integração com modelos e prompts
    ├── ollama_wrapper.py
    └── prompts.py
```

---

## 🚀 Como Usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure e instale os modelos locais

Você pode usar os scripts em `models/` para instalar e configurar o Ollama ou outros SLMs locais:

```bash
bash models/setup_install_ollama.sh
bash models/setup-models.sh
```

Consulte o arquivo [`docs/readme-select-models-for-use.md`](docs/readme-select-models-for-use.md) para detalhes sobre seleção e configuração de modelos.

### 3. Execute o pipeline principal

```bash
python main.py
```

O resultado final será salvo em `outputs/final_article.md`.

---

## 🧩 Componentes Principais

- **agents/**: Define os agentes, como o pesquisador (`researcher.py`) e o escritor (`writer.py`), cada um com responsabilidades e habilidades específicas.
- **tasks/**: Especifica as tarefas a serem executadas pelos agentes (pesquisa, estruturação, redação).
- **utils/**: Inclui wrappers para integração com modelos locais (ex: `ollama_wrapper.py`) e prompts customizados.
- **models/**: Scripts para setup e instalação dos modelos de linguagem.
- **outputs/**: Diretório para armazenar as saídas geradas pelo pipeline.

---

## 🛠️ Customização

- **Adicionar novos agentes**: Crie um novo arquivo em `agents/` e defina o comportamento desejado.
- **Adicionar/alterar tarefas**: Edite ou crie novos arquivos em `tasks/`.
- **Alterar modelo de linguagem**: Modifique o wrapper em `utils/ollama_wrapper.py` para apontar para o endpoint/modelo desejado.

---

## 📝 Boas Práticas

- Mantenha os scripts de setup de modelos atualizados conforme novas versões dos SLMs.
- Utilize o diretório `outputs/` para versionar e analisar as saídas dos agentes.
- Documente agentes e tarefas para facilitar a colaboração.
- Use ambientes virtuais para isolar as dependências do projeto.

---

## 📚 Documentação

- [docs/readme-select-models-for-use.md](docs/readme-select-models-for-use.md): Guia para seleção e configuração de modelos de linguagem locais.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou novas funcionalidades.

---

## ⚖️ Licença

Este projeto está sob a licença MIT.

---

> Desenvolvido para facilitar a experimentação e integração de agentes inteligentes com modelos de linguagem locais! 🚀

---
Answer from Perplexity: pplx.ai/share