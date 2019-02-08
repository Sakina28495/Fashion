<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="https://bootswatch.com/4/darkly/bootstrap.min.css">
	<style media="screen">
		#fb-btn{margin-top: 6px;}
		#profile,#logout{display: none;}
	</style>
	<title></title>
</head>
<body>
	<script>
		window.fbAsyncInit = function()	{
		    FB.init({
		      appId            : '210033943240879',
		      autoLogAppEvents : true,
		      xfbml            : true,
		      version          : 'v3.2'
			});

			FB.getLoginStatus(function(response) {
			    statusChangeCallback(response);
			});
		};

	  	(function(d, s, id)	{
		    var js, fjs = d.getElementsByTagName(s)[0];
		    if (d.getElementById(id)) {return;}
		    js = d.createElement(s); js.id = id;
		    js.src = "https://connect.facebook.net/en_US/sdk.js";
		    fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));

		function statusChangeCallback(response)	{
	  		if(response.status === 'connected')	{
	  			console.log('Logged in and Authenticated');
	  			setElements(true);
	  			testAPI();
	  		}
	  		else{
	  			console.log('Not Authenticated');
	  			setElements(false);
	  		}
	  	}

		function checkLoginState() {
	  		FB.getLoginStatus(function(response) {
	    	statusChangeCallback(response);
	  		});
		}

		function testAPI() {
			FB.api('me?fields=id,name,email,birthday',function(response){
				if (response && !response.error) {
					//console.log(response);
					buildProfile(response);
				}
			})
		}

		function buildProfile(user) {
			let profile = `
				<h3> ${user.name}</h3>
				<ul class="list-group">
					<li class="list-group-item"> User Id : ${user.id} </li>
					<li class="list-group-item"> Email : ${user.email} </li>
					<li class="list-group-item"> Birthday : ${user.birthday} </li>
					<li class="list-group-item"> User Id : ${user.id} </li>
				</ul>
			`;
		}

		function setElements(isLoggedIn){
			if(isLoggedIn){
				document.getElementById('logout').style.display = 'block';
				document.getElementById('profile').style.display = 'block';
				document.getElementById('fb-btn').style.display = 'none';
				document.getElementById('heading').style.display = 'none';
			} else {
				document.getElementById('logout').style.display = 'none';
				document.getElementById('profile').style.display = 'none';
				document.getElementById('fb-btn').style.display = 'block';
				document.getElementById('heading').style.display = 'block';
			}

		}

		function logout() {
			FB.logout(function(response){
				setElements(false);
			});
		}

	</script>

	<nav class="navbar navbar-expand-md navbar-dark bg-dark  navbar-default ">
     <b> <i> <a class="navbar-brand" style="color: #000000;font-size: 25pt" href="#">Comportement</a> </i></b>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a href="index.html" style="color: #000000;font-size: 14pt; margin-left: 50px">Home <span class="sr-only">(current)</span></a>
          </li>
        </ul>

        <ul class="navbar-nav">
          <li><a href="#" id="logout" onclick="logout()" style="color: #000000;font-size: 14pt; margin-left: 50px">Logout</a></li>
          	<fb:login-button 
          		id="fb-btn"
				scope="public_profile,email,user_birthday,user_location"
				onlogin="checkLoginState();">
			</fb:login-button>
          </li>
        </ul>
      </div>
    </nav>

    <div class="container">
    	<h3 id="heading">Log In to View your Profile</h3>
    	<div id="profile"></div>
    </div>
</body>
</html>