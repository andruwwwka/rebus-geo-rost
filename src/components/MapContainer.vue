<template>
    <div class="reb-MapContainer">
        <span style="position: absolute; background-color: red; color: white;">MapCont</span>
        <Map/>
        <CatFilter/>
    </div>
</template>

<script>
    import Map from '@/components/Map.vue'
    import CatFilter from "./CatFilter";

    export default {
        name: "MapContainer",
        components: {
            CatFilter,
            Map
        }
    }
</script>

<style>
.reb-MapContainer {
    height: 100%;
}
</style>