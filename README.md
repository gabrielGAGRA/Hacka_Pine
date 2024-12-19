# LLM:  
url.py: extrai os links dos botões do site do Banco Pine  
scrapping.py: extrai os textos dos links do Banco Pine e trata para separar com um ponto a cada elemento da pagina, para extrair informações para treinar o chatbot (embedding desses textos em uma vector storage posteriormente)  

fine-tuning.json: fine-tuning para prevenir prompt injection  
prompt_chatbot.txt: prompt para o chatbot, ensina e evita prompt injection  
tools.json: function calling tool para extrair parâmetros de cotação para usar posteriormente no backend pra chamar a API com aqueles parâmetros. Dessa forma, poderiamos criar uma forma inteligente de fazer essa consulta usando o poder de entendimento da LLM  

textos: textos extraidos do site  


# Front-end: 
chatbot.vue: interface em vuetify  


# Back-end:  
Program.cs: Inicializa  
AIController.cs: Faz a logica de chamar a API do gemini  
appsettings.json: Guarda a chave de API de forma segura  
