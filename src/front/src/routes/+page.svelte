<script>
    import { Card, Button } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { Toast } from 'flowbite-svelte';
    import { showLoginToast, showLogoutToast, showCreateQuizToast } from './stores';

	let questions = [];

	async function getProblemRandom() {
		const response = await fetch('http://192.168.7.5:8000/question/get', {
			method: 'GET',
			headers: {
				'Authorization': "Bearer " + localStorage.getItem('token')
 		},
		});
		questions = await response.json()
	}

    onMount(() => {
      if ($showLoginToast) {
        setTimeout(() => {
          showLoginToast.set(false);
        }, 3000);
      }
      if ($showLogoutToast) {
        setTimeout(() => {
          showLogoutToast.set(false);
        }, 3000);
      }
      if ($showCreateQuizToast) {
        setTimeout(() => {
            showCreateQuizToast.set(false);
        }, 3000);
      }
			getProblemRandom()
    });

</script>

<div class="p-8 flex justify-between items-center">
	{#each questions as question }
	<Card href="/" class="m-8 w-2xl">
		<h3 class="m-8 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{question.title}</h3>
		<p class="m-8 font-normal text-gray-700 dark:text-gray-400 leading-tight">{question.description}</p>
		<div class="p-8">
		<Button color="blue">
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd"></path></svg>
      問題を解く
    </Button>
    <Button color="green">
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"></path></svg>
      間違えた問題を復習
    </Button>
		</div>
	</Card>

	{/each}
</div>

