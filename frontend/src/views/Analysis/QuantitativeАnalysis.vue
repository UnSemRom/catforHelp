<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>
<script>
  export default {
    data(){
      return {
        file: ''
      }
    },

    methods: {

      submitFile(){
            
            let files = new FormData();
            files.append('files[]', this.file);
            console.log(this.file)
            console.log(files.get('files[]'))
            var b;

            axios.post('http://127.0.0.1:5000/comparison_frequency_analysis',
            files,
          ).then(res => {b = res}).then(() => console.log(b.data))
          .catch(function(){
            console.log('Вывести ошибку');
          });

          
      },
       handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>