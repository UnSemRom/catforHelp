<template>
  <div>
    <b-navbar toggleable="sm" type="light" variant="light">
      <b-navbar-toggle target="nav-text-collapse"></b-navbar-toggle>

      <b-collapse id="nav-text-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item
            v-for="(item, index) in mainMenu"
            :key="index"
            :to="{ name: item.name }"
          >{{ item.name }}</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <template v-if="!isAuthenticated">
            <b-nav-item :to="'login'">Войти</b-nav-item>
            <b-nav-item :to="'registration'">Регистрация</b-nav-item>
          </template>

          <template v-else>
            <b-nav-item @click="onLogout">Выйти</b-nav-item>
          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script src="./index.js"></script>