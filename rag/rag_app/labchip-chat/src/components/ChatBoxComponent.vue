import axios from 'axios';

<template>
  <div class="chatbox">
    <div class="chat-header" :style="{ backgroundColor: headerColor }">
      LABCHIP CHATBOT666666
    </div>
    <div class="messages">
      <div v-for="(msg, index) in chatHistory" :key="index" :class="msg.type">
        {{ msg.text }}
      </div>
    </div>
    <div class="input-area">
      <input v-model="userMessage" @keyup.enter="sendMessage" />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
export default {

  name: 'ChatComponent',
  props: {
    headerColor: {
      type: String,
      default: '#409EFF' // Default color if none is provided
    }
  },

  data() {
    return {
      userMessage: '',
      chatHistory: []
    };
  },
  methods: {
    sendMessage() {
        axios.post('http://localhost:5000/chat', {
            message: this.userMessage
        })
        .then(response => {
            this.messages.push({
                content: response.data.response,
                type: 'received'
            });
        })
        .catch(error => {
            console.error("Error communicating with server: ", error);
        });
        
        this.messages.push({
            content: this.userMessage,
            type: 'sent'
        });
        this.userMessage = '';
    }
  }
};
</script>

<style scoped>
.chatbox {
  /* Add your styles for the chatbox layout here */
}
.messages {
  /* Style for the chat messages area */
}
.user {
  /* Style for user messages */
}
.bot {
  /* Style for bot (or backend) responses */
}
.input-area {
  /* Style for the input area */
}

.chat-header {
  display: flex;
  justify-content: center;
  align-items: center; /* vertically center the content */
  height: 60px;        /* give it a fixed height for a better appearance */
  padding: 0 20px;     /* padding on the sides */
  font-size: 1.5em;    /* increased font size */
  font-weight: bold;
  color: white;        /* text color set to white */
  text-align: center;
  background-color: var(--header-bg, #409EFF); /* Use a CSS variable with a fallback */
}
</style>

