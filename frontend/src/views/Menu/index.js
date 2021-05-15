import { mainNav } from '@/router/mainNav';
import { mapGetters } from 'vuex';

export default {
  name: 'Menu',
  data() {
    return {
      mainMenu: mainNav,
    };
  },
  computed: {
    ...mapGetters({
      isAuthenticated: 'auth/isAuthenticated',
    }),
  },
  methods: {
    onLogout() {
      this.$store.dispatch('auth/logout');
      return;
    },
  },
};