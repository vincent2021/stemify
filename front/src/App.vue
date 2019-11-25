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
      <Home/>
    </v-content>
  </v-app>
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'Stemify',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>
