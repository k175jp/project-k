<script lang="ts">
    import { goto } from '$app/navigation';
  
    let username = '';
    let password = '';
  
    async function handleSubmit() {
      try {
        const response = await fetch('http://192.168.7.38:8000/user/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        });
        const result = await response.json();
        console.log(result);
        // 登録成功時の処理（例：ログインページへリダイレクト）
        goto('/login');
      } catch (error) {
        console.error('登録エラー:', error);
      }
    }
  </script>
  
  <h1>新規会員登録</h1>
  <form on:submit|preventDefault={handleSubmit}>
    <div>
      <label for="username">ユーザー名：</label>
      <input id="username" type="text" bind:value={username} required>
    </div>
    <div>
      <label for="password">パスワード：</label>
      <input id="password" type="password" bind:value={password} required>
    </div>
    <button type="submit">登録</button>
  </form>
  
  <p>すでにアカウントをお持ちの方は<a href="/login">こちら</a></p>
  
  <style>
    form {
      display: flex;
      flex-direction: column;
      gap: 1em;
      max-width: 300px;
      margin: 0 auto;
    }
  </style>