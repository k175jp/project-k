<script lang="ts">
  import { goto } from '$app/navigation';
  import { Button, Label, Input, DarkMode } from 'flowbite-svelte';
  import { showToast } from '../stores';
  import { fade, fly } from 'svelte/transition';
  import { cubicOut } from 'svelte/easing';

  let username = '';
  let password = '';
  let isLoading = false;

  async function handleSubmit() {
    isLoading = true;
    try {
      const response = await fetch('http://192.168.7.38:8000/user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      
      if (response.status === 400) {
        showToast('すでにユーザーが存在します', 'error');
        return;
      }
      
      if (!response.ok) {
        throw new Error('サーバーエラーが発生しました');
      }
      
      const result = await response.json();
      console.log(result);
      showToast('登録しました', 'success');
      goto('/login');
    } catch (error) {
      console.error('登録エラー:', error);
      showToast('登録に失敗しました', 'error');
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 bg-white dark:bg-gray-800 p-10 rounded-xl shadow-2xl" in:fly="{{ y: 50, duration: 1000, easing: cubicOut }}" out:fade>
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-white" in:fly="{{ y: -20, duration: 800, delay: 300, easing: cubicOut }}">
        新規会員登録
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
          登録
        </Button>
      </div>
    </form>
    <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400" in:fade="{{ delay: 1100, duration: 800 }}">
      すでにアカウントをお持ちの方は
      <a href="/login" class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-indigo-400 dark:hover:text-indigo-300 transition-colors duration-300">
        こちら
      </a>
    </p>
  </div>
</div>