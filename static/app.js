// funcion para abrir el menu del header
function abrirMenu() {
    // obtenemos el id del elemento que contiene la informacion del menu
    const menu = document.getElementById('mobile-menu')

    // usamos toggle para cambiar la clase hidden para ocultar o mostrar el menu
    menu.classList.toggle('hidden')
}