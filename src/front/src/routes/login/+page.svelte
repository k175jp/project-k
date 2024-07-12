<script lang="ts">
  import { goto } from '$app/navigation';
  import { Button, Label, Input, Card } from 'flowbite-svelte';
  import { isLoggedIn, showLoginToast } from '../stores';

  let username = '';
  let password = '';

  async function handleSubmit() {
    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      
      if (response.status === 401) {
        // エラー処理
        return;
      }
      
      const result = await response.json();
      
      if (result.access_token) {
        localStorage.setItem('token', result.access_token);
        console.log('トークンが保存されました:', result.access_token);
        isLoggedIn.set(true);
        showLoginToast.set(true);
        goto('/');
      } else {
        // エラー処理
      }
    } catch (error) {
      console.error('ログインエラー:', error);
      // エラー処理
    }
  }
</script>

<div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
  <Card>
    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white mb-4">
      ログイン
    </h1>
    <form class="space-y-4 md:space-y-6" on:submit|preventDefault={handleSubmit}>
      <div>
        <Label for="username" class="mb-2">ユーザー名</Label>
        <Input id="username" type="text" bind:value={username} required />
      </div>
      <div>
        <Label for="password" class="mb-2">パスワード</Label>
        <Input id="password" type="password" bind:value={password} required />
      </div>
      <Button type="submit" class="w-full">ログイン</Button>
    </form>
    <p class="text-sm font-light text-gray-500 dark:text-gray-400 mt-4">
      アカウントをお持ちでない方は<a href="/register" class="font-medium text-primary-600 hover:underline dark:text-primary-500">こちら</a>
    </p>
  </Card>
</div>