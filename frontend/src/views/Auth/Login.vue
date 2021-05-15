<template>
  <div class="col-md-4 mx-auto">
    <b-form @submit.prevent="onSubmit">
      <b-form-group label="Email" label-for="email-input">
        <b-form-input
          id="email-input"
          v-model="mail"
          type="email"
          required
          placeholder="Введите email"
        />
      </b-form-group>
      <b-form-group label="Пароль" label-for="password-input">
        <b-form-input
          id="password-input"
          v-model="password"
          type="password"
          required
          placeholder="Введите пароль"
        />
      </b-form-group>

      <div>
        <b-form-checkbox class="mb-4" v-model="rememberMe">Запомнить меня</b-form-checkbox>
        <b-button type="submit" variant="primary">Войти</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      mail: '',
      password: '',
      rememberMe: true,
    };
  },
  methods: {
    async onSubmit() {
      const { mail, password, rememberMe } = this;
      const { data } = await this.$store.dispatch('auth/register', {
        name,
        mail,
        password,
      });
      if (!data) {
        return;
      }
      return this.$router.push({ name: 'files' });
    }
  }
};
</script>