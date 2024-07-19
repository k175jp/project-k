<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import "../app.css"
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Toast } from 'flowbite-svelte';
  import { isLoggedIn, showLoginToast, showLogoutToast, showRegisterToast, showEmptyFieldsToast, showLoginRequiredToast, showErrorToast, showCreateQuizToast } from './stores';

  onMount(() => {
    const token = localStorage.getItem('token');
    isLoggedIn.set(!!token);
  });

  function handleLogout() {
    localStorage.removeItem('token');
    isLoggedIn.set(false);
    showLogoutToast.set(true);
    setTimeout(() => {
      showLogoutToast.set(false);
    }, 3000);
    goto('/');
  }
</script>

<Navbar let:hidden let:toggle class="z-20">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
      Project-K
    </span>
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi href="/" active={$page.url.pathname === '/'}>ホーム</NavLi>
    {#if $isLoggedIn}
      <NavLi href="/" on:click={handleLogout}>ログアウト</NavLi>
      <NavLi href="/mypage">マイページ</NavLi>
      <NavLi href="/create-question">クイズ作成</NavLi>
    {:else}
      <NavLi href="/login" active={$page.url.pathname === '/login'}>ログイン</NavLi>
      <NavLi href="/register" active={$page.url.pathname === '/register'}>新規登録</NavLi>
    {/if}
  </NavUl>
</Navbar>

<main class="container mx-auto p-4 relative">
  <slot />
</main>

<div class="fixed bottom-4 right-4 z-30">
  {#if $showLoginToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showLoginToast.set(false)}>
      <svelte:fragment slot="icon">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
        <span class="sr-only">Check icon</span>
      </svelte:fragment>
      ログインしました
    </Toast>
  {/if}

  {#if $showLogoutToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showLogoutToast.set(false)}>
      <svelte:fragment slot="icon">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
        <span class="sr-only">Check icon</span>
      </svelte:fragment>
      ログアウトしました
    </Toast>
  {/if}

  {#if $showRegisterToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showRegisterToast.set(false)}>
      <svelte:fragment slot="icon">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
        <span class="sr-only">Check icon</span>
      </svelte:fragment>
      登録しました
    </Toast>
  {/if}

  {#if $showEmptyFieldsToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showEmptyFieldsToast.set(false)}>
      空欄があります
    </Toast>
  {/if}

  {#if $showLoginRequiredToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showLoginRequiredToast.set(false)}>
      ログインしてください
    </Toast>
  {/if}

  {#if $showErrorToast}
    <Toast transition="slide" autohide={true} timeout={3000} on:close={() => showErrorToast.set(false)}>
      エラーが発生しました
    </Toast>
  {/if}

  {#if $showCreateQuizToast}
    <Toast color="green" transition="slide" autohide={true} timeout={3000} on:close={() => showErrorToast.set(false)}>
      クイズを作成しました
    </Toast>
  {/if}

</div>