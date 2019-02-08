<!DOCTYPE html>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Log In</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	  <link rel="http://lipis.github.io/bootstrap-social.css/">
  </head>
 
	  <body>
		  <div class="bg-image">
		  <style>
			  .bg-image {
  background-image: url("header.jpg");
  background-color: #cccccc;
height: 768px;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
  align-self: stretch;
				
			  }
			  .logo{
				  position: relative;
					  }
			  * {
    box-sizing: border-box;
				  					  
}
			  .hover{
				  position: relative;
				  

			  }
.row {
	  
  
    display: inline-flex;

}
			  .or {
				  font-family: Baskerville, "Palatino Linotype", Palatino, "Century Schoolbook L", "Times New Roman", "serif"
			  }
			  
.image {
  display: block;
  width: 100%;
  height: auto;
		
}

.overlay {
  position: absolute; 
  bottom: 0; 
  background: rgb(0, 0, 0);
  background: rgba(0, 0, 0, 0.5); /* Black see-through */
  color: #f1f1f1; 
  width: 100%;
  transition: .5s ease;
  opacity:0;
  color: white;
  font-size: 20px;
  padding: 20px;
  text-align: center;

}

.hover:hover .overlay {
  opacity: 1;
}

.text {
  color: whitesmoke;
  font-size: 10px;
  position: absolute;
  top: 11%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
	font-family: Baskerville, "Palatino Linotype", Palatino, "Century Schoolbook L", "Times New Roman", "serif";
}
/* Create three equal columns that sits next to each other */
.column {
    flex: 33.33%;
    padding: 5px;
	border: thick;
	border-spacing: inherit;
}
		  </style>
		 
    <div class="container">
		 
      <div class="row justify-content-center">
        <div class="col-md-6 col-md-offset-3" align="center"> 
			
      <div class="logo">

            <img src="logo2.png" height="130px">

        </div>

			
            <form>
				
              <input type="" name="email" placeholder="Email" class="form-control"> <br>
              <input  name="password" type="password" placeholder="Password" class="form-control"> <br>
              <input type="submit" name="" value="Log In" class="btn btn-primary"> <br> <br>
              <input type="image" src="fb.png" alt="Submit" width="210" height="39"><br>
				
				<p class="or"> <font style="backface-visibility: "></font><font color="#F05F40">-----------------------</font><font color="white">OR SELECT YOUR STYLE</font><font color="#F05F40">---------------------</font></font></p>
            </form>
		  </div>
			<div class="row">
  <div class="column">
	  <div class="hover">
    <img src="header2.jpg" alt="" style="width: 98%">
	    <div class="overlay">
    <div class="text"><h5>THE</h5><h3>OFFICE LOOK</h3></div></div>
  </div>
  </div>
  <div class="column">
	  <div class="hover">
    <img src="header3.jpg" alt="" style="width: 98%">
	    <div class="overlay">
    <div class="text"><h3>ADVENTUROUS LOOK</h3></div></div>
	  </div></div>
  <div class="column">
 	  <div class="hover">
    <img src="header5.jpg" alt="" style="width: 98%">
	    <div class="overlay">
    <div class="text"><h3>CASUAL LOOK</h3></div></div>
	  </div></div>
  </div>
</div>

     
  </body>
</html>
