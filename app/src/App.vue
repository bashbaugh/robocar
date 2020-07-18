<template>
  <div id="app">
    <Navbar />
    <b-overlay :show="!ready">
      <div class="container py-3">
      <div class="row">
        <div class="col-md-4">
          <Joystick />
        </div>
        <div class="col-md-4">
          <Controls @sendWebsocketMessage="sendWebsocketMessage" />
        </div>
      </div>
    </div>
    <template v-slot:overlay>
        <div class="text-center">
          <b-spinner type="grow" label="Loading..." variant="info"></b-spinner>
          <p>{{ notReadyText }}</p>
        </div>
      </template>
    </b-overlay>
  </div>
</template>

<script>
import io from 'socket.io-client'
import Navbar from './components/Navbar'
import Joystick from './components/Joystick'
import Controls from './components/Controls'

const socket = io()

export default {
  name: 'App',
  components: {
    Navbar,
    Joystick,
    Controls
  },
  data() {
    return {
      ready: false,
      notReadyText: "Connecting to car, please wait..."
    }
  },
  mounted() {
    socket.on('connect', () => {
      this.ready = true
    })
  },
  methods: {
    sendWebsocketMessage() {

    }
  }
}
</script>

<style>
</style>
