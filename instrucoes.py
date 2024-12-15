"""
Funcionalidades Básicas Esperadas

Atendimento:
● RF01: O chatbot deve ser capaz de responder a perguntas
frequentes sobre produtos, serviços e políticas do banco.
● RF03: O chatbot deve oferecer opções de navegação para guiar
o cliente através de informações complexas.
● RF04: O chatbot deve ser capaz de identicar quando uma
solicitação exige atenção humana e direcionar o cliente para o
canal/pessoa adequada (ex: atendente humano, FAQ,
formulário online).

Cotação de Moeda:
● RF05: O chatbot deve fornecer cotações em tempo real de
diferentes moedas.
● RF06: O chatbot deve permitir que o cliente escolha a moeda
de origem e destino.
● RF07: O chatbot deve apresentar as cotações de forma clara e
concisa, incluindo a data e hora da atualização.

Contratação da Moeda:
● RF08: O chatbot deve permitir a contratação da moeda cotada,
solicitando ao usuário o valor que ele deseja contratar na
moeda destino.

Personalização:
● RF09: O chatbot deve se identicar como um representante do
Banco Pine.
● RF10: O chatbot deve utilizar uma linguagem amigável,
informal e prossional.
● RF11: O chatbot deve adaptar sua comunicação ao estilo do
cliente (ex: formal, informal).

Monitoramento e Manutenção:
● RF14: O chatbot deve registrar as interações com os clientes
para fins de análise e aprimoramento.
"""

"""
Orientações técnicas

Front-end
● Vue3
● Vuetify
● NextJS

Back-end
● O back-end deve ser desenvolvido em .NET C# 8.0.
● A arquitetura utilizada deve seguir o modelo DDD
(Domain-Driven Design).
● Utilize o Dapper para acesso ao banco de dados (caso utilize
SQL Server).
● A API criada deve implementar autenticação via Bearer JWT.
● Arquitetura hexagonal
● Clean code

Banco de dados
● O banco de dados utilizado será o SQL Server ou MongoDB
"""

"""
Critérios de Avaliação
● Funcionalidade: Cobertura das funcionalidades especicadas.
● Usabilidade: Experiência do usuário (UX) e Interatividade (UI).
● Inovação: Soluções criativas e ecientes.
● Integração: Capacidade de integração com as APIs e sistemas
existentes.
"""

"""
3. **Definição da Arquitetura Back-end**

   a. **Implementar Domain-Driven Design (DDD)**

      - Criar projetos separados para as camadas: Domínio, Aplicação, Infraestrutura e Interface.
      - No Visual Studio, adicionar novas pastas ou projetos para cada camada.
      - Definir entidades, agregados e repositórios na camada de Domínio.

   b. **Implementar Arquitetura Hexagonal**

      - Definir portas (interfaces) e adaptadores para comunicação entre camadas.
      - Utilizar injeção de dependência para desacoplamento.
      - Configurar os adaptadores de entrada (Controllers) e saída (Repositórios).

4. **Desenvolvimento da API Base**

   a. **Criar projeto Web API**

      - No diretório do back-end, executar:
        ```bash
        dotnet new webapi -o BancoPineChatbot.API
        ```
      - Configurar o projeto para usar a versão correta do .NET.

   b. **Implementar autenticação JWT**

      - Adicionar o pacote NuGet:
        ```shell
        dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer
        ```
      - Configurar os serviços de autenticação no `Program.cs`:
        ```csharp
        builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
            .AddJwtBearer(options => { /* Configurações */ });
        ```
      - Criar métodos para geração e validação de tokens JWT.

   c. **Integrar Dapper para acesso ao banco de dados**

      - Adicionar o pacote NuGet:
        ```shell
        dotnet add package Dapper
        ```
      - Criar conexão com o banco de dados e implementar repositórios usando Dapper.
      - Escrever métodos para operações básicas (CRUD) das entidades.

5. **Integração com API de Cotação de Moedas**

   a. **Implementar serviço de integração**

      - Criar uma classe `ExchangeService` que consome a API.
      - Utilizar `HttpClient` para realizar requisições HTTP.
      - Mapear a resposta para modelos C#.

   b. **Adicionar endpoints na API**

      - Criar controladores que exponham endpoints para o front-end solicitar cotações.
      - Implementar cache se necessário para otimizar chamadas.

8. **Desenvolvimento da Interface do Chatbot**

   a. **Criar projeto Vue.js**

      - No diretório do front-end, executar:
        ```bash
        vue create banco-pine-chatbot
        ```
      - Selecionar as configurações necessárias (Router, Vuex).

   b. **Configurar Vuetify**

      - Dentro do projeto, adicionar Vuetify:
        ```bash
        vue add vuetify
        ```
      - Personalizar temas de acordo com a identidade visual do banco.

   c. **Desenvolver componentes**

      - Criar componentes para a janela de chat, mensagens e entrada do usuário.
      - Implementar layout responsivo.

9. **Implementação das Funcionalidades de Atendimento**

   a. **Respostas a perguntas frequentes**

      - Conectar o front-end ao endpoint da API para enviar perguntas.
      - Exibir as respostas do modelo de IA na interface do chat.

   b. **Reconhecimento de intenções**

      - Implementar lógica no back-end para identificar a intenção do usuário.
      - Direcionar para respostas ou ações adequadas.

   c. **Navegação guiada**

      - Oferecer opções pré-definidas para tópicos complexos.
      - Implementar botões ou quick replies na interface.

   d. **Encaminhamento para atendimento humano**

      - Identificar quando uma solicitação não pode ser atendida pelo chatbot.
      - Fornecer informações de contato ou formulário para suporte humano.

10. **Implementação da Cotação de Moedas no Chatbot**

    a. **Fornecer cotações**

       - No front-end, implementar ação para solicitar cotação.
       - Enviar requisições ao endpoint específico no back-end.

    b. **Escolha de moedas**

       - Criar componentes de seleção para moeda de origem e destino.
       - Validar inputs no front-end.

    c. **Exibir cotações**

       - Mostrar o valor da cotação, data e hora na interface.
       - Garantir clareza e concisão na apresentação.

11. **Implementação da Contratação de Moeda**

    a. **Solicitar valor ao usuário**

       - Após mostrar a cotação, perguntar se o usuário deseja contratar.
       - Coletar o valor desejado na moeda de destino.

    b. **Processar a contratação**

       - Enviar os dados para o back-end para processamento.
       - Simular confirmação ou próximos passos.

15. **Implementação de Monitoramento e Registro**

    a. **Registrar interações**

       - No back-end, implementar logs das conversas (respeitando a privacidade).
       - Armazenar dados em uma base para análise futura.
"""

"""
PRINCIPAIS
FUNCIONALIDADES
• Consultas de Contas: Saldo, extratos, limites e tarifas.
• Produtos Bancários: Informações sobre empréstimos,
financiamentos e cartões.
• Investimentos: Detalhes de aplicações, simulações e taxas.
• Cotações de Moedas e Commodities: Valores atualizados em
tempo real.
• Perguntas Frequentes: Orientações sobre abertura de conta,
renegociação e mais.
• Integração Multicanal: Disponibilidade no site, aplicativo e
WhatsApp.

REQUISITOS TÉCNICOS

FRONT END
Vue3 Vuetify Nuxt
Ao combinar Vue3, Vuetify e Nuxt, obtém-se um desenvolvimento ágil,
visual consistente e ótima performance, aliado a um ecossistema
otimizado para escalabilidade

BACK END
.NET C#
Com o .NET C# 8.0, é possível criar APIs seguras, escaláveis e de alta
performance para front-ends modernos, aproveitando recursos
assíncronos, serialização otimizada e fácil integração com a nuvem.

BANCO DE DADOS
SQL SERVER
Banco relacional que organiza dados em
tabelas com esquema fixo, ideal para
dados estruturados e transações
complexas que exigem integridade
referencial e relações bem definidas.
mongoDB
Banco não relacional que armazena dados em
documentos JSON flexíveis, ideal para dados
não estruturados, aplicações ágeis e modelos
que evoluem rapidamente.
"""

"""
O desafio consiste em criar um chatbot que atenda às seguintes necessidades:

Aumentar a eficiência no atendimento ao cliente: O chatbot deve ser capaz de responder às perguntas mais frequentes dos clientes de forma rápida e precisa, liberando os atendentes humanos para lidar com casos mais complexos. Isso significa que o chatbot precisa ter um conhecimento profundo sobre os produtos e serviços do banco, bem como sobre as políticas e procedimentos internos.

Facilitar o acesso a informações bancárias e cotações de moedas: O chatbot deve fornecer informações relevantes sobre contas, produtos bancários, investimentos e cotações de moedas de forma clara, concisa e fácil de entender. A interface do chatbot deve ser intuitiva e permitir que os usuários naveguem facilmente pelas informações que precisam.

Melhorar a experiência do cliente com um serviço disponível 24/7: O chatbot deve estar disponível a qualquer hora do dia ou da noite, oferecendo suporte e informações aos clientes quando precisarem. Isso significa que o chatbot precisa ser capaz de funcionar de forma autônoma e sem a necessidade de intervenção humana.
Pix pelo Mecanismo Especial de Devolução (MED) 10 min

Reduzir custos operacionais com automação inteligente: A automação de tarefas repetitivas através do chatbot permitirá que o Banco Pine otimize seus recursos e reduza custos operacionais. Isso pode incluir tarefas como agendamento de consultas, envio de lembretes de pagamento e resposta a perguntas simples sobre saldo e extrato.

Consultas de Contas: Saldo, extratos, limites, tarifas e histórico de transações. O chatbot deve ser capaz de fornecer informações detalhadas sobre as contas dos clientes, incluindo saldos, extratos, limites de crédito e tarifas.

Informações sobre Produtos Bancários: Empréstimos, financiamentos, cartões de crédito e débito, seguros e outros produtos. O chatbot deve fornecer informações completas sobre os diferentes produtos e serviços oferecidos pelo banco, incluindo taxas, condições e requisitos de elegibilidade.

Detalhes de Investimentos: Aplicações, simulações de investimentos, taxas e rendimentos. O chatbot deve permitir que os clientes acessem informações sobre seus investimentos, como saldo, performance e histórico de transações.

Cotações de Moedas e commodities: Valores atualizados em tempo real de diversas moedas. O chatbot deve fornecer cotações de moedas atualizadas em tempo real, permitindo que os clientes acompanhem as flutuações do mercado.

Perguntas Frequentes: Respostas para dúvidas comuns sobre abertura de conta, renegociação de dívidas, serviços bancários e outros tópicos relevantes. O chatbot deve ter um banco de dados de perguntas frequentes que possa responder às dúvidas mais comuns dos clientes.
"""