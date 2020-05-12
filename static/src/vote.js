const animals = ['cats','parrots','dogs']
const $voteForm = document.querySelector('#vote-form')

const header = new Headers({
  'Access-Control-Allow-Credentials': true,
  'Access-Control-Allow-Origin': '*'
})


// const ES = new EventSource(url, header)

function sendVote(urlLink) {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", urlLink);
  xhr.send();
  xhr.onload = () => {console.log(xhr.response)};
}

function init() {

  animals.forEach(Item => {
    const $button = `<button id="${Item}-btn" type="button" class="btn btn-dark ml-3" data-progress="${Item}">${Item.toUpperCase()}</button>`;
    let temp = document.createElement('div');
    temp.innerHTML = $button;
    let htmlObject = temp.firstChild;
    const url = `/sse/vote/${Item}`
    htmlObject.addEventListener("click", () => {sendVote(url)});
    $voteForm.appendChild(htmlObject);
    // let $obj = document.getElementById(`${Item}-btn`);
    // $obj.addEventListener("click",() => {sendVote(url)});
  });
}


document.addEventListener("DOMContentLoaded", function(event) {
  init()
});