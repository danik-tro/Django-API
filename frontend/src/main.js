import App from './App.vue'
import Vue from 'vue'
import store from './vuex/api'


Vue.config.productionTip = false


new Vue({
    render: h => h(App),
    store
}).$mount('#app')

