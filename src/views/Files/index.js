import { mapGetters } from 'vuex';

export default {
  name: 'Files',
  data() {
    return {
      empty: {
        name: '',
        description: '',
      }
    };
  },
  computed: {
    ...mapGetters({
      allFiles: 'file/allFiles',
    }),
    uploadedFiles() {
      var files = this.allFiles.files;
      return files;
    }
  },
  async mounted() {
    return await this.$store.dispatch('file/getAllFiles');
  }
}