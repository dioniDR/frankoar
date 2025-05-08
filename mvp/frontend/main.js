
document.getElementById("btn-historia").addEventListener("click", () => {
  fetch("/mvp/backend/historia")
    .then(response => response.text())
    .then(data => {
      document.getElementById("historia").innerText = data;
    })
    .catch(err => {
      document.getElementById("historia").innerText = "Error al obtener historia.";
    });
});

document.getElementById("btn-preguntar").addEventListener("click", () => {
  const pregunta = document.getElementById("pregunta").value;
  fetch("/mvp/backend/preguntar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pregunta })
  })
    .then(response => response.text())
    .then(data => {
      document.getElementById("respuesta").innerText = data;
    })
    .catch(err => {
      document.getElementById("respuesta").innerText = "Error al enviar pregunta.";
    });
});
