<template>
<div class="py-3">
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
      size: 100
    })
  }
}
</script>

<style>
#joystick-container {
  position: relative;
  width: 500px;
  height: 500px;
  border: 1px solid blue;
}
</style>