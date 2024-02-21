document.addEventListener('DOMContentLoaded', search);
const URL_API = 'http://localhost:3000/api'

var customers = []

function agregar() {
  clean()
  abrirFormulario()
}

function abrirFormulario() {
  htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class", "modale opened");
}

function cerrarModal() {
  htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class", "modale");
}

function clean() {
  document.getElementById('txtId').value = ''
  document.getElementById('txtFirstname').value = ''
  document.getElementById('txtLastname').value = ''
  document.getElementById('txtPhone').value = ''
  document.getElementById('txtAddress').value = ''
  document.getElementById('txtEmail').value = ''
}
function init(){
  search()
}

async function search(){
  var url = URL_API + '/customers'
  var response = await fetch(url, {
    'method':'GET',
    'headers':{
      'Content-Type': 'application/json'
    }
  })
  customers = await response.json();

  var html = ''
  for (customer of customers){
    row = `<tr>
      <td>${customer.first_name}</td>
      <td>${customer.last_name}</td>
      <td>${customer.email}</td>
      <td>${customer.telefono}</td>
      <td>
        <a href="#" onclick="edit(${customer.id})" class="myButton">Editar</a>
        <a href="#" onclick="remove(${customer.id})" class="btnDelete">Eliminar</a>
      </td>
      </tr>`
    html = html + row
  }


  document.querySelector('#customers > tbody').outerHTML = html;
}

function edit(id){
  abrirFormulario()
  var customer = customers.find(x => x.id == id)
  document.getElementById('txtId').value = customer.id
  document.getElementById('txtAddress').value = customer.address
  document.getElementById('txtEmail').value = customer.email
  document.getElementById('txtFirstname').value = customer.first_name
  document.getElementById('txtLastname').value = customer.last_name
  document.getElementById('txtPhone').value = customer.telefono
}

async function remove(id){
  respuesta = confirm('¿Estas seguro de que quieres eliminar el cliente?')
  if (respuesta){
    var url = URL_API + '/customers/' + id
    await fetch(url, {
      'method':'DELETE',
        'headers':{
      'Content-Type': 'application/json'
      }
    })
    window.location.reload();
    alert('Se eliminó el cliente')
  }
}

async function guardar(){
    //document.getElementById('txtFirstname').value;
    var data = {
      "address": document.getElementById('txtAddress').value,
      "email": document.getElementById('txtEmail').value,
      "first_name": document.getElementById('txtFirstname').value,
      "last_name": document.getElementById('txtLastname').value,
      "telefono": document.getElementById('txtPhone').value
    }

    var id = document.getElementById('txtId').value
    if (id != '') {
      data.id = id
    }

    var url = URL_API + '/customers'
    await fetch(url, {
      'method':'POST',
      "body": JSON.stringify(data),
        'headers':{
      'Content-Type': 'application/json'
      }
    })
    window.location.reload();
    alert('Se guardó el cliente')
}
