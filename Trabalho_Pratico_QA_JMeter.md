# 📋 Trabalho Prático: Testes de Desempenho com Apache JMeter

**Disciplina:** Garantia da Qualidade de Software / Testes de Software  
**Professor(a):** Prof. Sauer  
**Valor:** 15,0 Pontos  
**Formato de Entrega:** Individual ou em Dupla  
**Ambiente de Produção Alvo:** [https://qa.sauer.pro.br](https://qa.sauer.pro.br)  

---

## 🎯 1. Objetivo da Atividade

Aplicar na prática os conceitos de **Engenharia de Performance e Qualidade de Software** utilizando o **Apache JMeter** para avaliar o comportamento, tempo de resposta, vazão (*Throughput*) e taxa de erros de uma aplicação web real sob diferentes cenários de carga e estresse.

---

## 🌐 2. Roteiro Prático & Links de Acesso

> 📌 **Atenção:** Todo o roteiro detalhado de execução, catálogo de APIs e tutoriais passo a passo estão disponíveis diretamente nas páginas da aplicação. Acesse os links abaixo para realizar o laboratório:

* 🚀 **Aplicação Alvo:** [https://qa.sauer.pro.br](https://qa.sauer.pro.br)  
  *(Credenciais de teste: Usuário `admin` | Senha `123456`)*
* 📖 **Roteiro do Laboratório & APIs:** [https://qa.sauer.pro.br/documentacao](https://qa.sauer.pro.br/documentacao)  
  *(Seção "Exercício 01: Testes de Carga e Stress com Apache JMeter")*
* 🎓 **Mini Curso Interativo do JMeter:** [https://qa.sauer.pro.br/curso-jmeter](https://qa.sauer.pro.br/curso-jmeter)  
  *(Aprenda a interface, componentes e interpretação das métricas)*
* 📥 **Guia de Instalação do JMeter & Java:** [https://qa.sauer.pro.br/instalacao-jmeter](https://qa.sauer.pro.br/instalacao-jmeter)  
  *(Passo a passo para baixar o Java e descompactar o JMeter)*
* 🐙 **Repositório no GitHub:** [https://github.com/alesauer/qa-testeUnitario](https://github.com/alesauer/qa-testeUnitario)  
  *(Código-fonte e script `.jmx` pré-configurado)*

---

## 📊 3. Tabela de Coleta de Resultados (Preenchimento Obrigatório)

Após executar os testes descritos no portal, preencha a tabela comparativa com os dados consolidados do **Summary Report**:

| Métrica Avaliada no Summary Report | Experimento A: Carga (20 Usuários) | Experimento B: Stress (500 Usuários) |
| :--- | :--- | :--- |
| **Amostras Totais (# Samples)** | | |
| **Tempo Médio de Resposta (Average ms)** | | |
| **Tempo Mínimo (Min ms)** | | |
| **Tempo Máximo (Max ms)** | | |
| **Taxa de Erro (Error %)** | | |
| **Vazão / Throughput (req/seg)** | | |

---

## ❓ 4. Questões Discursivas para o Relatório

Responda às questões abaixo com base nos dados obtidos durante os experimentos:

1. **Desempenho sob Carga Normal:**  
   No Experimento A, o tempo médio de resposta (*Average*) e a taxa de erros (*Error %*) ficaram dentro de limites aceitáveis para a experiência do usuário final? Justifique com os números coletados.

2. **Comportamento no Teste de Stress:**  
   O que aconteceu com a latência e a vazão no Experimento B quando o número de usuários simultâneos aumentou drasticamente? O sistema sofreu lentidão gradual ou colapso?

3. **Diagnóstico dos Gargalos da Aplicação:**  
   Considerando a arquitetura da aplicação (Flask + banco relacional SQLite em arquivo), quais fatores técnicos explicam as falhas e a perda de desempenho sob alta concorrência?

4. **Recomendações Técnicas de QA:**  
   Como Engenheiro(a) de QA, quais melhorias de arquitetura e infraestrutura você recomendaria para que a aplicação suporte 10.000 usuários simultâneos (ex: servidor WSGI, pool de conexões, banco PostgreSQL, Redis, balanceador de carga)?

---

## 📦 5. Entregáveis no Google Classroom

Anexe nesta atividade:

1. 📄 **Relatório Técnico (PDF ou Word):**
   * Identificação do(s) Aluno(s).
   * Tabela de dados preenchida (Seção 3).
   * Respostas das 4 questões dissertativas (Seção 4).
   * **Prints comprobatórios legíveis:**
     * Print do **View Results Tree** com as requisições verdes.
     * Print do **Summary Report** do Teste de Carga.
     * Print do **Summary Report** do Teste de Stress.
2. 💾 **Arquivo do Plano de Testes (`.jmx`):**
   * O arquivo exportado do seu JMeter utilizado nos testes.

---

## ⚖️ 6. Critérios de Avaliação (15,0 Pontos)

| Critério | Descrição | Pontuação |
| :--- | :--- | :---: |
| **Estrutura do Plano de Testes (.jmx)** | Configuração correta de Threads, HTTPS, POST /login, Parâmetros e Response Assertion. | **4,0 pts** |
| **Execução e Coleta das Métricas** | Tabela comparativa preenchida corretamente com dados condizentes dos experimentos. | **4,0 pts** |
| **Análise Crítica e Respostas** | Qualidade técnica e clareza nas respostas das questões de diagnóstico e gargalos. | **5,0 pts** |
| **Evidências e Formatação** | Inclusão de prints legíveis, organização do relatório e envio no prazo. | **2,0 pts** |
| **TOTAL** | | **15,0 pts** |
