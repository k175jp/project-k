<script>
    let searchQuery = '';
    function handleSearch() {
      // Implement search logic
    }
  </script>
  
  <div>
    <input type="text" bind:value={searchQuery} placeholder="検索..." />
    <button on:click={handleSearch}>検索</button>
  </div>
  
  <style>
    div {
      display: flex;
      justify-content: center;
      margin: 20px 0;
    }
    input {
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 300px;
    }
    button {
      padding: 10px 20px;
      margin-left: 10px;
      border: none;
      background-color: #007BFF;
      color: white;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
  