<template>
  <div class="edt-main-wrapper">
    <p>{{title}}</p>
  </div>
</template>

<script>
  export default {
    name: "edt-main-wrapper.vue",
    components: {},
    props: {},
    data() {
      return {
        title: 'Main wrapper'
      }
    },
    computed: {},
    methods: {},
    watch: {},
    mounted() {
      console.log('I am a alive')
    }
  }
</script>

<style scoped>
  .edt-main-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    max-width: 900px;
    margin: 0 auto;
  }
</style>