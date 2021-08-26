function print(value){
    console.log(value);
}

export default function Select(target){
    let value = null;
    if (typeof(target) !== "string") return undefined;
    if(typeof(target) === "string"){
        value = document.querySelectorAll(target);
        if(value.length <= 1) value = document.querySelector(target);          
    }
    if(value === null) console.log(`"Element ${target}" Cannot Be Found`);
    return value;
}

let targetsList = [".app", "ul li","p"];

function selectManyTargets(targets){
    let nodeList = [];
    for(let i = 0; i < targets.length; i++){
        let node = Select(targets[i])
        nodeList.push(node)
    }
    return nodeList;
}
export {print,selectManyTargets};