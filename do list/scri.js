let inputboy = document.getElementById('inp');
let addboy = document.getElementById('but');
let test = document.getElementById('testman')

let cun = -1;

addboy.onclick = function(){
    let thing = inputboy.value.trim();
    inputboy.value = "";
    inputboy.focus();
    if(thing === "") return;
    //console.log(cun);
    cun++ 
    let t = document.createElement('tr');
    let n = document.createElement('td');
    n.textContent = cun + ":";
    n.className="cun"
    let sub = document.createElement('td');
    sub.textContent = thing;
    let delet = document.createElement('td')
    let delbutton = document.createElement('button');
    delbutton.textContent="Delete"
    delet.append(delbutton);

    t.append(n);
    t.append(sub);
    t.append(delet);
    let tbody = document.getElementById('bod')
    let addtr = document.getElementById('addtr')
    //tbody.append(t);
    tbody.insertBefore(t , addtr)

    let allcuns = document.getElementsByClassName("cun");

    delbutton.onclick = function() {
        if(confirm("are you sure?")){
            let ind = t.rowIndex - 1;
            console.log(ind);
            t.remove();
            for(let i = ind ; ind<allcuns.length ; i++){
                allcuns[i].textContent = i + ":";
            }
            //cun = cun - 2
            //console.log(cun);
        }
    }
}
test.onclick = imgadder;

     let table = document.getElementById('listy');
// function imgadder(){
//     img = document.createElement('img');
//     img.src="black.webp";
//     img.id="blackimg"
//     table.after(img);
// }

function imgadder(){
    link = document.createElement('a')
    link.href="indexxxx.html"
    img = document.createElement('img');
    img.src="void.webp"
    link.append(img)
    table.before(link)
}