const copyButtonLabel = "Copy Code";

// use a class selector if available
let blocks = document.querySelectorAll("div.highlight");

blocks.forEach((block) => {
    // only add button if browser supports Clipboard API
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
    // visual feedback that task is completed
    button.innerText = "Copied!";
    setTimeout(() => {
        button.innerText = copyButtonLabel;
    }, 1000);
}

const icon = document.getElementById("toggle-icon");

function setTheme(isDark) {
    document.body.classList.toggle("dark", isDark);
    icon.textContent = isDark ? "🌙" : "🌞";
    localStorage.setItem("theme", isDark ? "dark" : "light");
}

function toggleDarkMode() {
    const isDark = !document.body.classList.contains("dark");
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
