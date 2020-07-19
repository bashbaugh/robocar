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
          <Controls @sendWebsocketUpdate="sendWebsocketMessage" />
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
import Navbar from './components/Navbar'
import Joystick from './components/Joystick'
import Controls from './components/Controls'

const socket = new WebSocket('ws://' + location.host + '/carsocket')

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
    socket.onopen = (e) => {
      this.ready = true
    }
  },
  methods: {
    sendWebsocketMessage(data) {
      socket.send(JSON.stringify(data))
    }
  }
}
</script>

<style>
</style>
