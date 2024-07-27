<script>
    import { onMount } from 'svelte';
    import { Button } from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';

    export let data;
  
    let questions = [];
    let isFetch = false;
    let currentQuestionIndex = 0;
    let selectedAnswer = null;
    let isAnswered = false;
    let answer = '';
    let isCorrect = 0;
    let result = false;
    let option = '';

    async function get_question(option) {
      let url = `/api/question/get_question_set/${data.params.question_set_id}${option}`
      const response = await fetch(url,{
        headers: {
          'Authorization': "Bearer " + localStorage.getItem('token'),
        }
      });
      questions = await response.json();
      isFetch = true;
    };
  
    onMount(async () => {
      if ($page.url.searchParams.get('mistakes') === "true") {
        option = '?mistakes=true';
      }
      await get_question(option);
    });

    async function selectAnswer(choice, select) {
      if (!isAnswered) {
        const response = await fetch(`/api/question/answer`, {
        method: 'POST',
        headers: {
          'Authorization': "Bearer " + localStorage.getItem('token'),
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          choice: select,
          question_id: questions[currentQuestionIndex].id,
          question_set_id: data.params.question_set_id
        })
      });
        answer = (await response.text()).replace(/['"]+/g, '');
        if (answer === select) {
          isCorrect = isCorrect + 1;
        }
        selectedAnswer = choice;
        isAnswered = true;
      }
    }
  
    function nextQuestion() {
      if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        selectedAnswer = null;
        isAnswered = false;
        answer = '';
      }
    }

    function gotoResult() {
        result = true;
    }

    function goHome() {
      goto("/");
    }

    function restart() {
      currentQuestionIndex = 0;
      isFetch = false;
      selectedAnswer = null;
      isAnswered = false;
      answer = '';
      isCorrect = 0;
      result = false;
    }

    async function mistakes() {
      questions = [];
      isFetch = false;
      currentQuestionIndex = 0;
      selectedAnswer = null;
      isAnswered = false;
      answer = '';
      isCorrect = 0;
      result = false;
      option = "?mistakes=true"
      await get_question(option);
    }
  </script>
  

<div class="max-w-2xl mx-auto p-4">
  {#if !result}
  {#if questions.length > 0}
    <div class="mb-4 text-right">
      <span class="text-sm text-gray-400">{currentQuestionIndex + 1}/{questions.length}</span>
    </div>
    <div class="shadow-md rounded-lg p-6 mb-4">
      <h2 class="text-xl font-bold mb-4">{isAnswered ? '答え' : '問題'}</h2>
      <p class="mb-4">{isAnswered ? answer : questions[currentQuestionIndex].text}</p>
    </div>
    <div class="grid grid-cols-2 gap-4 mb-4">
      {#each ['A', 'B', 'C', 'D'] as choice, index}
        <Button 
          color={answer === questions[currentQuestionIndex][`choice${index+1}`] ? 'green' : selectedAnswer === choice ? 'red' : 'light'} 
          class="justify-start"
          on:click={() => selectAnswer(choice, questions[currentQuestionIndex][`choice${index + 1}`])}
        >
          {choice}. {questions[currentQuestionIndex][`choice${index + 1}`]}
        </Button>
      {/each}
    </div>
    <div class="flex justify-end">
      {#if isAnswered}
        {#if currentQuestionIndex === questions.length - 1}
          <Button color="blue" on:click={gotoResult}>結果を表示</Button>
        {:else}
          <Button color="blue" on:click={nextQuestion}>次へ</Button>
        {/if}
      {/if}
    </div>
  {:else if questions.length === 0 && isFetch === true}
  <div class="mb-4 flex justify-between items-center">
    <span class="text-2xl font-bold">問題が見つかりませんでした.</span>
  </div>
  <Button color="dark" on:click={goHome}>
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
      ホームに戻る
    </Button>
  {:else}
  <div class="mb-4 flex justify-between items-center">
    <span class="text-2xl font-bold">問題を読み込んでいます...</span>
  </div>
  {/if}
  {:else}
  <div class="mb-4 flex justify-between items-center">
    <span class="text-2xl font-bold">{isCorrect}/{questions.length}</span>
  </div>
  <Button color="dark" on:click={goHome}>
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>
      ホームに戻る
    </Button>
    <Button color="blue" on:click={restart}>
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd"></path></svg>
      もう一度やり直す
    </Button>
    <Button color="green" on:click={mistakes}>
      <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"></path><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"></path></svg>
      間違えた問題を復習
    </Button>
  {/if}
</div>
