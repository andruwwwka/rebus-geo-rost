<template>
    <div class="reb-MapContainer">
        <!--<span style="position: absolute; background-color: red; color: white;">MapCont</span>-->
        <Map :filter="filter"/>
        <CatFilter :items="items"
                   v-on:filter-change="filterChange"/>
    </div>
</template>

<script>
    import Map from '@/components/Map.vue'
    import CatFilter from "./CatFilter";

    export default {
        name: "MapContainer",
        data () {
            return {
                items: [
                    {id: 'infant_school', name: 'Дошкольные учреждения', enabled: true},
                    {id: 'school', name: 'Школы', enabled: true},
                    {id: 'bus_station', name: 'Транспорт', enabled: false},
                    {id: 'hospital', name: 'Медучреждения', enabled: false},
                    {id: 'culture', name: 'Культурные обхекты', enabled: true},
                    {id: 'sports_ground', name: 'Спортивные обекты', enabled: true},
                    {id: 'post_office', name: 'Почтовые отделения', enabled: true},
                    {id: 'waste_points', name: 'Пункты РСО', enabled: false}
                ]/*,
                filter: [/!*'school'*!/ 'bus_station']*/
            }
        },
        methods: {
            filterChange(filterItems) {
                /*let newFilter = [];
                for (var i = 0, len = filterItems.length; i < len; i++ ) {
                    if (filterItems[i].enabled) {
                        newFilter.push(filterItems[i].id);
                    }
                }
                this.filter = newFilter;
                //debugger;*/
            }
        },
        computed: {
            filter () {
                let newFilter = [];
                for (var i = 0, len = this.items.length; i < len; i++ ) {
                    if (this.items[i].enabled) {
                        newFilter.push(this.items[i].id);
                    }
                }
                return newFilter;
            }
        },
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