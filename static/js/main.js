import Select, {print} from './selector.js';

function noteCard(){
    let noteDropOpen = false;
    let noteCardBtn = document.querySelectorAll(".noteDisplay .noteCard .noteUser .info .info-btn");

    let noteCardDropDown = document.querySelectorAll(".noteDisplay .noteCard .noteUser .info .noteDropDown");

    for(let i = 0; i < noteCardBtn.length; i++){
        noteCardBtn[i].addEventListener('click', () => {
            noteCardDropDown[i].classList.toggle("noteDropDownActive")

        })
    }
}

window.addEventListener('load', () => {
    noteCard()
})
