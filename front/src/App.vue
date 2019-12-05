<template>
  <v-app>
    <v-app-bar
      app
      color="indigo darken-3"
      dark
    >
      <div class="d-flex align-center">
        <h1>Stemify</h1>
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-content>
      <v-layout
        text-center
        wrap
      >
      <v-flex xs12>
          <v-img
            :src="require('@/assets/logo.png')"
            class="my-3"
            contain
            height="200"
          ></v-img>
        </v-flex>

        <v-flex mb-4>
          <h1 class="display-2 font-weight-bold mb-3">
            Welcome to Stemify
          </h1>
          <p class="subheading font-weight-regular">
            Stemify allow you to seperate into stems any song !
          </p>
        </v-flex>
    </v-layout>
      <Home/>
      <Player/>
      <Upload/>
    </v-content>
  </v-app>
</template>

<script>
import Player from '@/components/Player.vue';
import Upload from '@/components/Upload.vue';

export default {
  name: 'Stemify',

  components: {
    Upload,
    Player,
  },

  data: () => ({
    //
  }),
};
</script>
