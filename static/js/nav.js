import Select, {print} from './selector.js';

let navBtn = Select(".nav-bar .wrapper .nav-items .profile-container");
let navLinkContainer = Select(".nav-bar .wrapper .nav-items .nav-links");
let navClose = true;
print(navLinkContainer)
function nav_open(navButton, target) {

    navButton.addEventListener("click", () => {
        if(navClose === true){
            target.classList.add("active");
            setTimeout(() => {
                target.style.opacity = "1";
                target.style.top = "100px";

            },100)
            navClose = false;
        }
        else if(navClose === false){
            target.style.opacity = "0";
            target.style.top = "120px";

            setTimeout(() => {
                target.classList.remove("active");
            },200)
            navClose = true;

        }
    })

}
window.addEventListener('load', () => {
    nav_open(navBtn, navLinkContainer);
})
