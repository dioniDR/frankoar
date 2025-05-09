document.getElementById("btn-historia").addEventListener("click", () => {
  fetch("http://localhost:8000/historia")
    .then(response => response.json())
    .then(data => {
      document.getElementById("historia").innerText = data.titulo + "\n\n" + data.contenido;
    })
    .catch(err => {
      document.getElementById("historia").innerText = "Error al obtener historia. Verifica que el servidor esté ejecutándose en http://localhost:8000";
    });
});

document.getElementById("btn-preguntar").addEventListener("click", () => {
  const pregunta = document.getElementById("pregunta").value;
  fetch("http://localhost:8000/preguntar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pregunta })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("respuesta").innerText = data.respuesta;
    })
    .catch(err => {
      document.getElementById("respuesta").innerText = "Error al enviar pregunta. Verifica que el servidor esté ejecutándose en http://localhost:8000";
    });
});

// Carga inicial del nombre del avatar
fetch("http://localhost:8000/avatar")
  .then(response => response.json())
  .then(data => {
    document.getElementById("nombre-avatar").innerText = data.nombre;
  })
  .catch(err => {
    console.error("Error al cargar datos del avatar:", err);
  });
