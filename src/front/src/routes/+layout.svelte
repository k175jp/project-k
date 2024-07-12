<script>
    import { page } from '$app/stores';
</script>
  
  <nav>
    <a href="/" class:active={$page.url.pathname === '/'}>ホーム</a>
    <a href="/login" class:active={$page.url.pathname === '/login'}>ログイン</a>
    <a href="/register" class:active={$page.url.pathname === '/register'}>新規登録</a>
  </nav>
  
  <main>
    <slot />
  </main>
  
  <style>
    nav {
      display: flex;
      justify-content: space-around;
      padding: 1em;
      background-color: #f0f0f0;
    }
    
    a {
      text-decoration: none;
      color: #333;
    }
    
    .active {
      font-weight: bold;
    }
    
    main {
      padding: 2em;
      max-width: 800px;
      margin: 0 auto;
    }
  </style>