<%-- 
    Document   : Menu
    Created on : Sep 8, 2017, 12:08:14 AM
    Author     : estre
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <!-- Scripts-->
   <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="apple-touch-icon.png">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <!--        <link rel="stylesheet" href="css/bootstrap-theme.min.css">-->
        <!--For Plugins external css-->
        <link rel="stylesheet" href="css/plugins.css" />
        <!--Theme custom css -->
        <link rel="stylesheet" href="css/style.css">
        <!--Theme Responsive css-->
        <link rel="stylesheet" href="css/responsive.css" />
        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
        
        <script src="js/vendor/jquery-1.11.2.min.js"></script>
        <script src="js/vendor/bootstrap.min.js"></script>

        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
    </head>
   <body  data-spy="scroll" data-target="#main-navbar">
        <div class='preloader'><div class='loaded'>&nbsp;</div></div>
        <div id="menubar" class="main-menu">	
            <nav class="navbar navbar-default navbar-fixed-top">
                <div class="container">
                    <!-- Brand and toggle get grouped for better mobile display -->
                    <div class="navbar-header">
                        <h1><a href=""><B>USAC Driver</B></a></h1>                         
                    </div>
                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                       <ul class="nav navbar-nav navbar-right">
                          <li class="active"><a href="#crear">Crear<span class="sr-only">(current)</span></a></li>
                          <li><a href="#modificar">Modificar</a></li>
                          <li><a href="#eliminar">Eliminar</a></li>
                          <li><a href="#compartir">Compartir</a></li>
                          <li><a href="Inicio.jsp">SALIR &nbsp; <i class="fa fa-angle-right"></i></a></li>                              
                     </div>
                       </ul>
                    </div><!-- /.navbar-collapse -->                    
                </div><!-- /.container-fluid -->
            </nav>
        </div>
        <header id="home" class="sections"></header>       
        <section id="crear" class="sections">
           <form method="post" action="accion.php" enctype="multipart/form-data">
              Ingresa el archivo:
              <input name="imagen" type="file" />
           </form>
        </section>
        <section id="modificar" class="sections">
           
        </section>
        <section id="eliminar" class="sections">
           
        </section>
        <section id="compartir" class="sections">
           
        </section>
    </body>
</html>
