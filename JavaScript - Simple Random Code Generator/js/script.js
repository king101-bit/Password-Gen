var keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$%^&*+@/~#¬";
var code='';

function getCode(btn){
	code=generateCode(16);
	document.getElementById('code').innerHTML = "<center><label style='font-size:35px; margin-top:30px; color:#FFF;'>"+code+"</label></center>";
	document.getElementById('button').removeAttribute('disabled');
	btn.setAttribute('disabled', 'disabled');
}

function generateCode(len){
	code='';
		for(i=0; i<len; i++){
			code+=keys.charAt(Math.floor(Math.random()*keys.length));
		}

	return code;
}

function checkCode(btn){
	var val=document.getElementById('ccode').value;

	if(val == ""){
		document.getElementById('result').innerHTML="<center class='text-danger'>Fill up the form first!</center>";
	}else{
		if(code==val){
			document.getElementById('result').innerHTML="The code can be use";
			document.getElementById('reset').style.display='inline';
		}else{
			document.getElementById('result').innerHTML="Invalid code";
		}
	}
}
