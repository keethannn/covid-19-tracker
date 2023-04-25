<template>
    <div class="flex-wrap text-center inline">
        <h1 class="3-xl font-bold text-2xl">{{text}}</h1>
        <div class="text-2xl mt-2 mb-4">
            {{timestamp}}
        </div>
    </div>
</template>

<script>
    import moment from 'moment'

    export default {
        name: 'DataTitle',
        props: ['text', 'dataDate'],
        computed: {
            timestamp: function()
            {
                return moment(this.dataDate).format('MMMM Do YYYY, h:mm:ss a')
            }
        }
    }
</script>