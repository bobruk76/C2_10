<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
    <title>PVM A6.8</title>
  </head>
  <body>
    <div class="container-fluid">
      <h1>Vote resutls:</h1>

      <div id="cats">
        <h2>Cats</h2>
        <div class="progress mb-2">
          <div id="progressbar-cats" class="progress-bar progress-bar-striped progress-bar-animated active" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
          </div>
        </div>
      </div>

      <div id="parrots">
        <h2>Parrots</h2>
        <div class="progress mb-2">
          <div id="progressbar-parrots" class="progress-bar progress-bar-striped progress-bar-animated active" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
          </div>
        </div>
      </div>

      <div id="dogs">
        <h2>Dogs</h2>
        <div class="progress mb-2">
          <div id="progressbar-dogs" class="progress-bar progress-bar-striped progress-bar-animated active" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
          </div>
        </div>
      </div>
      <a href="/vote" target="_blank">vote yourself</a>

    </div>
    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>
    <script src="/static/src/script.js"></script>
  </body>
</html>