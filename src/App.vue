<template>
	<Header />
	<NavBar />
	<div class="container">
		<router-view/>
	</div>
</template>

<script>
import Header from '@/components/Header'
import NavBar from '@/components/NavBar'

export default {
	components: {
		Header,
		NavBar
	},
}
</script>