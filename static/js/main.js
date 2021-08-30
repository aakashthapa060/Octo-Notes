import Select, {print} from './selector.js';

function noteCard(){
    let noteDropOpen = false;
    let noteCardBtn = document.querySelector(".noteDisplay .noteCard .noteUser .info .info-btn");

    let noteCardDropDown = document.querySelector(".noteDisplay .noteCard .noteUser .info .noteDropDown");
    noteCardBtn.addEventListener("click", () => {
        if(noteDropOpen === false){
            noteCardDropDown.style.display = "block";
            noteDropOpen = true;
            console.log("hello")
        }
        else if(noteDropOpen === true){
            noteCardDropDown.style.display = "none";
            noteDropOpen = false;
        }
    })
}

window.addEventListener('load', () => {
    noteCard()
})
