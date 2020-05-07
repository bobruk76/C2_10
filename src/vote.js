const animals = ['cats','parrots','dogs']
const $voteForm = document.querySelector('#vote-form')

const header = new Headers({
  'Access-Control-Allow-Credentials': true,
  'Access-Control-Allow-Origin': '*'
})

// const url = new URL('https://sf-pyw.mosyag.in/sse/vote/stats')
// const ES = new EventSource(url, header)


function init() {

  animals.forEach(Item => {
    const $button = `<button type="button" class="btn btn-dark ml-3" data-progress="${Item}">${Item.toUpperCase()}</button>`;
    let temp = document.createElement('div');
    temp.innerHTML = $button;
    let htmlObject = temp.firstChild;
    $voteForm.appendChild(htmlObject);
  });
}


document.addEventListener("DOMContentLoaded", function(event) {
  init()
});