import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex);

let store = new Vuex.Store({
    state: {
        products: []
    },
    mutations: {},
    actions: {
        // GET_PRODUCTS_FROM_API({commit}) {
        //     return axios(url, {
        //
        //     })
        // }
    },
    getters: {
        PRODUCTS(state) {
            return state.products;
        }
    }
});

export default store;

