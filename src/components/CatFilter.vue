<template>
    <div class="reb-CatFilter">
        <div class="reb-CatFilter__list">
            <div v-for="item in items"
                 class="reb-CatFilter__item"
                 :class="{ 'reb-CatFilter__item-inactive': !item.enabled }"
                 v-on:click="itemClick(item)"
            >
                <span>
                    <!--'../assets/' + item.icon + '.svg'"-->
                    <!--<img :src="itemToIconSrc(item)" width="24px" height="24px"/>-->
                    <!--<img :src="../assets/' + item.icon + '.svg'" width="24px" height="24px"/>-->
                </span>
                <span>{{ item.name }}</span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CatFilter",
        props: {
            items: Array
        },
        data () {
            return {

            }
        },
        methods: {
            itemToIconSrc (item) {
                return  '../assets/' + item.icon + '.svg';
            },
            itemClick (item) {
                item.enabled = !item.enabled;
                this.$emit('filter-change', this.items);
            }
        }
    }
</script>

<style>
    .reb-CatFilter {
        position: absolute;
        top: 20px;
        left: 20px;
        border: blue;
        padding: 10px 0;
        background-color: white;
        border-radius: 8px;
        box-shadow: 5px 2px 9px rgba(0,0,0,0.2);
        text-align: left;
    }
    .reb-CatFilter__list {
        line-height: 2;
    }
    .reb-CatFilter__item {
        cursor: pointer;
        padding: 0 20px;
    }
    .reb-CatFilter__item:hover {
        background-color: #EBF2F7;
    }

    .reb-CatFilter__item-inactive {
        color: #949494;
    }
</style>