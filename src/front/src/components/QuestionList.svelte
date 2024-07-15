<script>
    let questions = [
      { id: 1, title: '問題1', details: '問題1の詳細です。' },
      { id: 2, title: '問題2', details: '問題2の詳細です。' },
      { id: 3, title: '問題3', details: '問題3の詳細です。' },
      { id: 4, title: '問題4', details: '問題4の詳細です。' },
      { id: 5, title: '問題5', details: '問題5の詳細です。' },
      { id: 6, title: '問題6', details: '問題6の詳細です。' },
      { id: 7, title: '問題7', details: '問題7の詳細です。' },
      { id: 8, title: '問題8', details: '問題8の詳細です。' },
      { id: 9, title: '問題9', details: '問題9の詳細です。' },
      { id: 10, title: '問題10', details: '問題10の詳細です。' }
    ];
  
    let currentPage = 1;
    const itemsPerPage = 5;
  
    function getPaginatedQuestions() {
      const start = (currentPage - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return questions.slice(start, end);
    }
  
    function goToPage(page) {
      currentPage = page;
    }
  
    $: paginatedQuestions = getPaginatedQuestions();
  </script>
  
  <div>
    {#each paginatedQuestions as question}
      <div class="question-card">
        <a href={`/questions/answer?title=${encodeURIComponent(question.title)}&details=${encodeURIComponent(question.details)}`}>
          <h2>{question.title}</h2>
          <p>{question.details}</p>
        </a>
      </div>
    {/each}
  
    <div class="pagination">
      {#each Array(Math.ceil(questions.length / itemsPerPage)) as _, index}
        <button on:click={() => goToPage(index + 1)}>{index + 1}</button>
      {/each}
    </div>
  </div>
  
  <style>
    .question-card {
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 15px;
      margin-bottom: 10px;
    }
    .question-card h2 {
      margin: 0 0 10px 0;
    }
    .question-card a {
      text-decoration: none;
      color: inherit;
    }
    .question-card a:hover {
      background-color: #f0f0f0;
    }
    .pagination {
      display: flex;
      justify-content: center;
      margin-top: 20px;
    }
    .pagination button {
      padding: 10px;
      margin: 0 5px;
      border: 1px solid #ccc;
      background-color: white;
      cursor: pointer;
    }
    .pagination button:hover {
      background-color: #007BFF;
      color: white;
    }
  </style>
  