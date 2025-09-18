<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Streamlit Theme Translation</title>
  <style>
    /* Base Theme */
    body {
      background-color: #FFFFFF; /* base = light */
      color: #1F1916; /* textColor */
      font-family: serif;
    }

    a {
      color: #76706C; /* linkColor */
      text-decoration: none; /* linkUnderline = false */
    }

    a:hover {
      text-decoration: underline;
    }

    /* Primary and Secondary colors */
    .primary {
      color: #56524D; /* primaryColor */
    }

    .secondary-bg {
      background-color: #E4E4E4; /* secondaryBackgroundColor */
    }

    /* Borders */
    .with-border {
      border: 1px solid #2B2523; /* borderColor */
    }

    /* Code blocks */
    code, pre {
      background-color: #D4D4D4; /* codeBackgroundColor */
      color: #1F1916;
      padding: 4px 6px;
      border-radius: 4px;
      font-family: monospace;
    }

    /* Dataframe styles */
    table.dataframe {
      border: 1px solid #2B2523; /* dataframeBorderColor */
      border-collapse: collapse;
      width: 100%;
    }

    table.dataframe th {
      background-color: #D4D4D4; /* dataframeHeaderBackgroundColor */
      border: 1px solid #2B2523;
      padding: 6px;
    }

    table.dataframe td {
      border: 1px solid #2B2523;
      padding: 6px;
    }

    /* Sidebar */
    .sidebar {
      background-color: #D4D4D4;
      border: 1px solid #2B2523;
      padding: 16px;
      font-family: serif;
      color: #1F1916; /* sidebar text */
    }

    .sidebar .primary {
      color: #56524D; /* sidebar primaryColor */
    }

    .sidebar .secondary-bg {
      background-color: #AAA39F; /* sidebar secondaryBackgroundColor */
    }

    /* Chart Colors */
    .chart-categorical {
      --cat-1: #204F80;
      --cat-2: #804F1F;
      --cat-3: #0A2845;
      --cat-4: #426F99;
      --cat-5: #45280A;
      --cat-6: #996F42;
    }

    .chart-sequential {
      --seq-1: #FDF2C5;
      --seq-2: #FCE584;
      --seq-3: #FBD453;
      --seq-4: #FBC030;
      --seq-5: #F49F1E;
      --seq-6: #DC7702;
      --seq-7: #B85300;
      --seq-8: #8F4014;
      --seq-9: #793207;
      --seq-10: #441B06;
    }
  </style>
</head>
<body>

  <div class="sidebar">
    <h2 class="primary">Sidebar Title</h2>
    <p>Sidebar content styled here.</p>
  </div>

  <main>
    <h1 class="primary">Main Title</h1>
    <p class="secondary-bg with-border">This is a block with secondary background and border.</p>
    <p>Check out this <a href="#">link</a>.</p>

    <pre><code>print("Code block example")</code></pre>

    <table class="dataframe">
      <thead>
        <tr><th>Column A</th><th>Column B</th></tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>2</td></tr>
        <tr><td>3</td><td>4</td></tr>
      </tbody>
    </table>
  </main>

</body>
</html>