import { ValidationProvider, ValidationObserver, extend } from 'vee-validate';
import { required, email, min, max } from 'vee-validate/dist/rules';

extend('required', {
  ...required,
  message: 'Поле должно быть заполнено',
});

extend('email', {
  ...email,
  message: 'Некорректный e-mail',
});

extend('min', {
  ...min,
  message: 'Не менее {length} символов',
});

extend('max', {
  ...max,
  message: 'Не более {length} символов',
});

export { ValidationProvider, ValidationObserver };