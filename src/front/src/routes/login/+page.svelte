<script lang="ts">
  import { goto } from '$app/navigation';
  import { Button, Label, Input, DarkMode } from 'flowbite-svelte';
  import { isLoggedIn, showToast} from '../stores';
  import { fade, fly } from 'svelte/transition';
  import { cubicOut } from 'svelte/easing';

  let username = '';
  let password = '';
  let isLoading = false;
  let showMessage = false;
  let messagePosition = { x: 0, y: 0 };

  async function handleSubmit() {
    try {
      const response = await fetch('http://192.168.7.38:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      
      if (response.status === 401) {
        showToast('ユーザーが存在しません', 'error')
        return;
      }
      
      const result = await response.json();
      
      if (result.access_token) {
        localStorage.setItem('token', result.access_token);
        console.log('トークンが保存されました:', result.access_token);
        isLoggedIn.set(true);
        showToast('ログインしました', 'success');
        goto('/');
      } else {
        showToast('ログインに失敗しました', 'error');
      }
    } catch (error) {
      console.error('ログインエラー:', error);
      showToast('ログインに失敗しました', 'error');
    } finally {
      isLoading = false;
    }
  }

  function handleForgotPassword() {
    showMessage = true;
    animateMessage();
    setTimeout(() => {
      showMessage = false;
    }, 10000);
  }

  function animateMessage() {
    const interval = setInterval(() => {
      messagePosition.x = Math.random() * window.innerWidth;
      messagePosition.y = Math.random() * window.innerHeight;
      messagePosition = messagePosition;
    }, 100);

    setTimeout(() => clearInterval(interval), 10000);
  }
</script>


<div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 bg-white dark:bg-gray-800 p-10 rounded-xl shadow-2xl" in:fly="{{ y: 50, duration: 1000, easing: cubicOut }}" out:fade>
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-white" in:fly="{{ y: -20, duration: 800, delay: 300, easing: cubicOut }}">
        ログイン
      </h2>
    </div>
    <form class="mt-8 space-y-6" on:submit|preventDefault={handleSubmit}>
      <div class="rounded-md shadow-sm space-y-4">
        <div in:fly="{{ x: -50, duration: 800, delay: 500, easing: cubicOut }}">
          <Label for="username" class="sr-only">ユーザー名</Label>
          <Input id="username" name="username" type="text" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white bg-white dark:bg-gray-700 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm transition-all duration-300 ease-in-out" placeholder="ユーザー名" bind:value={username} />
        </div>
        <div in:fly="{{ x: 50, duration: 800, delay: 700, easing: cubicOut }}">
          <Label for="password" class="sr-only">パスワード</Label>
          <Input id="password" name="password" type="password" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-white bg-white dark:bg-gray-700 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm transition-all duration-300 ease-in-out" placeholder="パスワード" bind:value={password} />
        </div>
      </div>

      <div in:fly="{{ y: 50, duration: 800, delay: 900, easing: cubicOut }}">
        <Button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-300 ease-in-out" disabled={isLoading}>
          {#if isLoading}
            <span class="animate-spin mr-2">&#9696;</span>
          {/if}
          ログイン
        </Button>
      </div>
    </form>
    <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400" in:fade="{{ delay: 1100, duration: 800 }}">
      アカウントをお持ちでない方は
      <a href="/register" class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-indigo-400 dark:hover:text-indigo-300 transition-colors duration-300">
        こちら
      </a>
    </p>
    <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400" in:fade="{{ delay: 1300, duration: 800 }}">
      <a href="#" on:click|preventDefault={handleForgotPassword} class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-indigo-400 dark:hover:text-indigo-300 transition-colors duration-300">
        パスワードを忘れた方はこちら
      </a>
    </p>
  </div>
</div>

{#if showMessage}
  <div class="fixed inset-0 bg-black bg-opacity-50 z-50 overflow-hidden" transition:fade>
    {#each Array(20) as _, i}
      <div
        class="absolute text-center transform -translate-x-1/2 -translate-y-1/2 animate-pulse"
        style="left: {Math.random() * 100}%; top: {Math.random() * 100}%; animation-delay: {i * 0.05}s;"
        in:fly="{{ y: -50, duration: 500, delay: i * 50, easing: cubicOut }}"
      >
        <p class="text-4xl font-bold text-red-600 animate-bounce" style="animation-duration: {0.5 + Math.random() * 0.5}s;">
          パスワードを忘れたお前が悪い
        </p>
      </div>
    {/each}
  </div>
{/if}