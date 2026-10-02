# 📋 Trabalho Prático: Testes de Desempenho (Carga e Stress) com Apache JMeter

**Disciplina:** Garantia da Qualidade de Software / Testes de Software  
**Professor(a):** Prof. Sauer  
**Ambiente Alvo:** [https://qa.sauer.pro.br](https://qa.sauer.pro.br)  
**Formato de Entrega:** Individual ou em Dupla (conforme orientação em sala)  

---

## 🎯 1. Objetivo da Atividade

O objetivo deste trabalho prático é aplicar os conceitos de **Engenharia de Performance e Qualidade de Software** utilizando o **Apache JMeter** para avaliar a capacidade, estabilidade, vazão e tempo de resposta de uma aplicação web real em ambiente de produção com terminação SSL segura.

Ao final desta atividade, você será capaz de:
- [x] Configurar planos de testes automatizados de performance no Apache JMeter.
- [x] Diferenciar na prática os objetivos de um **Teste de Carga** vs. **Teste de Stress**.
- [x] Simular múltiplos usuários simultâneos autenticando no sistema.
- [x] Extrair e interpretar métricas reais (*Throughput*, *Average Latency*, *Error %* e *Samples*).
- [x] Redigir um relatório técnico executivo de QA apontando diagnósticos e gargalos do sistema.

---

## 🌐 2. Links e Recursos de Apoio

Antes de iniciar os testes, utilize os materiais interativos disponibilizados na própria aplicação:

| Recurso | Link Direto | Descrição |
| :--- | :--- | :--- |
| 🚀 **Aplicação Web (Alvo)** | [https://qa.sauer.pro.br](https://qa.sauer.pro.br) | Interface de autenticação com usuário e senha. |
| 📖 **Portal de Documentação** | [https://qa.sauer.pro.br/documentacao](https://qa.sauer.pro.br/documentacao) | Arquitetura, catálogo de APIs e roteiro do laboratório. |
| 📥 **Guia de Instalação** | [https://qa.sauer.pro.br/instalacao-jmeter](https://qa.sauer.pro.br/instalacao-jmeter) | Passo a passo para baixar o Java e descompactar o JMeter. |
| 🎓 **Mini Curso do JMeter** | [https://qa.sauer.pro.br/curso-jmeter](https://qa.sauer.pro.br/curso-jmeter) | Explicação visual de cada menu e componente do JMeter. |
| 🐙 **Repositório GitHub** | [github.com/alesauer/qa-testeUnitario](https://github.com/alesauer/qa-testeUnitario) | Código-fonte completo e script `.jmx` de exemplo. |

### 🔑 Credenciais Padrão para os Testes:
* **Usuário:** `admin`
* **Senha:** `123456`

---

## 🛠️ 3. Roteiro Passo a Passo de Execução

### Etapa 1: Preparação do Ambiente
1. Certifique-se de que o **Java** (JRE/JDK 17 ou 21) está instalado em sua máquina executando `java -version` no terminal.
2. Descompacte o Apache JMeter e abra a interface gráfica executando `bin/jmeter.bat` (Windows) ou `./bin/jmeter.sh` (Linux/Mac).

---

### Etapa 2: Construção do Plano de Testes no JMeter
Monte o plano de testes seguindo as instruções abaixo:

1. **Criar Grupo de Usuários (*Thread Group*):**
   * Botão direito em *Test Plan* ➔ *Add* ➔ *Threads (Users)* ➔ *Thread Group*.
2. **Criar Requisição HTTP (*HTTP Request*):**
   * Botão direito em *Thread Group* ➔ *Add* ➔ *Sampler* ➔ *HTTP Request*.
   * **Protocol:** `https`
   * **Server Name or IP:** `qa.sauer.pro.br`
   * **Port Number:** `443`
   * **HTTP Method:** `POST`
   * **Path:** `/login`
   * **Parameters:**
     * `usuario` = `admin`
     * `senha` = `123456`
3. **Adicionar Validação de Resposta (*Response Assertion*):**
   * Botão direito na requisição ➔ *Add* ➔ *Assertions* ➔ *Response Assertion*.
   * Padrão a testar (*Patterns to Test*): `Bem-vindo, admin!`
4. **Adicionar Ouvintes de Resultados (*Listeners*):**
   * Botão direito em *Thread Group* ➔ *Add* ➔ *Listener* ➔ **View Results Tree** (Árvore de Resultados).
   * Botão direito em *Thread Group* ➔ *Add* ➔ *Listener* ➔ **Summary Report** (Relatório de Resumo).

---

### Etapa 3: Executar o Experimento A — Teste de Carga (Load Testing)
* **Objetivo:** Simular o tráfego normal e estável esperado para a aplicação.
* **Configuração no Thread Group:**
  * **Number of Threads (users):** `20`
  * **Ramp-up period (seconds):** `5`
  * **Loop Count:** `5`
* **Ação:** Execute o teste clicando em **▶ (Start)**, aguarde a finalização e anote os dados do **Summary Report**.

---

### Etapa 4: Executar o Experimento B — Teste de Stress (Stress Testing)
* **Objetivo:** Aumentar a concorrência além do limite para descobrir o ponto de ruptura e o comportamento do servidor sob sobrecarga.
* **Ação Prévia:** Limpe os resultados anteriores clicando no ícone de vassouras **🧹 (Clear All)**.
* **Configuração no Thread Group:**
  * **Number of Threads (users):** `300 a 500` *(ou conforme limite de hardware do aluno)*
  * **Ramp-up period (seconds):** `10`
  * **Loop Count:** `10`
* **Ação:** Execute o teste e observe a degradação da latência e o surgimento de erros.

---

## 📊 4. Tabela de Coleta de Resultados (Preenchimento Obrigatório)

Preencha a tabela abaixo com os dados obtidos na aba **Summary Report** do JMeter:

| Métrica Avaliada | Experimento A: Teste de Carga | Experimento B: Teste de Stress | Análise Comparativa |
| :--- | :--- | :--- | :--- |
| **Amostras Totais (# Samples)** | | | *(Ex: 100 vs 5.000)* |
| **Tempo Médio de Resposta (Average ms)** | | | |
| **Tempo Mínimo (Min ms)** | | | |
| **Tempo Máximo (Max ms)** | | | |
| **Taxa de Erro (Error %)** | | | |
| **Vazão / Throughput (req/seg)** | | | |

---

## ❓ 5. Questões Discursivas para o Relatório de QA

Responda fundamentado com os dados coletados nos experimentos:

1. **Qualidade de Serviço na Carga Normal:**  
   No *Experimento A (Carga)*, o tempo médio de resposta e a taxa de erros ficaram dentro de limites aceitáveis para a experiência de um usuário real? Justifique com base nas métricas obtidas.

2. **Diagnóstico do Ponto de Ruptura (Stress):**  
   O que aconteceu com a latência (*Average*) e com a vazão (*Throughput*) quando o volume de requisições foi elevado no *Experimento B (Stress)*? O sistema sofreu degradação suave ou colapso abrupto?

3. **Gargalos da Arquitetura:**  
   Considerando que a aplicação roda em Python Flask com banco relacional SQLite em container Docker, quais são os principais gargalos técnicos que provocam as lentidões e erros quando muitas conexões simultâneas tentam gravar/consultar o banco ao mesmo tempo?

4. **Recomendações de Melhoria:**  
   Como Engenheiro(a) de QA, quais melhorias de infraestrutura e arquitetura você recomendaria para a equipe de desenvolvimento suportar 10.000 usuários simultâneos (ex: servidor WSGI Gunicorn/Uvicorn, pool de conexões, banco PostgreSQL, cache Redis, balanceador de carga)?

---

## 📦 6. O que deve ser Entregue no Google Classroom

Anexe na atividade do Google Classroom os seguintes arquivos:

1. 📄 **Relatório Técnico (PDF ou Word):**
   * Identificação do(s) Aluno(s).
   * Tabela preenchida de coleta de dados (Seção 4).
   * Respostas dissertativas das 4 questões (Seção 5).
   * **Prints comprobatórios legíveis:**
     * Print da tela do **View Results Tree** com as requisições verdes.
     * Print da tela do **Summary Report** do Teste de Carga.
     * Print da tela do **Summary Report** do Teste de Stress.
2. 💾 **Arquivo do Plano de Testes (`.jmx`):**
   * O arquivo exportado do seu JMeter contendo a configuração que você utilizou.

---

## ⚖️ 7. Critérios de Avaliação (100 Pontos)

| Critério | Descrição | Pontuação |
| :--- | :--- | :---: |
| **Estrutura do Plano de Testes (.jmx)** | Configuração correta de Threads, HTTPS, POST /login, Parâmetros e Response Assertion. | **25 pts** |
| **Execução e Coleta das Métricas** | Tabela comparativa preenchida corretamente com dados condizentes dos experimentos. | **25 pts** |
| **Análise Crítica e Respostas** | Qualidade técnica e clareza nas respostas das questões de diagnóstico e gargalos. | **30 pts** |
| **Evidências e Formatação** | Inclusão de prints legíveis, organização do relatório e envio no prazo. | **20 pts** |
| **TOTAL** | | **100 pts** |

---

> 💬 **Dúvidas?** Consulte o portal em [https://qa.sauer.pro.br/documentacao](https://qa.sauer.pro.br/documentacao) ou o Mini Curso em [https://qa.sauer.pro.br/curso-jmeter](https://qa.sauer.pro.br/curso-jmeter). Bom trabalho! 🚀
