<template>
    <div class="reb-Map">
        <!--<span style="position: absolute; background-color: red; color: white;">Map</span>-->
        <!--
        :coords="[54.62896654088406, 39.731893822753904]"
        :behaviors="['ruler']"
        :controls="['trafficControl']"
        :placemarks="placemarks"
        -->
        <yandex-map
                :settings="settings"
                :coords="[57.617499, 39.924038]"
                zoom="12"
                style="width: 100%; height: 100%;"
                :cluster-options="{
                1: {clusterDisableClickZoom: true}
                }"
                :behaviors="[]"
                :controls="[]"
                map-type="map"
                @map-was-initialized="initHandler"
        >
            <!--<ymap-marker v-for="item in geoData"
                    marker-type="Rectangle"
                    :coords="[[item.lat1, item.lon1], [item.lat2, item.lon2]]"
                    :options="{fillColor: '00ff00', outline: false}"
                    :marker-id="item.id"
                    hint-content=""
            />-->
            <!--<ymap-marker
                    marker-type="Rectangle"
                    :coords="[[57.665666, 39.790122], [57.617499, 39.924038]]"
                    :options="{fillColor: '00ff00', outline: false}"
                    marker-id="1"
                    hint-content="some hint"
            />
            <ymap-marker
                    marker-type="Rectangle"
                    :coords="[[57.676666, 39.801122], [57.618499, 39.925038]]"
                    :options="{fillColor: '33000099', outline: false}"
                    marker-id="2"
                    hint-content="some hint"
            />-->
        </yandex-map>
        <canvas ref="my-canvas" class="reb-Map__canvas"></canvas>
    </div>

</template>

<!--<script src="https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=c55b9816-9c45-4a43-a45a-4505c813e193" type="text/javascript"></script>-->
<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'
    import axios from 'axios'

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
            filter: Array,
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
                mapInstance: undefined,
                mapBounds: undefined,
                latHeight: undefined,
                lonWidth: undefined,
                mapWidth: undefined,
                mapHeight: undefined,
                geoData: [
                    {
                        id: 1,
                        rating: 1,
                        lat1: 57.520544,
                        lat2: 57.525544,
                        lon1: 39.695266,
                        lon2: 39.700266
                    },
                    {
                        id: 2,
                        rating: 2,
                        lat1: 57.520544,
                        lon1: 39.700267,
                        lat2: 57.525544,
                        lon2: 39.705267
                    },
                    {
                        id: 3,
                        rating: 3,
                        lat1: 57.520544,
                        lon1: 39.705268,
                        lat2: 57.525544,
                        lon2: 39.710268
                    },
                    {
                        id: 4,
                        rating: 1,
                        lat1: 57.520544,
                        lon1: 39.710269,
                        lat2: 57.525544,
                        lon2: 39.715269
                    }
                ]
                /*placemarks: [
                    {
                        //markerType: 'rectangle',
                        coords: [57.617499, 39.924038],
                        properties: {}, // define properties here
                        options: {}, // define options here
                        clusterName: "1",
                        callbacks: { click: function() {} }
                    }/!*,
                    {
                        markerType: 'rectangle',
                        coords: [[57.665666, 39.790122 ], [57.617499, 39.924038]],
                        properties: {}, // define properties here
                        options: {}, // define options here
                        clusterName: "1",
                        callbacks: { click: function() {} }
                    }*!/
                ]*/
            }
        },
        watch: {
            filter: function (val) {
                this.updateData();
            }
        },
        mounted() {
            this.updateData();
        },
        methods: {
            ratingToColor (rating) {
                switch (rating) {
                    case 1: return '#D50005'; //красн
                    case 2: return '#FFCC33'; //жел
                    case 3: return '#00CC33'; //зел
                    default: return '#FFFFFF'
                }
            },

            updateData () {
                axios
                    .get('https://rebus-hackaton.herokuapp.com/geo_data/ratings/' + this.stringFilter)
                    .then(response => {
                        this.geoData = response.data;
                        this.drawGeoDataToCanvas();
                    })
                    .catch(error => {
                        console.log(error);
                    });
            },

            drawGeoDataToCanvas () {
                // draw only after got data and initialize yandex map
                if (!this.mapBounds || !this.geoData) {
                    return;
                }
                //mapInstance
                this.calcMapSizes();

                let canvas = this.$refs['my-canvas'];
                canvas.width = this.mapWidth;
                canvas.height = this.mapHeight;
                var ctx = canvas.getContext("2d");
                ctx.clearRect(0,0,canvas.width,canvas.height);
                for (var i = 0, len = this.geoData.length; i < len; i++) {
                    let item = this.geoData[i];
                    let fill = this.ratingToColor(item.rating);
                    //console.log('fill', fill);
                    ctx.fillStyle = fill;
                    let topLeft = this.lonLatToXY(item.lon1, item.lat1);
                    let botRight = this.lonLatToXY(item.lon2, item.lat2);
                    ctx.fillRect(topLeft[0],topLeft[1],botRight[0]-topLeft[0],botRight[1]-topLeft[1]);
                }
            },

            calcMapSizes () {
                this.latHeight = this.mapBounds[1][0] - this.mapBounds[0][0];
                this.lonWidth = this.mapBounds[1][1] - this.mapBounds[0][1];
                this.mapWidth = this.mapInstance.container.getMapSize()[0];
                this.mapHeight = this.mapInstance.container.getMapSize()[1];
            },

            lonLatToXY (lon, lat) {
                let x = (lon - this.mapBounds[0][1]) / this.lonWidth * this.mapWidth ;
                let y = (lat - this.mapBounds[0][0]) / this.latHeight * this.mapHeight;
                return [x,y];
            },

            initHandler (mapInstance) {
                this.mapInstance = mapInstance;
                this.mapBounds = mapInstance.getBounds();
                this.drawGeoDataToCanvas();
                //debugger;
                //console.log('initHandler ГОТОВО');
            }
        },
        computed: {
            // вычисляемый фильтр
            stringFilter: function () {
                return (this.filter && this.filter.length) ? '?kind=' + this.filter.join(',') : '';
            }
        },
        components: {
            yandexMap, ymapMarker
        }
    }
</script>

<style>
    .reb-Map {
        width: 100%;
        height: 100%;
    }
    .reb-Map__canvas {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        opacity: .3;
    }
</style>