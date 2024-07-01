<script>
	export let name;
</script>

<main>
	<h1>Project-K</h1>
	<div class="loginAndRegister">
		<button class="login" on:click={() => window.location.href = '/login'}>ログイン</button>
		<button class="register" on:click={() => window.location.href = '/register'}>アカウント作成</button>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	div.loginAndRegister {
		display: flex;
		justify-content: center;
	}

	button {
		padding: 15px 25px;
		margin: 10px 20px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
