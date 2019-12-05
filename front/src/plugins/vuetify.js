import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#3f51b5',
        secondary: '#ff5722',
        accent: '#673ab7',
        error: '#f44336',
        warning: '#ff9800',
        info: '#607d8b',
        success: '#4caf50',
      },
    },
  },
});
