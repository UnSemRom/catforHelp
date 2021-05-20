<style scoped>
input[type="file"] {
  position: absolute;
  top: -500px;
}
div.file-listing {
  width: 200px;
}
span.remove-file {
  color: red;
  cursor: pointer;
  float: right;
}
</style>
<template>
  <section>
    <div class="wrapper-content wrapper-content--fixed">
      <div class="container">
        <div class="large-12 medium-12 small-12 cell">
          <label
            >Files
            <input
              type="file"
              id="files"
              ref="files"
              multiple
              v-on:change="handleFilesUpload()"
            />
          </label>
        </div>
        <div class="large-12 medium-12 small-12 cell">
          <div
            v-for="(file, key) in files"
            v-bind:key="file.id"
            class="file-listing"
          >
            {{ file.name }}
            <span class="remove-file" v-on:click="removeFile(key)">Remove</span>
          </div>
        </div>
        <br />
        <div class="large-12 medium-12 small-12 cell">
          <button v-on:click="addFiles()">Add Files</button>
        </div>
        <br />
        <div class="large-12 medium-12 small-12 cell">
          <button v-on:click="submitFiles()">Submit</button>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  data() {
    return {
      files: [],
    };
  },
  methods: {
    addFiles() {
      this.$refs.files.click();
    },
    submitFiles() {
      let files = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        files.append("files[]", file);
      }
      axios
        .post("http://127.0.0.1:5000/comparison_frequency_analysis", files)
        .then((res) => {
          console.log(res);
        })
        .catch(function () {
          console.log("Вывести ошибку");
        });
    },
    handleFilesUpload() {
      let uploadedFiles = this.$refs.files.files;
      for (var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i]);
      }
    },
    removeFile(key) {
      this.files.splice(key, 1);
    },
  },
};
</script>