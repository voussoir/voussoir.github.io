function writestyle()
{
	console.log("You have pressed the giant button");
}
var swatchstate = 1;
function showhideswatch()
{
	var swatches = document.getElementById("colorswatchtable-expando");
	if (swatchstate == 0)
	{
		document.getElementById("bragaboutit").innerHTML = "Welcome to Professional Javascript";
		swatches.style.webkitAnimationName = "";
		swatches.style.webkitAnimationName = "expand";
		swatches.style.height="672px";
		swatchstate = 1;
	}
	else
	{
		swatches.style.webkitAnimationName = "";
		swatches.style.webkitAnimationName = "contract";
		swatches.style.height="0px";
		swatchstate = 0;
	}
}