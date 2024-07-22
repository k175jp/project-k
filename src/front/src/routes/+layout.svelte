<script lang="ts">
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import "../app.css"
  import { NavLi, NavUl, NavHamburger, DarkMode } from 'flowbite-svelte';
  import { isLoggedIn, toasts, showToast} from './stores';
  import Fa from 'svelte-fa';
  import { faCheckCircle, faTimesCircle, faInfoCircle, faHome, faSignInAlt, faUserPlus, faSignOutAlt, faUser, faQuestionCircle } from '@fortawesome/free-solid-svg-icons';
  import { fly } from 'svelte/transition';
  import { theme } from './theme';

  let hidden = true;

  function toggle() {
    hidden = !hidden;
  }

  async function checkTokenExpiration() {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const response = await fetch('/api/auth/check-token', {
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
    goto('/');
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

<header class="fixed w-full top-0 z-50">
  <nav class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <a href="/" class="flex-shrink-0 flex items-center">
            <span class="text-2xl font-semibold text-indigo-600 dark:text-indigo-400">Project-K</span>
          </a>
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:items-center">
          <NavUl class="flex space-x-4">
            <NavLi href="/" active={$page.url.pathname === '/'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
              <Fa icon={faHome} class="mr-2" />
              ホーム
            </NavLi>
            {#if $isLoggedIn}
              <NavLi href="/" on:click={handleLogout} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
                <Fa icon={faSignOutAlt} class="mr-2" />
                ログアウト
              </NavLi>
              <NavLi href="/mypage" class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
                <Fa icon={faUser} class="mr-2" />
                マイページ
              </NavLi>
              <NavLi href="/create-question" class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
                <Fa icon={faQuestionCircle} class="mr-2" />
                クイズ作成
              </NavLi>
            {:else}
              <NavLi href="/login" active={$page.url.pathname === '/login'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
                <Fa icon={faSignInAlt} class="mr-2" />
                ログイン
              </NavLi>
              <NavLi href="/register" active={$page.url.pathname === '/register'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 px-3 py-2 text-sm font-medium transition-colors duration-200">
                <Fa icon={faUserPlus} class="mr-2" />
                新規登録
              </NavLi>
            {/if}
          </NavUl>
          <DarkMode on:change={toggleTheme} class="ml-4" />
        </div>
        <div class="sm:hidden flex items-center">
          <NavHamburger on:click={toggle} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors duration-200" />
        </div>
      </div>
    </div>
  </nav>
  {#if !hidden}
    <div transition:fly="{{ y: -50, duration: 300, opacity: 0 }}" class="sm:hidden bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <NavUl>
          <NavLi href="/" active={$page.url.pathname === '/'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
            <Fa icon={faHome} class="mr-2" />
            ホーム
          </NavLi>
          {#if $isLoggedIn}
            <NavLi href="/" on:click={handleLogout} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
              <Fa icon={faSignOutAlt} class="mr-2" />
              ログアウト
            </NavLi>
            <NavLi href="/mypage" class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
              <Fa icon={faUser} class="mr-2" />
              マイページ
            </NavLi>
            <NavLi href="/create-question" class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
              <Fa icon={faQuestionCircle} class="mr-2" />
              クイズ作成
            </NavLi>
          {:else}
            <NavLi href="/login" active={$page.url.pathname === '/login'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
              <Fa icon={faSignInAlt} class="mr-2" />
              ログイン
            </NavLi>
            <NavLi href="/register" active={$page.url.pathname === '/register'} class="text-gray-700 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 block px-3 py-2 text-base font-medium transition-colors duration-200">
              <Fa icon={faUserPlus} class="mr-2" />
              新規登録
            </NavLi>
          {/if}
        </NavUl>
        <DarkMode on:change={toggleTheme} class="mt-2" />
      </div>
    </div>
  {/if}
</header>

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