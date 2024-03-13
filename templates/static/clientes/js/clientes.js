function add_carro(){

    container = document.getElementById("form-carro")

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' class='form-control' name='carro' placeholder='Carro'> </div> <div class='col-md'> <input type='text' class='form-control' name='placa' placeholder='Placa'> </div> <div class='col-md'> <input type='text' class='form-control' name='ano' placeholder='Ano'> </div> </div></div> </div> </div>"

    container.innerHTML += html


}