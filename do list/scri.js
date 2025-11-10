let inputboy = document.getElementById('inp');
let addboy = document.getElementById('but');
//let delboy = document.getElementsByClassName('del');

let cun = -1;

addboy.onclick = function(){
    let thing = inputboy.value.trim();
    inputboy.value = "";
    inputboy.focus();
    if(thing === "") return;
   
    cun++
     console.log(cun);
    let t = document.createElement('tr');
    let n = document.createElement('td');
    n.textContent = cun + ":";
    n.className="cun"
    let sub = document.createElement('td');
    sub.textContent = thing;
    let d = document.createElement('td')
    let b = document.createElement('button');
    b.textContent="Delete"
    d.append(b);

    t.append(n);
    t.append(sub);
    t.append(d);
    let tbody = document.getElementById('bod')
    let addtr = document.getElementById('addtr')
    //tbody.append(t);
    tbody.insertBefore(t , addtr)

    let allcuns = document.getElementsByClassName("cun");

    b.onclick = function() {
        if(confirm("are you sure?")){
            let ind = t.rowIndex - 1;
            console.log(ind);
            t.remove();
            for(let i = ind ; ind<allcuns.length ; i++){
                allcuns[i].textContent = i + ":";
            }
            //cun = cin - 2
            //console.log(cun);
        }
    }
}


