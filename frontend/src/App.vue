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
      console.log('app component is running')
    }
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
