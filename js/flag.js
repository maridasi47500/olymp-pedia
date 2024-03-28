
$(function(){
if ($("#nom_personne").length > 0){
$("#nom_personne").keydown(function(){
var thisval=$(this).val();
if (thisval.length > 0){
$.ajax({url:"/getmoussaillon?id="+thisval,
success: function(data){
var hey=data.moussaillon;
heyperson.innerHTML="<option></option>";
for (var i = 0;i<hey.length ;i++){
heyperson.innerHTML+="<option value=\""+hey[i].id+"\">"+hey[i].pays+" "+hey[i].nom+"</option>";

}
}
});
}
});
/* search nom persone*/
$("#heyperson").change(function(){
var thisval=$(this).val();
if (thisval.length > 0){
//alert(thisval);
	if (!$('[name=my_person_ids]').toArray().some(x=>x.value===thisval)){
$.ajax({url:"/moussaillon/"+thisval+".json",
success: function(data){
var hey=data.moussaillon;


console.log("<div class=\"mouss\"><input type=\"checkbox\" name=\"my_person_ids\" checked=\"checked\" id=\"moussaillonid"+hey.id+"\" onchange=\"$('[name=person_ids]').val($('[name=my_person_ids]:checked').toArray().map(x=>String(x.value)).join(','));\" value=\""+hey.id+"\"/><label for=\"moussaillonid"+hey.id+"\">"+hey.pays+" "+hey.nom+"</label></div>");

document.getElementById("moussaillon").innerHTML+=("<div class=\"mouss\"><input type=\"checkbox\" name=\"my_person_ids\" checked=\"checked\" id=\"moussaillonid"+hey.id+"\" onchange=\"$('[name=person_ids]').val($('[name=my_person_ids]:checked').toArray().map(x=>String(x.value)).join(','));\" value=\""+hey.id+"\"/><label for=\"moussaillonid"+hey.id+"\">"+hey.pays+" "+hey.nom+"</label></div>");
$('[name=person_ids]').val($('[name=my_person_ids]:checked').toArray().map(x=>String(x.value)).join(","));

}});
}
}
});
/* search nom persone*/
}
if ($("#personne_photo").length > 0 || $("#lieu_photo").length > 0){
var fileElem=$("#personne_photo").length > 0 ? personne_photo : lieu_photo;
fileElem.addEventListener("change", handleFiles, false);

function handleFiles() {
  if (!this.files.length) {
    fileList.innerHTML = "<p>Aucun fichier sélectionné !</p>";
  } else {
    fileList.innerHTML = "";
    const list = document.createElement("ul");
    fileList.appendChild(list);
    for (let i = 0; i < this.files.length; i++) {
      const li = document.createElement("li");
      list.appendChild(li);

      const img = document.createElement("img");
      img.src = URL.createObjectURL(this.files[i]);
      img.height = 60;
      img.onload = () => {
        URL.revokeObjectURL(img.src);
      };
      li.appendChild(img);
      const info = document.createElement("span");
      info.innerHTML = `${this.files[i].name} : ${this.files[i].size} octets`;
      li.appendChild(info);
    }
  }
}
}


});
