document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;

    if (!btn) {
        console.error("Botón #toggle-theme no encontrado");
        return;
    }

    // Tema inicial por defecto
    if (!html.hasAttribute("data-bs-theme")) {
        html.setAttribute("data-bs-theme", "light");
    }

    btn.addEventListener("click", function () {
        const currentTheme = html.getAttribute("data-bs-theme");
        const nextTheme = currentTheme === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", nextTheme);
    });
});
