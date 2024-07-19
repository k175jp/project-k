<script lang="ts">
  import { goto } from '$app/navigation';
  import { Button, Label, Input, Card } from 'flowbite-svelte';
  import { showRegisterToast } from '../stores';

  let username = '';
  let password = '';

  async function handleSubmit() {
    try {
      const response = await fetch('http://192.168.7.5:8000/user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.status === 400) {
        alert('すでにユーザーが存在します');
        return;
      }

      if (!response.ok) {
        throw new Error('サーバーエラーが発生しました');
      }

      const result = await response.json();
      console.log(result);
      showRegisterToast.set(true);
      setTimeout(() => {
        showRegisterToast.set(false);
      }, 3000);
      goto('/login');
    } catch (error) {
      console.error('登録エラー:', error);
      alert('登録に失敗しました。もう一度お試しください。');
    }
  }
</script>

<div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
  <Card>
    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white mb-4">
      新規会員登録
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
      <Button type="submit" class="w-full">登録</Button>
    </form>
    <p class="text-sm font-light text-gray-500 dark:text-gray-400 mt-4">
      すでにアカウントをお持ちの方は<a href="/login" class="font-medium text-primary-600 hover:underline dark:text-primary-500">こちら</a>
    </p>
  </Card>
</div>
