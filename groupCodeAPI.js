var url= "http://maps.googleapis.com/maps/api/staticmap?center=Brooklyn,+NY&zoom=13&scale=false&size=600x300&maptype=roadmap&format=png&visual_refresh=true";

var markerStart= "&markers=icon:http://orig00.deviantart.net/7c64/f/2014/019/b/7/pikachu_yellow_sprite__revamp_by_15crashbandicoot15-d72t25s.png%7Cshadow:true%7C";

var poke= ["217 Eastern Parkway Brooklyn","350 Eastern Parkway Brooklyn", "477 Eastern Parkway Brooklyn", "373 Park Place Brooklyn", "573 Park Place Brooklyn", "212 Utica Avenue Brooklyn", "1200 Atlantic Avenue Brooklyn", "650 Atlantic Avenue Brooklyn"  ];


for(var i = 0; i < poke.length; i++){
	url= url + markerStart + encodeURI(poke[i]);
}



console.log(url);

var htmlIMG= document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src",url);





