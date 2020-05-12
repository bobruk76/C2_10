
Array.prototype.max = function () {
  return Math.max.apply(Math, this);
}

const progressCats = document.querySelector('#progressbar-cats')
const progressParrots = document.querySelector('#progressbar-parrots')
const progressDogs = document.querySelector('#progressbar-dogs')

const header = new Headers({
  'Access-Control-Allow-Credentials': true,
  'Access-Control-Allow-Origin': '*'
})

const url = new URL('/sse/vote/stats', location)
const ES = new EventSource(url, header)

function setProgressWidth(obj, value, maxValue){
    widthProgress = Math.round(100*value/maxValue)
    obj.style.cssText = `width: ${widthProgress}%`
    obj.textContent = `${value}`
}

function createDB() {
  const urlCreateDB = new URL('/db-create', location)
  let xhr = new XMLHttpRequest();
  xhr.open("POST", urlCreateDB);
  xhr.send();
  xhr.onload = () => {console.log(xhr.response)};
}

function init() {
  ES.onerror = error => {
    ES.readyState ? progress.textContent = "Some error" : null;
  }

  ES.onmessage = ({ data }) => {

    let result = JSON.parse(data);
    let maxVotes = Object.values(result).max();

    setProgressWidth(progressCats, result.cats, maxVotes);
    setProgressWidth(progressParrots, result.parrots, maxVotes);
    setProgressWidth(progressDogs, result.dogs, maxVotes);

    let $htmlObject = document.querySelector('#crt-db-btn')
    $htmlObject.addEventListener("click", () => {createDB()});

  }

}

document.addEventListener("DOMContentLoaded", function(event) {
  init()
});