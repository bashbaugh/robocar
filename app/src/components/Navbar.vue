<template>
<div>
<b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="#">Robocar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#" disabled>Control Panel</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-navbar-nav>
        <b-nav-item href="#" v-b-modal.about-modal>About</b-nav-item>
      </b-navbar-nav>

        <b-nav-item-dropdown text="Options" right>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <b-icon-power></b-icon-power>
          </template>
          <b-dropdown-item href="#">Shutdown</b-dropdown-item>
          <!--<b-dropdown-item href="#">Sign out</b-dropdown-item>-->
        </b-nav-item-dropdown>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <b-modal id="about-modal" title="Robocar Control Panel" centered>
    <p>This is the Robocar control panel</p>
    <template v-slot:modal-footer>
     <a href="https://github.com/scitronboy/robocar" target="_blank">https://github.com/scitronboy/robocar</a>
    </template>
  </b-modal>
</div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>