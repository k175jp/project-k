import { writable } from 'svelte/store';

export const isLoggedIn = writable(false);
export const showLoginToast = writable(false);
export const showLogoutToast = writable(false);
export const showRegisterToast = writable(false);
export const showEmptyFieldsToast = writable(false);
export const showLoginRequiredToast = writable(false);
export const showErrorToast = writable(false);
export const showCreateQuizToast = writable(false);