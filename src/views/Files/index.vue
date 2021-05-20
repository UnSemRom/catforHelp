<template>
  <div>
    <b-container>
      <b-row v-for="(row, index) in rows" :key="index">
        <b-col v-for="item in row" :key="item.id">
          <router-link :to="{ name: 'file', params: { id: item.id } }" tag="div">
            <b-card
              overlay
              text-variant="white"
              :img-src="item.cover"
              :img-alt="item.name"
            >
              <b-card-text :class="$style.preview">
                <h5>{{ item.name }}</h5>
                <p>{{ item.description }}</p>
              </b-card-text>
              <b-icon-play font-scale="6" />
            </b-card>
          </router-link>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script src="./index.js"></script>
<style src="./index.scss" lang="scss" module></style>