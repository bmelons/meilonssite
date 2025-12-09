<template>
  <div class="bigguyspongebob">
    <h1>we got a {{ message }}</h1>
    <div>
      <input v-model="ninput" placeholder="Name"></input>
      <input v-model="tinput" placeholder="Tuah Tuah Tuah"></input>
      <button @click="submit">Submit</button>
    </div>
    <h1> guestbook </h1>
    <div v-for="a in data">
      {{ a.message }} - <b>{{ a.name }}</b>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      message: '',
      data: [],
      ninput: '',
      tinput: ''
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:5000/api/message') // Replace with your Flask API URL
      .then((response) => {
        this.message = response.data.message
      })
      .catch((error) => {
        console.error('Error fetching data:', error)
      });
    this.update();
  },
  methods: {
    update() {
      axios.get("http://127.0.0.1:5000/api/guestbook/entries")
    .then( (response) => this.data = response.data.entries ).catch((error) => {
        console.error('Error fetching data:', error)
      });
    },
    submit() {
      axios.post("http://127.0.0.1:5000/api/guestbook/add", {
        name: this.ninput,
        message: this.tinput
      }).then((response) =>{
        console.log(response);
        this.update();
        this.ninput = '';
        this.tinput = '';
      }
    );

    }
  }
}
</script>

<style>
h1 {
  font-size: 40pt;
}
* {
  font-size: x-large;
}

.bigguyspongebob {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 50vh
}

button {
  height: 4em;
  width: 10em;
}
input {
  height: 4vh;
  width: 10em;
}

</style>
