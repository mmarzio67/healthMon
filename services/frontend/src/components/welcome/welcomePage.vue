<template>
    <div id="welcome">
        <p>{{ msg }}</p>
      <h1>Time to track some daily activities!</h1>
      <p>Discipline and tracking make your life easy to manage - and now you're just one sign in (or sign up) away from it!</p>
      <div class="cta">
        <router-link to="/signup">Sign Up</router-link>
        <router-link to="/signin">Sign In</router-link>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'PingFastAPI',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
  
  <style scoped>
    #welcome {
      width: 80%;
      margin: auto;
    }
    h1 {
      text-align: center;
    }
    p {
      text-align: center;
    }
    .cta {
      width: 300px;
      margin: auto;
      text-align: center;
    }
    .cta a {
      margin: 10px;
      text-decoration: none;
      display: inline-block;
      border: 1px solid #521751;
      border-radius: 3px;
      width: 100px;
      padding: 10px;
      box-sizing: border-box;
      color: #521751;
    }
    .cta a:hover,
    .cta a:active {
      background-color: #521751;
      color: white;
    }
  </style>
  Footer
  © 2023 GitHub, Inc.