const copyButtonLabel = "Copy Code";

let blocks = document.querySelectorAll("div.highlight");

blocks.forEach((block) => {
    if (navigator.clipboard) {
        let button = document.createElement("button");
        button.innerText = copyButtonLabel;
        block.insertAdjacentElement("afterbegin", button);
        button.addEventListener("click", async () => {
            await copyCode(block, button);
        });
    }
});

async function copyCode(block, button) {
    let code = block.querySelector("code");
    let text = code.innerText;
    await navigator.clipboard.writeText(text);
    button.innerText = "Copied!";
    setTimeout(() => {
        button.innerText = copyButtonLabel;
    }, 1000);
}

function setTheme(isDark) {
    document.documentElement.classList.toggle("dark", isDark);
    const icon = document.getElementById("toggle-icon");
    if (icon) {
        icon.textContent = isDark ? "☽" : "☀";
    }
    localStorage.setItem("theme", isDark ? "dark" : "light");
}

function toggleDarkMode() {
    const isDark = !document.documentElement.classList.contains("dark");
    setTheme(isDark);
}

window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark)",
    ).matches;
    const isDark = savedTheme === "dark" || (!savedTheme && prefersDark);
    setTheme(isDark);
});
