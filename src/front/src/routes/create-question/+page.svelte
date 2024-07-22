<script lang="ts">
  import { goto } from '$app/navigation';
  import { Input, Label, Alert, Button } from "flowbite-svelte";


  let questions = [{ question: '', answers: ['', '', '', '']}];
  let currentIndex = 0;
  let Modal = false;
  let Modal1 = false;
  let Modal2 = false;

  function addQuestion() {
    questions.push({ question: '', answers: ['', '', '', '']});
    questions = questions
    currentIndex = questions.length - 1;
  }

  function deleteQuestion() {
    if (questions.length > 1) {
      questions.splice(currentIndex, 1);
      questions = questions
      currentIndex = Math.max(0, currentIndex - 1);
    }
  }

  function saveQuestions() {
    console.log('Questions saved', questions);
    let qs = [];
    for (let q of questions) {
    if (q.question === "" || q.answers[0] === "" || q.answers[1] === "" || q.answers[2] === "" || q.answers[3] === "") {
        Modal = true;
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
    let req = {'title': 'title', 'description':'description', 'questions': qs};
    fetch("http://192.168.7.38:8000/question/create",{
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
            Modal1 = true;
        } else {
            Modal2 = true;
        }
      } else {
        goto("/");
      }
    })
    .catch(error => {
        console.error(error)
    })
  }

  function nextQuestion() {
    currentIndex = Math.min(questions.length - 1, currentIndex + 1);
  }

  function prevQuestion() {
    currentIndex = Math.max(0, currentIndex - 1);
  }
</script>
<!-- 
<style>
  .buttons button {
    cursor: pointer;
    flex: 1;
    margin: 5px;
  }

  .buttons button:hover {
    background-color: grey;
  }
  
  .navigation {
    display: flex;
    margin-top: 20px;
  }
</style> -->

{#if Modal}
    <Alert>空白があります</Alert>
{/if}

{#if Modal1}
    <Alert>ログインしてください</Alert>
{/if}

{#if Modal2}
    <Alert>エラーが発生しました</Alert>
{/if}

<div class="container">
  <div class="question">
    <Label for="question">問題</Label>
    <Input class="input" id="question" type="text" bind:value={questions[currentIndex].question} />
  </div>

  <div class="answers">
    {#each questions[currentIndex].answers as answer, index}
      <div>
		<Input class="input" type="text" bind:value={questions[currentIndex].answers[index]} />
      </div>
    {/each}
  </div>

  <div class="buttons">
    <Button on:click={addQuestion}>追加</Button>
    <Button on:click={deleteQuestion}>削除</Button>
    <Button on:click={saveQuestions}>保存</Button>
  </div>

  <div class="navigation">
    <Button on:click={prevQuestion}>&lt;</Button>
    <div>{currentIndex + 1} / {questions.length}</div>
    <Button on:click={nextQuestion}>&gt;</Button>
  </div>
</div>