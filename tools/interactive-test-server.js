// This file is part of pyZohoAPI, Copyright (C) Todd D. Esposito 2021.
// Distributed under the MIT License (see https://opensource.org/licenses/MIT).

const param_container = document.getElementById("param_container")
const select_api = document.getElementById("select_api")
const select_type = document.getElementById("select_type")
const input_id = document.getElementById("input_id")
const input_xtrapath = document.getElementById("input_xtrapath")
const input_qparams = document.getElementById("input_qparams")

const results_container = document.getElementById("results_container")
const results_data = document.getElementById("results")
const apiinfo_container = document.getElementById("apiinfo_container")
const apiinfo_data = document.getElementById("apiinfo")

const url_api =  document.getElementById("url_api")
const url_type = document.getElementById("url_type")
const url_id = document.getElementById("url_id")
const url_xtrapath = document.getElementById("url_xtrapath")
const url_qparams = document.getElementById("url_qparams")

const apis = {
  'books': 'books.zoho.com/api/v3',
  'inventory': 'inventory.zoho.com/api/v1',
}

function onURLChange() {
  url_api.innerText = apis[select_api.value]
  url_type.innerText = select_type.value
  url_id.innerText = input_id.value ? "/" + input_id.value : ""
  url_xtrapath.innerText = input_xtrapath.value ? "/" + input_xtrapath.value : ""
  url_qparams.innerText = input_qparams.value ? "?" + input_qparams.value : ""
  for (let el of document.getElementsByClassName('actionbutton')) {
    el.disabled = select_type.value ? false : true
  }
}

function formatResults() {
  if (Object.keys(rsp).length !== 0) {
    const edopts = {
      "indentation": 4,
      "mainMenuBar": false,
      "mode": "code",
      "sortObjectKeys": true,
    }
    const editor = new JSONEditor(results_data, edopts, rsp)
    // results_data.innerText = JSON.stringify(rsp, null, 4)
    results_container.classList.remove('hidden')
    param_container.open = false
  } else {
    results_container.classList.add('hidden')
    param_container.open = true
  }
  if (Object.keys(apirsp).length !== 0) {
    apiinfo_data.innerText = JSON.stringify(apirsp, null, 4)
    apiinfo_container.classList.remove('hidden')
  } else {
    apiinfo_container.classList.add('hidden')
  }
}
