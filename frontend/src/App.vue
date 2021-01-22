<template>
  <div id="app">
    <p>Hello</p>
    <edt-main-wrapper />
  </div>
</template>


<script>
  import edtMainWrapper from './components/edt-main-wrapper'

  export default {
    name: 'app',
    components: {
      edtMainWrapper
    },
    mounted() {
      console.log('OK');
      this.query();
    },
    data () {
      return {

      }
    },
    props: {

    },
    methods: {
      query: function () {
        const request = new XMLHttpRequest();
        const url = 'http://localhost:8000/api/';

        request.open('GET', url);
        request.setRequestHeader('Content-Type', 'application/x-www-form-url');
        request.addEventListener('readystatechange', () => {
          if (request.readyState === 4 && request.status === 200) {
            console.log(request.responseText);
          }
        });
        request.send();
      },

    },
    watch: {

    },
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
