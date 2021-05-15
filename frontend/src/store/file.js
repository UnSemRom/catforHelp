import $http from '@/api';

const SET_ALL_FILES = 'SET_ALL_FILES';

export default {
    namespaced: true,
    state: {
        files: [],
    },
    mutations: {
        [SET_ALL_FILES](state, payload){
            state.files = payload;
        }
    },
    actions: {
        async getALLFILES( { commit }) {
            try {
                const { data } = await $http.get('/,,,,,,,,,,,,,,,,,,,');

                commit(SET_ALL_FILES, data);

                return {data, error: null};
            } catch(error){
                const {
                    data: { message },
                    status,
                } = error.response;

                return { data: null, error: { message, status}};


            }
            
        }
    },
    getters: {
        allFiles(state){
            return state
        }
    }
};