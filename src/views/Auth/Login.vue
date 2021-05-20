@@ -0,0 +1,136 @@
<template>
  <div class="wrapper-content wrapper-content--fixed">
    <section>
      <div class="container">
        <div class="auth">
          <div class="auth__banner">
            <h1 class="title">Hello banner</h1>
            <img src="@/images/temp.png" />
          </div>
          <div class="auth__form">
            <span class="title">Login</span>
            <form @submit.prevent="onSubmit">
              <div class="form-item" :class="{ errorInput: $v.mail.$error }">
                <input id="email-input" type="email" placeholder="Email" v-model="mail" :class="{ error: $v.mail.$error }" @change="$v.mail.$touch()"/>
                <div class="error" v-if="!$v.mail.required">Field is required</div>
                <div class="error" v-if="!$v.mail.email">Email is not correct</div>
              </div>
              <div class="form-item" :class="{ errorInput: $v.password.$error }">
                <input id="password-input" type="password" placeholder="Password" v-model="password" :class="{ error: $v.password.$error }" @change="$v.password.$touch()"/>
                <div class="error" v-if="!$v.password.required">Password is required.</div>
                <div class="error" v-if="!$v.password.minLength">Password must have at least{{ $v.password.$params.minLength.min }} letters.</div>
              </div>
              <label class="custom-checkbox">
                <input type="checkbox" value="value-1">
                <span>Indigo</span>
              </label>
              <div class="buttons-list">
                <button class="btn btnPrimary" type="submit" :disabled="submitStatus === 'PENDING'">Login</button>
              </div>
              <div class="buttons-list buttons-list--info">
                <p class="" v-if="submitStatus === 'OK'">Thanks for your submission!</p>
                <p class="" v-if="submitStatus === 'ERROR'">Please fill the form correctly.</p>
                <p class="" v-if="submitStatus === 'PENDING'">Sending...</p>
              </div>
              <div class="buttons-list buttons-list--info">
                <span>Need Registration?<router-link to="/registration">Enter Here</router-link></span>
              </div>
              
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { required, email, minLength } from "vuelidate/lib/validators";
export default {
  data() {
    return {
      mail: "",
      password: "",
      rememberMe: true,
      submitStatus: null,
    };
  },

  validations: {
    mail: {
      required,
      email,
    },
    password: {
      required,
      minLength: minLength(6),
    },
  },

  methods: {
    async onSubmit() {
      this.$v.$touch();
      if (this.$v.$invalid) {
        this.submitStatus = "ERROR";
      } else {
        const { mail, password, rememberMe } = this;
        console.log(rememberMe)
        const { data } = await this.$store.dispatch("auth/login", {
          mail,
          password,
        });
        if (!data) {
          this.submitStatus = err.message;
          return;
        } else {
          this.submitStatus = "OK";
        }
        return this.$router.push({ name: "files" });
      }
    },
  },
};
</script>

<style scoped>
.auth {
  display: flex;
}
.auth__banner,
.auth__form {
  width: 50%;
}
.form-item .error {
  display: none;
  margin-bottom: 8px;
  font-size: 13.4px;
  color: #fc5c65;
}
.form-item.errorInput .error {
  display: block;
}
input.error {
  border-color: #fc5c65;
  animation: shake 0.3s;
}
.buttons-list {
  text-align: right;
  margin-bottom: 20px;
}
.buttons-list.buttons-list--info {
  text-align: center;
}
.buttons-list.buttons-list--info:last-child {
  margin-bottom: 0;
}
a {
  color: #444ce0;
}

label{
  text-align: left;
}
</style>