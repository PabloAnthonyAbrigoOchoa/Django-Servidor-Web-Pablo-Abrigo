from io import open_code
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.template import Template, Context
    
def plantilla (request):
    plantilaExterna = open()
    template = Template(plantilaExterna.read())
    plantilaExterna.close
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def index(request):
    return HttpResponse("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>DjangoServidorWeb-Pablo Abrigo</title>
    <link href="index.css" rel="stylesheet" type="text/css">
    </head>
    <style>
    @import "compass/css3";
@import url(https://fonts.googleapis.com/css?family=Vibur);
*{
  box-sizing:border-box;
  -moz-box-sizing:border-box;
  -webkit-box-sizing:border-box;
  font-family:arial;
}
body{background:#862020;}
h1{
  color:rgb(43, 42, 42);
  text-align:center;
  font-family: 'Vibur', cursive;
  font-size: 40px;
}

.login-form{
  width:350px;
  padding:40px 30px;
  background:#eee;
  @include border-radius(4px);
  margin:auto;
  position: absolute;
  left: 0;
  right: 0;
  top:10%;
  @include translateY(-50%);
}
.form-group{
  position: relative;
  margin-bottom:15px;
}
.form-control{
  width:100%;
  height:50px;
  border:none;
  padding:5px 7px 5px 15px;
  background:#fff;
  color:#666;
  border:2px solid #ddd;
  @include border-radius(4px);
}
.form-group .fa{
  position: absolute;
  right:15px;
  top:17px;
  color:#999;
}
.log-status.wrong-entry {
 @include animation( wrong-log 0.3s);
}
.log-status.wrong-entry .form-control, .wrong-entry .form-control + .fa {
  border-color: #ed1c24;
  color: #ed1c24;
}
.log-btn{
  background:#0AC986;
  dispaly:inline-block;
  width:100%;
  font-size:16px;
  height:50px;
  color:#fff;
  text-decoration:none;
  border:none;
  @include border-radius(4px);
}

.link{
  text-decoration:none;
  color:#C6C6C6;
  float:right;
  font-size:12px;
  margin-bottom:15px;
}
.alert{
  display:none;
  font-size:12px;
  color:#f00;
  float:left;
}
@include keyframes (wrong-log) {
  0%, 100% { left: 0px;}
  20% , 60%{left: 15px;}
  40% , 80%{left: -15px;}
}
    </style>
    <body>
    <div class="login-form">
        <h1>Bienvenidos</h1>
        <h1>ServidorWebDjango</h1>
        <h1>Pablo Abrigo</h1>
        <div class="form-group ">
          <input type="text" class="form-control" placeholder="Username " id="UserName">
          <i class="fa fa-user"></i>
        </div>
        <div class="form-group log-status">
          <input type="password" class="form-control" placeholder="Password" id="Passwod">
          <i class="fa fa-lock"></i>
        </div>
         <span class="alert">Invalid Credentials</span>
         <a class="link" href="#">Lost your password?</a>
        <button type="button" class="log-btn" >Log in</button>
      </div>
    </body>
</html>
    """)