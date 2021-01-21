function openNewPokePage(){
    var poke = document.getElementById("pokeInput").value;
    var def = "http://127.0.0.1:5000/load/";
    var page = def.concat(poke);
    window.open(page,"_self");
}