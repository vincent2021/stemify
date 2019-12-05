<template>
  <v-container>
    <v-card
        text-center
        wrap
    >
    <v-container>
        <v-file-input
          v-model="selectedFile"
          id="upload"
          accept="audio/mp3"
          placeholder="mp3 files only"
          prepend-icon="mdi-file-music-outline"
          label="Upload your song"
          @change="onFileChange">
        </v-file-input>
     <v-row align="center">
      <v-col class="d-flex" cols="12" sm="6">
        <v-select
          :items="stemList"
          label="# of stems"
          v-model="stem"
        ></v-select>
      </v-col>
     </v-row>

    <v-container>
      <div v-if="selectedFile">
        <v-btn @click="play(0)">Play the original song</v-btn>
      </div>
    </v-container>
    <v-container id="waveform0"></v-container>
    </v-container>
    </v-card>
  </v-container>
</template>

<script>
import WaveSurfer from 'wavesurfer.js';
import api from '@/service/api';

export default {
  name: 'Upload',
  data() {
    return {
      selectedFile: null,
      stemList: ['2', '4', '5'],
      stem: '2',
      convertFiles: null,
      waveforms: [],
      fileType: [],
    };
  },
  mounted() {
    this.$nextTick(() => {
      for (let i = 0; i <= 0; i += 1) {
        this.waveforms[i] = WaveSurfer.create({
          container: '#waveform'.concat(i),
          waveColor: 'orange',
          progressColor: 'navy',
        });
      }
    });
  },
  methods: {
    onFileChange(selectedFile) {
      if (selectedFile) {
        const fileFD = new FormData();
        fileFD.append('file', selectedFile);
        fileFD.append('stem', this.stem);
        api().post('/upload', fileFD).then((ret) => {
          if (ret.status_code !== 404) {
            this.convertFiles = ret.data;
            this.loadOutput(ret.data);
          }
        }).catch((e) => { console.log(e); });
        this.loadAudioFile(selectedFile, 0);
      } else {
        this.selectedFile = null;
      }
    },
    loadOutput(files) {
      const filesApi = 'http://52.47.46.54:5050/file/';
      let i = 1;
      Object.entries(files).forEach(([key, value]) => {
        this.waveforms[i].load(filesApi + value);
        this.fileType[i] = key;
        i += 1;
      });
    },
    loadAudioFile(file) {
      this.waveforms[0].loadBlob(file);
    },
    play(index) {
      const player = this.waveforms[index];
      player.playPause();
    },
  },
};
</script>
