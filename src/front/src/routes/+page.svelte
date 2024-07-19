<script>
    import { Alert } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { Toast } from 'flowbite-svelte';
    import { showLoginToast, showLogoutToast, showCreateQuizToast } from './stores';

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
    });
</script>

<div class="p-8">
    <Alert>
      <span class="font-medium">Info alert!</span> Flowbite UIのテストです。
    </Alert>
</div>

<div class="bg-blue-500 text-white p-4 rounded-lg shadow-md hover:bg-blue-600 transition-colors">
    これはTailwind CSSのテストです
</div>
