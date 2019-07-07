<template>
    <div class="reb-CatFilter">
        <div class="reb-CatFilter__list">
            <div>Школы</div>
            <div class="reb-CatFilter__item-inactive">Детские сады</div>
            <div>Медицина</div>
            <div>Спортивные объекты</div>
            <div>Общественный транспорт</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CatFilter"
    }
</script>

<style>
    .reb-CatFilter {
        position: absolute;
        top: 20px;
        left: 20px;
        border: blue;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 5px 2px 9px rgba(0,0,0,0.2);
        text-align: left;
    }
    .reb-CatFilter__list {
        line-height: 2;
    }
    .reb-CatFilter__item {

    }
    .reb-CatFilter__item-inactive {
        color: #949494;
    }
</style>