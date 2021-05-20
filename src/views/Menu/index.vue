<template>

  <div class="wrapper">
    <header>
      <div class="navbar">
      
          <div class="navbar-content">
            <ul class="navbar-list">
              <img src="@/images/logo.png" class="logo" />
              <li class="navbar-item" v-for="link in linksDcr" :key="link.title">
                <router-link class="navbar-link" :title="link.title" :to="link.url">{{ link.title }}</router-link>
              </li>
            </ul>
            <ul class="navbar-list" v-if="isAuthenticated">
              <li class="navbar-item" v-for="link in linksMain" :key="link.title">
                <router-link class="navbar-link" :title="link.title" :to="link.url">{{ link.title }}</router-link>
              </li>
            </ul>
            <ul class="navbar-list" v-if="!isAuthenticated">
              <li class="navbar-item">
                <router-link class="navbar-link" :to="'login'">Войти</router-link>
              </li>
              <li class="navbar-item">
                <router-link class="navbar-link" :to="'registration'">Регистрация</router-link>
              </li>
            </ul>
            <ul class="navbar-list" v-else>
              <li class="navbar-item">
                <button @click="onLogout">Выйти</button>
              </li>
              <li class="navbar-item">
                <router-link :to="'personalArea'">Личный кабинет</router-link>
              </li>
            </ul>
          </div>
        
      </div>
      </header>
  </div>

</template>


<style lang="scss">
.navbar-link {
  &.router-link-exact-active {
    color: #5247e7;
  }
}
</style>



<script>
import { mapGetters } from "vuex";

export default {
  name: "Menu",
  data() {
    return {
      linksMain: [
        { title: "Вес слов", url: "/weightWords" },
        { title: "Облако слов", url: "/wordCloud" },
        { title: "Схожесть текстов", url: "/similarityTexts" },
        { title: "Количественный анализ", url: "/quantitativeАnalysis" },
      ],
      linksDcr: [
        { title: "O CAT", url: "/aboutCat" },
        { title: "Виды аналитики", url: "/typesAnalytics" },
      ],
      linksProf: [{ title: "Личный кабинет", url: "/" }],
    };
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "auth/isAuthenticated",
    }),
  },
  methods: {
    onLogout() {
      this.$store.dispatch("auth/logout");
      return;
    },
  },
};
</script>