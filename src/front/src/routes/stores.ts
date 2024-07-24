import { writable } from 'svelte/store';

export interface Toast {
  id: number;
  message: string;
  type: 'success' | 'error' | 'info';
  progress: number;
}

export const toasts = writable<Toast[]>([]);

export const isLoggedIn = writable(false);

let toastId = 0;

export function showToast(message: string, type: 'success' | 'error' | 'info' = 'info') {
  const id = toastId++;
  const newToast: Toast = { id, message, type, progress: 1 };
  
  toasts.update(currentToasts => [...currentToasts, newToast]);

  const interval = setInterval(() => {
    toasts.update(currentToasts => 
      currentToasts.map(t => 
        t.id === id ? { ...t, progress: t.progress - 0.02 } : t
      )
    );
  }, 100);

  setTimeout(() => {
    clearInterval(interval);
    toasts.update(currentToasts => currentToasts.filter(t => t.id !== id));
  }, 5000);
}