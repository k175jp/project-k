<script>
	import Header from './components/Header.svelte';
	import SearchBar from './components/SearchBar.svelte';
    import QuestionList from './components/QuestionList.svelte';
  </script>
  
  <main>
	<Header />
	<SearchBar />
	<QuestionList />
  </main>
  
  <style>
	main {
	  font-family: Arial, Helvetica, sans-serif;
	  padding: 20px;
	}
  </style>
