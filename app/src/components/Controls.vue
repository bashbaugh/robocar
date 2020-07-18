<template>
<div>
  <h5><u>Controls</u></h5>
  <div class="p-3">
    <b-button :pressed.sync="controlState.disabled" :variant="controlState.disabled ? 'success' : 'danger'">{{ controlState.disabled ? 'Enable Car' : 'Disable Car' }}</b-button>
  </div>
</div>
</template>

<script>

export default {
  name: 'Joystick',
  data() {
    return {
      controlState: {
          disabled: true
      }
    }
  },
  methods: {
    setControl(control, setting) {
      self.$emit('sendWebsocketMessage', )
    }
  }
}
</script>

<style>
</style>