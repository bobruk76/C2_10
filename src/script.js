
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

const url = new URL('https://sf-pyw.mosyag.in/sse/vote/stats')
const ES = new EventSource(url, header)

function setProgressWidth(obj,value,maxValue){
    widthProgress = Math.round(100*value/maxValue)
    obj.style.cssText = `width: ${widthProgress}%`
    obj.textContent = `${value}`
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
  }

}

document.addEventListener("DOMContentLoaded", function(event) {
  init()
});