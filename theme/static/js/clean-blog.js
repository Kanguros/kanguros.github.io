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

// Navbar and dropdowns
var toggle = document.getElementsByClassName("navbar-toggler")[0],
  collapse = document.getElementsByClassName("navbar-collapse")[0],
  dropdowns = document.getElementsByClassName("dropdown");

// Toggle if navbar menu is open or closed
function toggleMenu() {
  collapse.classList.toggle("collapse");
  collapse.classList.toggle("in");
}

// Close all dropdown menus
function closeMenus() {
  for (var j = 0; j < dropdowns.length; j++) {
    dropdowns[j]
      .getElementsByClassName("dropdown-toggle")[0]
      .classList.remove("dropdown-open");
    dropdowns[j].classList.remove("open");
  }
}

// Add click handling to dropdowns
for (var i = 0; i < dropdowns.length; i++) {
  dropdowns[i].addEventListener("click", function () {
    if (document.body.clientWidth < 768) {
      var open = this.classList.contains("open");
      closeMenus();
      if (!open) {
        this.getElementsByClassName("dropdown-toggle")[0].classList.toggle(
          "dropdown-open"
        );
        this.classList.toggle("open");
      }
    }
  });
}

// Close dropdowns when screen becomes big enough to switch to open by hover
function closeMenusOnResize() {
  if (document.body.clientWidth >= 768) {
    closeMenus();
    collapse.classList.add("collapse");
    collapse.classList.remove("in");
  }
}

// Event listeners
window.addEventListener("resize", closeMenusOnResize, false);
toggle.addEventListener("click", toggleMenu, false);
