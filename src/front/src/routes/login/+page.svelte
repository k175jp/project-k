<script lang="ts">
    import { goto } from '$app/navigation';

    let username = '';
    let password = '';

    async function handleSubmit() {
      try {
        const response = await fetch('http://192.168.7.38:8000/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        });
        const result = await response.json();

        if (result.access_token) {
          localStorage.setItem('token', result.access_token);
          console.log('トークンが保存されました:', result.access_token);
          goto('/');
        } else {
          console.error('ログインエラー: トークンが返されませんでした');
        }
      } catch (error) {
        console.error('ログインエラー:', error);
      }
    }
  </script>

  <h1>ログイン</h1>
  <form on:submit|preventDefault={handleSubmit}>
    <div>
      <label for="username">ユーザー名：</label>
      <input id="username" type="text" bind:value={username} required>
    </div>
    <div>
      <label for="password">パスワード：</label>
      <input id="password" type="password" bind:value={password} required>
    </div>
    <button type="submit">ログイン</button>
  </form>

  <p>アカウントをお持ちでない方は<a href="/register">こちら</a></p>

  <style>
    form {
      display: flex;
      flex-direction: column;
      gap: 1em;
      max-width: 300px;
      margin: 0 auto;
    }
  </style>
