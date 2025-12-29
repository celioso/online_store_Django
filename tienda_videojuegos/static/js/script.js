document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;
    const STORAGE_KEY = "bs-theme";

    if (!btn) {
        console.error("Botón #toggle-theme no encontrado");
        return;
    }

    // 1. Cargar tema guardado o usar light por defecto
    const savedTheme = localStorage.getItem(STORAGE_KEY) || "light";
    html.setAttribute("data-bs-theme", savedTheme);

    // 2. Alternar tema y guardarlo
    btn.addEventListener("click", function () {
        const currentTheme = html.getAttribute("data-bs-theme");
        const nextTheme = currentTheme === "dark" ? "light" : "dark";

        html.setAttribute("data-bs-theme", nextTheme);
        localStorage.setItem(STORAGE_KEY, nextTheme);
    });
});
