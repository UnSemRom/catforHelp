<template>
  <div class="col-md-4 mx-auto">
    <b-form @submit.prevent="onSubmit">
      <b-form-group label="Имя" label-for="name-input">
        <b-form-input
          id="name-input"
          v-model="name"
          type="text"
          required
          placeholder="Введите имя"
        />
      </b-form-group>
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
        <b-button type="submit" variant="primary">Регистрация</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
export default {
   name: 'Registration',
  data() {
    return {
      name: '',
      mail: '',
      password: '',
    };
  },
  methods: {
    async onSubmit() {
      console.log(mail);
      const { name, mail, password } = this;
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