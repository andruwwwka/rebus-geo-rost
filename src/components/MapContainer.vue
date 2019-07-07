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
                    {id: 'infant_school', name: 'Дошкольные учреждения', enabled: true, icon: 'kindergarten'},
                    {id: 'school', name: 'Школы', enabled: true, icon: 'school'},
                    {id: 'bus_station', name: 'Транспорт', enabled: false, icon: 'bus'},
                    {id: 'hospital', name: 'Медучреждения', enabled: false, icon: 'medicine'},
                    {id: 'culture', name: 'Культурные объекты', enabled: true, icon: 'culture'},
                    {id: 'sports_ground', name: 'Спортивные объекты', enabled: true, icon: 'sport'},
                    {id: 'post_office', name: 'Почтовые отделения', enabled: true, icon: 'basket'},
                    {id: 'waste_points', name: 'Пункты РСО', enabled: false, icon: 'basket'}
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