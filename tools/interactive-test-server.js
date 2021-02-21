const param_container = document.getElementById("param_container")
const select_api = document.getElementById("select_api")
const select_type = document.getElementById("select_type")
const input_id = document.getElementById("input_id")

const results_container = document.getElementById("results_container")
const results_data = document.getElementById("results")

const url_api =  document.getElementById("url_api")
const url_type = document.getElementById("url_type")
const url_id = document.getElementById("url_id")

const apis = {
  'books': 'books.zoho.com/api/v3',
  'inventory': 'inventory.zoho.com/api/v1',
}

function onURLChange() {
  url_api.innerText = apis[select_api.value]
  url_type.innerText = select_type.value
  url_id.innerText = input_id.value
  for (let el of document.getElementsByClassName('actionbutton')) {
    el.disabled = select_type.value ? false : true
  }
}

function formatResults() {
  if (Object.keys(rsp).length !== 0) {
    results_data.innerText = JSON.stringify(rsp, null, 4)
    results_container.classList.remove('hidden')
    param_container.open = false
  } else {
    results_container.classList.add('hidden')
    param_container.open = true
  }
}
