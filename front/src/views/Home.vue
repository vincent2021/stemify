<template>
  <div class="home">
    <img alt="Stemify logo" src="../assets/logo.png">
    <Home/>
    <Player/>
    <Upload/>
  </div>
</template>

<script>
// @ is an alias to /src
import Home from '@/components/Home.vue';
import Player from '@/components/Player.vue';
import Upload from '@/components/Upload.vue';

export default {
  name: 'home',
  components: {
    Home,
    Upload,
    Player,
  },
};
</script>
