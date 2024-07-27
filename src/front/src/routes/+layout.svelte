<script lang="ts">
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import "../app.css"
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, DarkMode } from 'flowbite-svelte';
  import { isLoggedIn, toasts, showToast} from './stores';
  import Fa from 'svelte-fa';
  import { faCheckCircle, faTimesCircle, faInfoCircle, faHome, faSignInAlt, faUserPlus, faSignOutAlt, faUser, faQuestionCircle } from '@fortawesome/free-solid-svg-icons';
  import { fly } from 'svelte/transition';
  import { theme } from './theme';

  let hidden = true;

  function toggleNavbar() {
    hidden = !hidden;
  }

  async function checkTokenExpiration() {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const response = await fetch('/api/user/', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        if (!response.ok) {
          throw new Error('Token expired');
        }
      } catch (error) {
        console.error('Token check failed:', error);
        localStorage.removeItem('token');
        isLoggedIn.set(false);
        showToast('セッションが期限切れです。再度ログインしてください。', 'info');
        goto('/login');
      }
    } else {
      goto("/login");
    }
  }

  onMount(async () => {
    const token = localStorage.getItem('token');
    isLoggedIn.set(!!token);

    const savedTheme = localStorage.getItem('theme') || 'light';
    theme.set(savedTheme);
    document.documentElement.setAttribute('data-theme', savedTheme);

    await checkTokenExpiration();
  });

  function handleLogout() {
    localStorage.removeItem('token');
    isLoggedIn.set(false);
    showToast('ログアウトしました', 'success');
    goto('/login');
  }

  function toggleTheme() {
    theme.update(currentTheme => {
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      localStorage.setItem('theme', newTheme);
      document.documentElement.setAttribute('data-theme', newTheme);
      return newTheme;
    });
  }
</script>

<Navbar let:hidden let:toggle class="px-4 sm:px-6 lg:px-8">
  <NavBrand href="/" class="mr-auto">
    <span class="text-2xl font-semibold text-indigo-600 dark:text-indigo-400">Project-K</span>
  </NavBrand>
  
  <div class="flex items-center order-2">
    <DarkMode on:change={toggleTheme} class="mr-4" />
    <NavHamburger on:click={toggleNavbar} class="md:hidden" />
  </div>
  
  <NavUl {hidden} class="order-1 md:flex md:items-center w-full md:w-auto">
    {#if $isLoggedIn}
      <NavLi href="/" active={$page.url.pathname === '/'}>
        <Fa icon={faHome} class="mr-2" />
        ホーム
      </NavLi>
      <NavLi on:click={handleLogout}>
        <Fa icon={faSignOutAlt} class="mr-2" />
        ログアウト
      </NavLi>
      <NavLi href="/mypage">
        <Fa icon={faUser} class="mr-2" />
        マイページ
      </NavLi>
      <NavLi href="/create-question">
        <Fa icon={faQuestionCircle} class="mr-2" />
        クイズ作成
      </NavLi>
    {:else}
      <NavLi href="/login" active={$page.url.pathname === '/login'}>
        <Fa icon={faSignInAlt} class="mr-2" />
        ログイン
      </NavLi>
      <NavLi href="/register" active={$page.url.pathname === '/register'}>
        <Fa icon={faUserPlus} class="mr-2" />
        新規登録
      </NavLi>
    {/if}
  </NavUl>
</Navbar>

<div class="toast-container">
  {#each $toasts as toast (toast.id)}
    <div
      class="toast bg-white dark:bg-gray-800 text-gray-900 dark:text-white"
      class:success={toast.type === 'success'}
      class:error={toast.type === 'error'}
      class:info={toast.type === 'info'}
      transition:fly="{{ y: 50, duration: 300, opacity: 0 }}"
    >
      <div class="toast-content">
        <div class="icon">
          {#if toast.type === 'success'}
            <Fa icon={faCheckCircle} class="text-green-500 dark:text-green-400" />
          {:else if toast.type === 'error'}
            <Fa icon={faTimesCircle} class="text-red-500 dark:text-red-400" />
          {:else}
            <Fa icon={faInfoCircle} class="text-blue-500 dark:text-blue-400" />
          {/if}
        </div>
        <div class="message text-gray-900 dark:text-gray-100">{toast.message}</div>
      </div>
      <div class="progress-bar-container bg-gray-200 dark:bg-gray-700">
        <div class="progress-bar" style="width: {toast.progress * 100}%"></div>
      </div>
    </div>
  {/each}
</div>

<main class="pt-16">
  <slot />
</main>

<style>
  .toast-container {
    position: fixed;
    bottom: 24px;
    right: 24px;
    display: flex;
    flex-direction: column-reverse;
    align-items: flex-end;
    gap: 12px;
    z-index: 1000;
  }
  .toast {
    display: flex;
    flex-direction: column;
    width: 320px;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    transition: all 0.3s ease;
    overflow: hidden;
    backdrop-filter: blur(10px);
  }
  .toast:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.18);
  }
  .toast-content {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
  }
  .icon {
    width: 24px;
    height: 24px;
    margin-right: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .message {
    font-size: 14px;
    font-weight: 500;
    line-height: 1.4;
  }
  .progress-bar-container {
    height: 4px;
    background-color: rgba(0, 0, 0, 0.1);
    border-radius: 2px;
    overflow: hidden;
  }
  .progress-bar {
    height: 100%;
    transition: width 0.1s linear;
  }
  .success {
    border-left: 4px solid #4CAF50;
  }
  .error {
    border-left: 4px solid #F44336;
  }
  .info {
    border-left: 4px solid #2196F3;
  }
  .success .progress-bar {
    background-color: #4CAF50;
  }
  .error .progress-bar {
    background-color: #F44336;
  }
  .info .progress-bar {
    background-color: #2196F3;
  }
</style>