var arr = [];
function grabData(){

	var name= $("#artist").val();
	console.log(name);
	$.ajax({
		url: 'https://api.spotify.com/v1/search?q=' + name + "&type=track",
			success: function(result){
				

				for (var i = 0; i < result.tracks.items.length; i++){
					var strHREF = result.tracks.items[i].href;
					strHREF = strHREF.substr(34, strHREF.length);		
					arr.push(strHREF);
				}
				generateIframes(arr);
			}
	})
}

function print(adj){
	$('#content').text('');
	for(var prop in obj){
		$('#content').append('<p>' + prop + ':' + obj[prop] + '</p>');
	}
}
$('#search').click(function(){
	grabData();
})


function generateIframes(arrID){
	
}