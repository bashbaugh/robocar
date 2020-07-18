<template>
  <div id="app">
    <Navbar />
    <div class="container">
      <Joystick />
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Joystick from './components/Joystick'

export default {
  name: 'App',
  components: {
    Navbar,
    Joystick
  }
}
</script>

<style>
</style>
