<?php
  require_once "config.php";
  if (isset($_SESSION['access_token'])) {
    header('Location: index1.php');
    exit();
  }
  $redirectURL = "http://localhost/FacebookLogin/fb-callback.php";
  $permissions = ['email'];
  $loginURL = $helper->getLoginUrl($redirectURL,$permissions);
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Log In</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
    <div class="container" style="margin-top:100px">
      <div class="row justify-content-center">
        <div class="col-md-6 col-md-offset-3" align="center"> 
            <img src="success.png"> <br> <br>
            <form>
              <input type="" name="email" placeholder="Email" class="form-control"> <br>
              <input  name="password" type="password" placeholder="Password" class="form-control"> <br>
              <input type="submit" name="" value="Log In" class="btn btn-primary">
              <input type="button" onclick="window.location = '<?php echo $loginURL ?>' " name="" value="Log In With Facebook " class="btn btn-primary">
            </form>
        </div>
      </div>
    </div>
  </body>
</html>
