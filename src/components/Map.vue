<template>
    <div class="reb-Map">
        <span style="position: absolute; background-color: red; color: white;">Map</span>
        <!--
        :coords="[54.62896654088406, 39.731893822753904]"
        :behaviors="['ruler']"
        :controls="['trafficControl']"
        -->
        <yandex-map
                :settings="settings"
                :coords="[57.617499, 39.924038]"
                zoom="10"
                style="width: 100%; height: 100%;"
                :cluster-options="{
                1: {clusterDisableClickZoom: true}
                }"
                :behaviors="[]"
                :controls="[]"
                :placemarks="placemarks"
                map-type="map"
                @map-was-initialized="initHandler"
        />
    </div>

</template>

<!--<script src="https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=c55b9816-9c45-4a43-a45a-4505c813e193" type="text/javascript"></script>-->
<script>
    import { yandexMap/*, ymapMarker*/ } from 'vue-yandex-maps'

    /*const settings = {
        apiKey: 'c55b9816-9c45-4a43-a45a-4505c813e193',
        lang: 'ru_RU',
        coordorder: 'latlong',
        version: '2.1'
    };
*/
    //Vue.use(yandexMap, settings);

    export default {
        name: "Map",
        props: {
            msg: String
        },
        data () {
            return {
                settings: {
                    apiKey: 'c55b9816-9c45-4a43-a45a-4505c813e193',
                    lang: 'ru_RU',
                    coordorder: 'latlong',
                    version: '2.1'
                },
                placemarks: []
            }
        },
        methods: {
            initHandler () {
                console.log('initHandler ГОТОВО');
            }
        },
        components: {
            yandexMap/*, ymapMarker*/
        }
    }
</script>

<style>
.reb-Map {
    width: 100%;
    height: 100%;
}
</style>