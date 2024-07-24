<script lang="ts">
  import { goto } from '$app/navigation';
  import { Input, Label, Button, Toast } from "flowbite-svelte";
  import { showToast} from '../stores';

  let questions = [{ question: '', answers: ['', '', '', '']}];
  let currentIndex = 0;
  let title = "";
  let description = "";

  function addQuestion() {
    questions = [...questions, { question: '', answers: ['', '', '', '']}];
    currentIndex = questions.length - 1;
  }

  function deleteQuestion() {
    if (questions.length > 1) {
      questions = questions.filter((_, index) => index !== currentIndex);
      currentIndex = Math.max(0, currentIndex - 1);
    }
  }

  function saveQuestions() {
    let qs = [];
    for (let q of questions) {
      if (q.question === "" || q.answers.some(a => a === "")) {
        showToast('空欄があります', 'info');
        return;
      }
      qs.push({
        "text": q.question,
        "choice1": q.answers[0], 
        "choice2": q.answers[1], 
        "choice3": q.answers[2], 
        "choice4": q.answers[3]
      });
    }
    let req = {'title': title, 'description':description, 'questions': qs};
    fetch("http://192.168.7.38:30800/question/create", {
      headers: {
        "Authorization": "Bearer " + localStorage.getItem('token'),
        "Content-Type": "application/json"
      },
      body: JSON.stringify(req),
      method: "POST"
    })
    .then(response => {
      if (!response.ok) {
        if (response.status === 401) {
          showToast('ログインしてください', 'error');
        } else {
          showToast('エラーが発生しました', 'error');
        }
      } else {
        showToast('クイズを作成しました', 'success');
        goto("/");
      }
    })
    .catch(error => {
      console.error(error);
      showToast('エラーが発生しました', 'error');
    });
  }

  function nextQuestion() {
    currentIndex = Math.min(questions.length - 1, currentIndex + 1);
  }

  function prevQuestion() {
    currentIndex = Math.max(0, currentIndex - 1);
  }
</script>

<div class="container mx-auto p-4">
  <h1 class="text-2xl font-bold mb-4">問題作成</h1>

  <div class="mb-4">
    <Label for="title">タイトル</Label>
    <Input id="title" type="text" bind:value={title} />
  </div>

  <div class="mb-4">
    <Label for="description">説明</Label>
    <Input id="description" type="text" bind:value={description} />
  </div>

  <div class="mb-4">
    <Label for="question">問題</Label>
    <Input id="question" type="text" bind:value={questions[currentIndex].question} />
  </div>

  <div class="space-y-2">
    {#each questions[currentIndex].answers as answer, index}
      <div>
        <Label for={`answer-${index}`}>
          {index === 0 ? '回答1（答え）' : `回答 ${index + 1}`}
        </Label>
        <Input id={`answer-${index}`} type="text" bind:value={questions[currentIndex].answers[index]} />
      </div>
    {/each}
  </div>

  <div class="flex justify-between mt-4">
    <Button on:click={addQuestion}>追加</Button>
    <Button color="red" on:click={deleteQuestion}>削除</Button>
    <Button color="green" on:click={saveQuestions}>保存</Button>
  </div>

  <div class="flex justify-between items-center mt-4">
    <Button on:click={prevQuestion} disabled={currentIndex === 0}>&lt;</Button>
    <div>{currentIndex + 1} / {questions.length}</div>
    <Button on:click={nextQuestion} disabled={currentIndex === questions.length - 1}>&gt;</Button>
  </div>
</div>