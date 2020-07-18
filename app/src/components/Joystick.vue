<template>
<div>
  <h5><u>Joystick</u></h5>
  <div id="joystick-container"></div>
</div>
</template>

<script>
import nipplejs from 'nipplejs'

export default {
  name: 'Joystick',
  mounted() {
    const manager = nipplejs.create({
      zone: document.getElementById('joystick-container'),
      color: '#ffb057',
      size: 100,
      mode: 'semi',
      catchDistance: 100
    })
  }
}
</script>

<style>
#joystick-container {
  position: relative;
  width: 100%;
  height: 400px;
  border: 2px solid #999999;
  border-radius: 8px;
}
</style>