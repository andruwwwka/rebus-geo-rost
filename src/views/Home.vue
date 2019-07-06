<template>
  <div class="home">
    <span style="position: absolute; background-color: red; color: white;">Home</span>
    <!--<img alt="Vue logo" src="../assets/logo.png">-->
    <MapContainer/>
  </div>
</template>

<script>
// @ is an alias to /src
import MapContainer from '@/components/MapContainer.vue'

export default {
  name: 'home',
  components: {
    MapContainer
  }
}
</script>

<style>
  .home {
    height: 100%;
  }
</style>
