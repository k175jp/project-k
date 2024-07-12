<script lang="ts">

	let title = '';
	let description = '';
	let questions = '';

	async function getProblemRandom() {
		const response = await fetch('http://192.168.7.38:8000/get/question_set', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ title, description, questions})
		});
		const question = await response.json
	}
</script>

<main>
	<h1>Project-K</h1>
	<div class="loginAndRegister">
		<button class="login" on:click={() => window.location.href = '/login'}>ログイン</button>
		<button class="register" on:click={() => window.location.href = '/register'}>アカウント作成</button>
	</div>
	<div>{getProblemRandom().question}</div>
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
