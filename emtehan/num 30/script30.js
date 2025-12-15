let radif = document.querySelectorAll("#eykhoda tr");
let doki = document.getElementById("doki");
let max = 0;
let first = "";
doki.onclick = function(){
    for (let i = 1; i < radif.length; i++) {
        let t_ha = radif[i].querySelectorAll("td");
        console.log(t_ha[2].innerText);
        if(Number(t_ha[2].innerText) > max){
            max = t_ha[2].innerText;
            first = t_ha[0].innerText;
        }
    }
    alert( first + " ba emtiaz " + max + " bishtarin emtiaz ra darad.");
}