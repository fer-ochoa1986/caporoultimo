console.log ("el codigo se esta cargando");
window.addEventListener("DOMContentLoaded", (Event) => {
console.log("DOM completamente cargado y procesado");

const menubtn = document.getElementById("menu");
const nav = document.querySelector("header nav");
const body = document.querySelector("body");
menubtn.addEventListener("click",(Event) => {
    menubtn.classList.toggle("salir");
    nav.classList.toggle("visible");
    body.classList.toggle("no-scroll");
});
});
/* funcion de carrousel */
const slides = document.querySelectorAll('.carousel-slide');

let currentSlide = 0;

function showSlide() {
  slides[currentSlide].classList.add('active');
}

function hideSlide() {
  slides[currentSlide].classList.remove('active');
}

function nextSlide() {
  hideSlide();
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide();
}

setInterval(nextSlide, 3000); // Cambiar de diapositiva cada 3 segundos

showSlide();

/*funcion de paginas para que cambien */
function mostrarPagina(nombrePagina) {
  var paginas = document.getElementsByClassName("pagina");
  for (var i = 0; i < paginas.length; i++) {
    paginas[i].style.display = "none";
  }

  var pagina = document.getElementById(nombrePagina);
  if (pagina) {
    pagina.style.display = "block";
  }
}

// Asigna eventos de clic a los enlaces de navegación para mostrar las páginas correspondientes
document.getElementById("enlace-inicio").addEventListener("click", function() {
  mostrarPagina("inicio");
});
document.getElementById("enlace-manicura").addEventListener("click", function() {
  mostrarPagina("inicio");
});
document.getElementById("enlace-depilacion").addEventListener("click", function() {
  mostrarPagina("inicio");
});

document.getElementById("enlace-productos").addEventListener("click", function() {
  mostrarPagina("productos");
});

document.getElementById("enlace-contacto").addEventListener("click", function() {
  mostrarPagina("contacto");
});
document.getElementById("enlace-ubicacion").addEventListener("click", function() {
  mostrarPagina("ubicacion");
});
/*animacion*/
      document.addEventListener("DOMContentLoaded", function() {
             var element = document.querySelector(".animate__heartBeat");
              element.classList.add("animate__animated")
              });
/*validar datos */
/*function validarFormulario() { }

var nombre = document.forms["formulario"]["nombre"].value;
var email = document.forms["formulario"]["email"].value;
var mensaje = document.forms["formulario"]["mensaje"].value;
if (nombre == "") {alert(" Ingrese su nombre.")};
return false;

/*if (email == "") {alert("Ingrese su correo electrónico.")};
return false;*/

/*if (mensaje == "") {alert("¿Que opinión tiene acerca de nuestro producto?")};
return false;

$(document).ready(function(){
    $('.menu-icon').click(function(){
      $('.menu-icon').toggleClass('active');
      $('.menu').slideToggle(300);
    });
  });
*/
/* API sql de precios y stock*/  
  
async function fetchData() {
    try {
      const response = await fetch("http://localhost/phpmyadmin/index.php?route=/database/structure&db=caporo");
      if (!response.ok) {
        throw new Error("Error en la solicitud: " + response.status);
      }
      const data = await response.json();
      // Hacer algo con los datos recibidos
      console.log(data);
    } catch (error) {
      // Manejar cualquier error ocurrido durante la solicitud
      console.error("Error:", error);
    }
  }
  
  fetchData();