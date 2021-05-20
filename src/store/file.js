import $http from '@/api';

const SET_ALL_FILES = 'SET_ALL_FILES';

export default {
    namespaced: true,
    state: {
        files: [],
    },
    mutations: {
        [SET_ALL_FILES](state, payload) {
            state.files = payload;
        },
        [SET_FILE](state, payload) {
            state.files.push(payload)
        },
    },
    actions: {
        async getALLFILES({ commit }) {
            try { const { data } = await $http.get('/,,,,,,,,,,,,,,,,,,,');
                commit(SET_ALL_FILES, data);
                return {
                    data,
                    error: null
                };
            } catch (error) {
                const { data: {message }, status, } = error.response;
                return {
                    data: null,
                    error: {
                        message,
                        status
                    }
                };
            }


        },
        async setFILE(context, files) {
            let { data } = await Axios.post('http://myapiendpoint.com/api/name', {
                files: files
            });
            if (data.status == 200) {
                context.commit('SET_NAME', files);
            }
            //this.$store.dispatch('SET_NAME', your_name);
        },
    },
    getters: {
        allFiles(state) {
            return state
            //let name = this.$store.getters.NAME;
        }
    }
};