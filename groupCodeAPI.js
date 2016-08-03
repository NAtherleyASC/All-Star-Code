var url= "http://maps.googleapis.com/maps/api/staticmap?center=Brooklyn,+NY&zoom=13&scale=false&size=600x300&maptype=roadmap&format=png&visual_refresh=true";

var markerStart= "&markers=icon:http://orig00.deviantart.net/7c64/f/2014/019/b/7/pikachu_yellow_sprite__revamp_by_15crashbandicoot15-d72t25s.png%7Cshadow:true%7C";

var markerOne= "&markers=icon:http://i819.photobucket.com/albums/zz113/ElMaco18/Charmander.png%7Cshadow:true%7C";

var markerTwo= "&markers=icon:http://i153.photobucket.com/albums/s209/matt382/arceusgba.png%7Cshadow:true%7C";

var poke= ["217 Eastern Parkway Brooklyn","350 Eastern Parkway Brooklyn", "317 Dekalb Avenue Brooklyn", "373 Park Place Brooklyn", "573 Park Place Brooklyn", "212 Utica Avenue Brooklyn", "1200 Atlantic Avenue Brooklyn", "650 Atlantic Avenue Brooklyn"  ];

var pokeTwo= ["217 Dekalb Avenue Brooklyn", "477 Eastern Parkway Brooklyn", "1 E 98th Street Brooklyn"];

var pokeThree= ["10 Halsey Street Brooklyn", "100 Halsey Street Brooklyn"];

for(var i = 0; i < poke.length; i++){
	url= url + markerStart + encodeURI(poke[i]);
}


for(var i = 0; i < pokeTwo.length; i++){
	url= url + markerOne + encodeURI(pokeTwo[i]);
}

for(var i = 0; i < pokeThree.length; i++){
	url= url + markerTwo+ encodeURI(pokeTwo[i]);
}




console.log(url);

var htmlIMG= document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src",url);





