<template>
  <!-- Use a fluid container to utilize full width -->
  <v-container fluid>
    <!-- Make the row fill the available height -->
    <v-row align="center" justify="center">
      <v-col
        cols="12"
        sm="10"
        md="8"
        lg="6"
        xl="4"
      >    
      <v-card :style="{ backgroundColor: backgroundColor, width: '100%' }" class="chat-card">
          <v-card-title :style="{ color: primaryColor }" class="headline">
            Banco Pine Chatbot
          </v-card-title>
          <!-- Chat Messages -->
          <v-divider></v-divider>
          <v-card-text>
            <div class="chat-window">
              <div v-for="(message, index) in messages" :key="index">
                <div v-if="message.sender === 'user'" class="text-right">
                  <v-chip :color="primaryColor" dark>{{ message.text }}</v-chip>
                </div>
                <div v-else-if="message.sender === 'bot'" class="text-left">
                  <v-chip :color="secondaryColor" dark>{{ message.text }}</v-chip>
                </div>
                <div v-else-if="message.sender === 'options'" class="text-left">
                  <v-btn
                    v-for="(option, idx) in message.options"
                    :key="idx"
                    @click="handleOptionSelection(option)"
                    :color="primaryColor"
                    class="option-button"
                  >
                    {{ option }}
                  </v-btn>
                </div>
                <v-spacer></v-spacer>
              </div>
            </div>
          </v-card-text>
          <!-- Input Field -->
          <v-divider></v-divider>
          <v-card-actions>
            <v-text-field
              v-model="userInput"
              label="Digite sua mensagem"
              @keyup.enter="sendMessage"
              clearable
              hide-details
              outlined
              dense
              full-width
            ></v-text-field>
            <v-btn @click="sendMessage" :color="primaryColor">Enviar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
      userInput: '',
      primaryColor: '#71242B', // Red color
      secondaryColor: '#F9F9F9', // White color
      backgroundColor: '#ffffff',
    };
  },
  methods: {
    async sendMessage() {
      if (this.userInput.trim() === '') return;
      this.addMessage(this.userInput, 'user');
      const userMessage = this.userInput;
      this.userInput = '';

      // Check for special commands or keywords
      if (userMessage.toLowerCase().includes('cotação')) {
        await this.handleCurrencyQuotation();
      } else {
        await this.getBotResponse(userMessage);
      }
    },
    addMessage(text, sender, options = null) {
      if (options) {
        this.messages.push({ sender, options });
      } else {
        this.messages.push({ text, sender });
      }
    },
    async getBotResponse(userInput) {
      const apiKey = 'YOUR_OPENAI_API_KEY'; // Placeholder API key
      const endpoint = 'https://api.openai.com/v1/chat/completions';

      const conversation = [
        { role: 'system', content: 'Você é um assistente virtual do Banco Pine.' },
        ...this.messages
          .filter((msg) => msg.sender !== 'options')
          .map((msg) => ({
            role: msg.sender === 'user' ? 'user' : 'assistant',
            content: msg.text,
          })),
        { role: 'user', content: userInput },
      ];

      try {
        const response = await axios.post(
          endpoint,
          {
            model: 'gpt-3.5-turbo',
            messages: conversation,
          },
          {
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${apiKey}`,
            },
          }
        );
        const botReply = response.data.choices[0].message.content.trim();
        this.addMessage(botReply, 'bot');

        // Offer navigation options for complex information
        this.offerNavigationOptions();

      } catch (error) {
        console.error(error);
        this.addMessage('Desculpe, ocorreu um erro ao processar sua solicitação.', 'bot');
      }
    },
    offerNavigationOptions() {
      const options = ['Cotação de Moedas', 'Falar com Atendente', 'FAQ'];
      this.addMessage(null, 'options', options);
    },
    handleOptionSelection(option) {
      if (option === 'Cotação de Moedas') {
        this.requestCurrencyChoice();
      } else if (option === 'Falar com Atendente') {
        this.addMessage(
          'Redirecionando para um atendente humano. Por favor, aguarde...',
          'bot'
        );
        // Placeholder for redirecting to human attendant
      } else if (option === 'FAQ') {
        this.addMessage('Você pode acessar nossa FAQ em: https://bancopine.com/faq', 'bot');
      }
    },
    requestCurrencyChoice() {
      const options = ['USD para BRL', 'EUR para BRL', 'GBP para BRL'];
      this.addMessage('Por favor, escolha a moeda de origem e destino:', 'bot');
      this.addMessage(null, 'options', options);
    },
    async handleCurrencyQuotation() {
      try {
        const response = await axios.get('https://yourapi.com/api/quotation', {
          params: {
            currencyFrom: 'USD',
            currencyTo: 'BRL'
          },
          headers: {
            Authorization: `Bearer YOUR_JWT_TOKEN`
          }
        });
        const quote = response.data;
        this.displayQuotation(quote);
      } catch (error) {
        console.error(error);
        this.addMessage('Desculpe, ocorreu um erro ao obter a cotação.', 'bot');
      }
    },
    displayQuotation(quote) {
      const message = `Cotação ${quote.currencyPair}: R$ ${quote.value}\nAtualizado em ${quote.date} às ${quote.time}.`;
      this.addMessage(message, 'bot');
      this.addMessage('Deseja contratar esta cotação?', 'bot');
      const options = ['Sim', 'Não'];
      this.addMessage(null, 'options', options);
    },
  },
};
</script>

<style scoped>
.chat-window {
  height: 60vh; /* Set to 60% of viewport height */
  max-height: 65vh; /* Optional: Set a maximum height */
  overflow-y: auto;
  padding-right: 10px;
}
.text-left {
  display: flex;
  justify-content: flex-start;
}
.text-right {
  display: flex;
  justify-content: flex-end;
}
.option-button {
  margin: 5px 5px 0 0;
  color: #ffffff;
}
.quote-card {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 8px;
  margin: 10px 0;
}
.currency-image {
  width: 50px;
  height: 50px;
}
.quote-info {
  text-align: center;
  font-size: 12px;
  color: #666;
}

/* Responsive adjustments */
@media (min-width: 600px) {
  .chat-window {
    height: 60vh;
  }
}

@media (min-width: 960px) {
  .chat-window {
    height: 70vh;
  }
}
</style>