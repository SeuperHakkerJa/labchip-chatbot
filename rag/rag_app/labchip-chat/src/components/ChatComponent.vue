<template>
  <div class="chat-container">
    <div class="chat-header" :style="{ backgroundColor: headerColor }">
      LABCHIP CHATBOT
    </div>
    <div class="messages">
      <div v-for="(msg, index) in chatHistory" :key="index" :class="msg.type">
        <span class="message-content">{{ msg.text }}</span>
      </div>
    </div>
    <div class="input-area">
      <input v-model="userMessage" placeholder="Type a message..." @keyup.enter="sendMessage" />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
      userMessage: '', // Store the current user's input
      chatHistory: []  // Store the history of messages
    };
  },
  methods: {
    sendMessage() {
    axios.post('http://localhost:5000/chat', {
        message: this.userMessage
    })
    .then(response => {
        this.chatHistory.push({
            text: response.data.response,
            type: 'bot'
        });
    })
    .catch(error => {
        console.error("Error communicating with server: ", error);
    });
    
    this.chatHistory.push({
        text: this.userMessage,
        type: 'user'
    });
    this.userMessage = '';
    }

  }
};
</script>

<style scoped>
.chat-container {
  max-width: 100%;
  padding: 5%;
  font-family: 'Arial', sans-serif;
}

.messages {
  height: calc(100vh - 80px);
  border: 1px solid #e1e1e1;
  border-radius: 5px;
  overflow-y: scroll;
  padding: 20px;
  margin-bottom: 20px;
}

.user .message-content {
  display: inline-block;
  background-color: #409EFF;
  border-radius: 15px 15px 0 15px;
  color: white;
  padding: 10px 20px;
  margin: 5px;
  float: right;
  clear: both;
}

.bot .message-content {
  display: inline-block;
  background-color: #e1e1e1;
  border-radius: 15px 15px 15px 0;
  color: #333;
  padding: 10px 20px;
  margin: 5px;
  float: left;
  clear: both;
}

.input-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

input {
  flex: 1;
  padding: 10px 20px;
  margin-right: 10px;
  border-radius: 20px;
  border: 1px solid #e1e1e1;
}

button {
  background-color: #409EFF;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #357ABD;
}

.chat-header {
  padding: 15px 20px;
  font-size: 1.2em;
  font-weight: bold;
  color: white;
  text-align: center;
}
</style>

