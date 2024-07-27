<script>
    import { Card, Button, Label, Input } from 'flowbite-svelte';
    import { onMount } from 'svelte';

	let questions = [];
    let keyword = "";
    let k_result = "";
    let modal = false;
    let result = {};

	async function getProblemRandom() {
		const response = await fetch('/api/question/get_my_question_set', {
			method: 'GET',
			headers: {
				'Authorization': "Bearer " + localStorage.getItem('token')
 		},
		});
		questions = await response.json()
	}

    onMount(async() => {
		await getProblemRandom();
    });

    async function showModal(id){
		const response = await fetch(`/api/question/result/${id}`, {
			method: 'GET',
			headers: {
				'Authorization': "Bearer " + localStorage.getItem('token')
 		},
		});
		result = await response.json();
        modal = true;
    }

    async function hideModal() {
        result = {};
        modal = false;
    }

    async function searchKeyword() {
		const response = await fetch(`/api/question/search_me?q=${keyword}`, {
			method: 'GET',
			headers: {
				'Authorization': "Bearer " + localStorage.getItem('token')
 		},
		});
		questions = await response.json();
        k_result = keyword;
    }

</script>


{#if modal}
{#each Object.entries(result) as [key, value]}
  <Card class="mb-4">
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      User {key}
    </h5>
    <ul class="space-y-2">
      {#each value as item}
        <li class="text-gray-700 dark:text-gray-400">
          Question {item.question_id}
          Is Correct: {item.is_correct ? '✅' : '❌'}
        </li>
      {/each}
    </ul>
  </Card>
{/each}
<Button on:click={hideModal}>戻る</Button>
{:else}
<div class="m-4 flex items-center">
  <Input class="m-4 w-50" id="title" type="text" bind:value={keyword} />
  <Button on:click={searchKeyword}>検索</Button>
</div>
{#if k_result !== ""}
<div class="m-4 flex items-center">
  <Label for="title">検索結果: {k_result}</Label>
</div>
{/if}
{#if questions.length > 0}
    <Label class="m-8 text-2xl">{questions[0].username}の問題一覧</Label>
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">
	{#each questions as question }
	<Card on:click={showModal(question.id)} class="m-8 w-2xl">
		<h3 class="m-8 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{question.title} </h3>
		<p class="m-8 font-normal text-gray-700 dark:text-gray-400 leading-tight">{question.description}</p>
	</Card>

	{/each}
</div>
{/if}
{/if}