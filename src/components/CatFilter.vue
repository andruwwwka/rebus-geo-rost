<template>
    <div class="reb-CatFilter">
        <ul>
            <li>Школы</li>
            <li>Детские сады</li>
            <li>Медицина</li>
            <li>Спортивные объекты</li>
            <li>Общественный транспорт</li>
        </ul>
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
    }
</style>